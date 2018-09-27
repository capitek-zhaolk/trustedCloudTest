#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 传输安全

import time


class transSecurity(object):
    def __init__(self):
        self.dict_list = {}
        self.telnet_list = {}

    # 读取/etc/xinetd.d/telnet
    def handle_telnet(self, file_dir_telnet):
        try:
            with open(file_dir_telnet) as json_telnet:
                for line in json_telnet:
                    self.telnet_list[line.strip().split('\n')[0].split('=')[0]] = line.strip().split('\n')[0].split('=')[1:]

            print u'disable的字段是：'
            for k,v in self.telnet_list.items():
                if k == 'disable':
                    if v[0] == 'no':
                        print u'disable：{0}'.format(v[0])
                    else:
                        print u'disable:{0}'.format(v[0])

        except Exception as e:
            print u'打开文件{0}错误'.format(file_dir_telnet)

    # 读取/etc/ssh/sshd_config
    def handle_ssh(self, file_dir_ssh):
        try:
            with open(file_dir_ssh, 'r') as dict_ssh:
                for lines in dict_ssh:
                    lines = lines.strip().replace('\n', '')

                    if lines.startswith("#"):
                        continue
                    else:
                        resu = lines.split(' ')
                        for li in range(len(resu)):
                            self.dict_list[resu[0]] = resu[1:]

            print u'Protocol字段是:'
            for k, v in self.dict_list.items():
                if k == 'Protocol':
                    print '{0} : {1}'.format(k, v[0])

        except Exception as e:
            print u'打开文件{0}错误'.format(file_dir_ssh)


transFuns = transSecurity()

# 读取 telnet
transFuns.handle_telnet('/etc/xinetd.d/telnet')

time.sleep(4)

# 读取 sshd
transFuns.handle_ssh('/etc/ssh/sshd_config')