#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 访问控制

import subprocess, os, time

class rhetoricalControl(object):
    def __init__(self):
        self.dict_list = {}

    # 限制root用户无法通过ssh直接登录；
    def handle_ssh(self, file_dir_ssh):
        print u'cat /etc/ssh/sshd_config数据是：'
        try:
            with open(file_dir_ssh, 'r') as dict_ssh:
                for lines in dict_ssh:
                    lines = lines.strip().replace('\n', '')

                    if lines.startswith("#"):
                        continue
                    else:
                        resu = lines.split(' ')
                        k_ = resu[0].strip('#')
                        v_ = resu[1:]
                        self.dict_list[k_] = v_
                    #
                    # if lines.find('#') == -1:
                    #     resu = lines.split(' ')
                    #     k_ = resu[0].strip('#')
                    #     v_ = resu[1:]
                    #     self.dict_list[k_] = v_

            for k, v in self.dict_list.items():
                if k == 'PermitRootLogin':
                    print '{0}: {1}'.format(k, v[0])

        except Exception as e:
            print u'打开文件{0}错误'.format(file_dir_ssh)

    # 用户缺省访问权限；
    def handle_bashrc(self, file_dir_bashrc):
        print u'cat /etc/bashrc数据是：'
        try:
            with open(file_dir_bashrc, 'r') as dict_basgrc:
                for lines in dict_basgrc:
                    lines = lines.strip().replace('\n', '')

                    if lines.startswith("#"):
                        continue
                    else:
                        resu = lines.split(' ')
                        for i in range(len(resu)):
                            self.dict_list[resu[0]] = resu[1:]

            for k,v in self.dict_list.items():
                if k == 'umask':
                    print '{0} : {1}'.format(k, v[0])

        except Exception as e:
            print u'{0}配置文件目录不存在'.format( file_dir_bashrc )

    # 应配置帐户对日志文件读取、修改和删除等操作权限进行限制
    def handle_logs(self, list_logs):
        try:
            print '文件权限是：'
            for ins in range(len(list_logs)):
                args = ['ls -l {0}'.format(list_logs[ins])]
                result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                res = result.stdout.read()
                if res == '':
                    print u'{0} 目录不存在'.format(format(list_logs[ins]))
                else:
                    print '{0}'.format(res)
        except Exception as e:
            print e


# 查看权限目录地址
list_logs = [
    # '/var/log/messages',
    # '/var/log/secure',
    # '/var/log/maillog',
    # '/var/log/cron',
    # '/var/log/spooler',
    # '/var/log/boot.log'

    '/var/log/kern.log',
    '/var/log/kern.log.1',
    '/var/log/kern.log.2.gz',
    '/var/log/syslog',
    '/var/log/syslog.1',
    '/var/log/syslog.2.gz',
]

conFuns = rhetoricalControl()


# 限制root用户无法通过ssh直接登录；
conFuns.handle_ssh('/etc/ssh/sshd_config')

time.sleep(4)

# 用户缺省访问权限；
conFuns.handle_bashrc('/etc/bashrc')

time.sleep(4)

# 应配置帐户对日志文件读取、修改和删除等操作权限进行限制
conFuns.handle_logs(list_logs)