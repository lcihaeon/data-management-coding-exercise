import paramiko
import fnmatch


class SftpServer(object):
    SFTP_CONFIG = {
        "host": 'localhost',
        "port": 3373,
        "username": 'admin',
        "password": 'admin',
        "private_key_file": 'tests/test_rsa.key'
    }

    def __init__(self, config=SFTP_CONFIG):
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
        """ Download remote file to local"""
        self._sftp.get(file_remote_path, file_local_path)

    def remove(self, file_remote_path):
        """ Remove remote file """
        self._sftp.remove(file_remote_path)
