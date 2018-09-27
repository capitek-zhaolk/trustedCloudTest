#!/usr/bin/env python
#-*- coding:utf-8 -*-

import paramiko

# 服务器地址
hostname = '172.17.0.229'
port = 22
username = 'root'
password = '111'
cmd = 'df -h'

class sshLineServer(object):
    def __init__(self, ip, port, username, password, cmd):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    # ssh 连接服务器
    def ssh_line_server(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        try:
            ssh.connect(self.ip, self.port, self.username, self.password)
            stdin, stdout, stderr = ssh.exec_command(self.cmd)
            result = stdout.read()
            if not result:
                result = stderr.read()

            print u'云主机登录成功'
            print result.decode()

        except Exception as e:
            print u'请确认服务器数据的正确性'


ssh_ = sshLineServer(hostname, port, username, password, cmd)

# ssh 连接服务器
ssh_.ssh_line_server()
