import logging

import azure.functions as func
import requests

from ..helpers.SftpServer import SftpServer

FILE_HANDLER_URL = 'http://localhost:7073/api/file-handler'


def main(_timer) -> func.HttpResponse:
    logging.info("File Watcher Ready ...")

    try:
        sftp = SftpServer()
        trigger_files = sftp.start_polling("*.trg")

        logging.info(f"trigger_files: {trigger_files}")

        if len(trigger_files) > 0:
            logging.info(f"Trigger files have been detected. Number of files: {len(trigger_files)}.")
            logging.info(f"Start to transfer files: {trigger_files}")

            data = {"files": trigger_files, "source": "sftp", "destination": "transfer"}
            requests.post(FILE_HANDLER_URL, data=data)
            logging.info(f"Making HTTP request to FileHandler App with payload: {data}")
        else:
            logging.info("No trigger files found.")

    except requests.exceptions.HTTPError as he:
        logging.error(he.response.text)
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        logging.error(f"Error has occurred: {e}")
