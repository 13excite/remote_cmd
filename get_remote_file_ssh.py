#!/usr/bin/env python

import paramiko
import os


hostname = '192.168.56.101'
port = 22
username = 'root'
passwprd = '123'
dir_path = '/var/log/uwsgi/uwsgi.log'

if __name__ == '__main__':
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=passwprd)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print('Retrieving', f)
        sftp.get(os.path.join(dir_path, f), f)
    t.close()
