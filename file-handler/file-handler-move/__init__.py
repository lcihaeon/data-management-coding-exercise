import fnmatch
import logging
import os

import azure.functions as func

from ..helpers.FileParser import *
from ..helpers.FileValidator import *
from ..helpers.SftpServer import SftpServer


class ExceptionWithMessage(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class RecordCountMismatchError(ExceptionWithMessage):
    pass


class ChecksumMismatchError(ExceptionWithMessage):
    pass


class SftpFileNotFoundError(ExceptionWithMessage):
    pass


def str_to_byte_array(message: str):
    b = bytearray()
    b.extend(map(ord, message))
    return b


def main(req: func.HttpRequest, xferStorage: func.Out[bytes], errorStorage: func.Out[bytes]) -> func.HttpResponse:
    logging.info('Ready to handle files ...')

    file_list = req.get_json()["files"]
    xfer_source = req.get_json()["source"]

    #
    xfer_dest = req.get_json()["destination"]

    try:
        if len(file_list) > 0 and xfer_source == "sftp":
            logging.debug(f"Ready to process the following files: {file_list}")

            sftp = SftpServer()

            for file in file_list:

                # Discard files that are not triggers
                if not fnmatch.fnmatch(file, '*.trg'):
                    logging.info(f"File ${file} is not a trigger file. ")
                    continue

                try:
                    sftp.get(file, file)
                except FileNotFoundError:
                    raise SftpFileNotFoundError(f"File {file} not found on sftp server")
                logging.info(f"{file} has been downloaded")
                sftp.remove(file)
                logging.info(f"{file} has been deleted from sftp")

                data_file_name, file_type, record_count, checksum = get_data_file_meta(file)

                if data_file_name:
                    try:
                        sftp.get(data_file_name, data_file_name)
                    except FileNotFoundError:
                        raise SftpFileNotFoundError(f"File {data_file_name} not found on sftp server")
                    logging.info(f"{data_file_name} has been downloaded")
                    sftp.remove(data_file_name)
                    logging.info(f"{data_file_name} has been deleted from sftp")

                    # upload data file to transfer storage
                    with open(file, "rb") as in_file:
                        xferStorage.set(in_file.read())
                        # TODO: invoke file-handler-validate locally

                    logging.info(f"{data_file_name} has been uploaded to blob transfer storage successfully")

                    try:
                        # TODO: this may be replaced by a http call to the FileValidator api
                        validate_row_count(data_file_name, record_count)
                    except AssertionError:
                        raise RecordCountMismatchError(f"Row count in file {data_file_name} does not match {record_count} provided in {file}")

                    try:
                        # TODO: this may be replaced by a http call to the FileValidator api
                        validate_checksum(data_file_name, checksum)
                    except AssertionError:
                        raise ChecksumMismatchError(f"Checksum in file {data_file_name} does not match {checksum} provided in {file}")

                    # clean up
                    os.remove(data_file_name)

                else:
                    return func.HttpResponse(f"File {file} does not contain data file name", status_code=200)

                # clean up
                os.remove(file)

        logging.debug(f"List of files is empty. Nothing to process.")

    except SftpFileNotFoundError as fnfe:
        logging.error(fnfe.message)
        logging.info("Sending error message to error storage")
        errorStorage.set(str_to_byte_array(fnfe.message))
        return func.HttpResponse(fnfe.message, status_code=200)
    except RecordCountMismatchError as rcme:
        logging.error(rcme.message)
        logging.info("Sending error message to error storage")
        errorStorage.set(str_to_byte_array(rcme.message))
        return func.HttpResponse(rcme.message, status_code=200)
    except ChecksumMismatchError as cme:
        logging.error(cme.message)
        logging.info("Sending error message to error storage")
        errorStorage.set(str_to_byte_array(cme.message))
        return func.HttpResponse(cme.message, status_code=200)

    return func.HttpResponse("complete", status_code=200)
