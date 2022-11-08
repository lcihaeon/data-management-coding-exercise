import json, requests
import logging

import azure.functions as func
import paramiko
import fnmatch
import pdb

sftp_config = {
    "host": 'localhost',
    "port": 3373,
    "username": 'admin',
    "password": 'admin',
    "private_key_file": 'test/test_rsa.key'
}
FILE_HANDLER_URL = 'http://localhost:7073/api/file-handler'


class SftpServer(object):
    def __init__(self, config=sftp_config):
        # pkey = paramiko.RSAKey.from_private_key_file('/tmp/test_rsa.key')
        # transport = paramiko.Transport(('localhost', 3373))
        # transport.connect(username='admin', password='admin', pkey=pkey)
        # sftp = paramiko.SFTPClient.from_transport(transport)
        # pdb.set_trace()
        pkey = paramiko.RSAKey.from_private_key_file(config['private_key_file'])
        transport = paramiko.Transport((config['host'], config['port']))
        transport.connect(username=config['username'], password=config['password'], pkey=pkey)
        self._sftp = paramiko.SFTPClient.from_transport(transport)

    def start_polling(self, file_pattern):
        matching_files = []
        for f in self._sftp.listdir('.'):
            if fnmatch.fnmatch(f, file_pattern):
                matching_files.append(f)

        return matching_files

    def get(self, file_remote_path, file_local_path):
        """ Download files """
        self._sftp.get(file_remote_path, file_local_path)

    def remove(self, file_remote_path):
        self._sftp.remove(file_remote_path)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("File Watcher Ready ...")

    sftp = SftpServer()
    trigger_files = sftp.start_polling("*.trg")

    logging.info(f"trigger_files: {trigger_files}")

    if len(trigger_files) > 0:
        logging.info(f"Trigger files have been detected. Number of files: {len(trigger_files)}.")
        logging.info(f"Start to transfer files: {trigger_files}")

        data = {"files": trigger_files, "source": "sftp", "destination": "transfer"}
        requests.post(FILE_HANDLER_URL, data=data)
        # logging.info(f"Making HTTP request for data: {data}")
    else:
        logging.info("No trigger files found.")

    return func.HttpResponse(status_code=200)
