#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess

# 不能存在非系统默认账户或进程

'''
以用户身份登陆云主机；
查看云主机的可用账户，看是否存在非系统默认账户
查看云主机正在运行的进程
'''

class UserInfo(object):
    def __init__(self, all_args):
        self.all_args = all_args
        self.ps_list = []
        self.ps_user_list = []
        self.res_ = []

        self.passwd_user_lists = []


    # 获取数据
    def ps_user_info(self):
        for ps_args in range(len(self.all_args)):
            # ps -ef 获取正在运行的进程
            if ps_args == 0:
                result = subprocess.Popen(self.all_args[ps_args], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                while result.poll() is None:
                    lines = result.stdout.readline()
                    line =  lines.split()
                    self.ps_list.append(line)

            # cat /etc/passwd 查看可用账户
            elif ps_args == 1:
                try:
                    with open(self.all_args[ps_args], 'r') as passW:
                        for pas in passW.readlines():
                            self.res_.append( pas.strip().replace('\n', '') )
                            # print self.res_
                except Exception as e:
                    print u'打开文件{0}错误'.format(self.all_args[ps_args])

        # print u'主机正在运行的进程为{0}'.format(self.ps_list)
        return self.ps_list, self.res_


    # 处理数据
    def handle_ps_data(self):
        result = self.ps_user_info()
        print result[0]
        for ins in range(len(result)):
            if ins == 0:
                for infos_ in range(len(result[ins])):
                    if infos_ != 0:
                        self.ps_user_list.append(result[ins][infos_][0])
            elif ins == 1:
                for infos in range(len(result[ins])):
                    self.passwd_user_lists.append(result[ins][infos].split(':')[0])
            else:
                pass

        # list 去重
        self.ps_user_list = list(set(self.ps_user_list))

        # print u'云主机的可用账户为{0}'.format(self.ps_user_list)

        for each in range(len(self.ps_user_list)):
            if self.ps_user_list[each] in self.passwd_user_lists:
                print u'符合的数据为{0}'.format(self.ps_user_list[each])
                continue
            else:
                print u'不符合的数据为：{0}'.format( self.ps_user_list[each] )


# 获取正在运行的进程 命令
args_ = [
    'ps -ef',
    '/etc/passwd1'
]

user_info = UserInfo(args_)

user_info.handle_ps_data()