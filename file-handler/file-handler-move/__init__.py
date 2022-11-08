import logging

import azure.functions as func
import paramiko

sftp_config = {
    "host": 'localhost',
    "port": 3373,
    "username": 'admin',
    "password": 'admin',
    "private_key_file": 'test/test_rsa.key'
}


class SftpServer(object):
    def __init__(self, config=sftp_config):
        # pkey = paramiko.RSAKey.from_private_key_file('/tmp/test_rsa.key')
        # transport = paramiko.Transport(('localhost', 3373))
        # transport.connect(username='admin', password='admin', pkey=pkey)
        # sftp = paramiko.SFTPClient.from_transport(transport)
        pkey = paramiko.RSAKey.from_private_key_file(config['private_key_file'])
        transport = paramiko.Transport((config['host'], config['port']))
        transport.connect(username=config['username'], password=config['password'], pkey=pkey)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def start_polling(self, file_pattern):
        self.sftp.listdir('.')
        return []

    def get(self, file_remote_path, file_local_path):
        """ Download files """
        self.sftp.get(file_remote_path, file_local_path)

    def remove(self, file_remote_path):
        self.sftp.remove(file_remote_path)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Ready to handle files ...')

    file_list = req.get_json()["files"]
    xfer_source = req.get_json()["source"]
    xfer_dest = req.get_json()["destination"]

    if len(file_list) > 0 and xfer_source == "sftp":
        sftp = SftpServer()

        for file in file_list:
            sftp.get(file, file) # TODO: connect with transport storage
            logging.info(f"{file} has been moved to storage xyz")
            sftp.remove(file)
            logging.info(f"{file} has been deleted from sftp")


    return func.HttpResponse(status_code=200)
