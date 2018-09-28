#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import subprocess, os, time

# 身份鉴别安全测试用例

class identityIdentification(object):
    def __init__(self):
        pass

    # 读取/etc/passwd
    def handlePass(self, file_handle_pass):
        try:
            with open(file_handle_pass, 'r') as passW:
                print u'/etc/passwd系统账户信息列表:'
                for pas in passW.readlines():
                    print pas
        except Exception as e:
            print u'打开文件{0}错误'.format(file_handle_pass)

    # 读取/etc/shadow
    def handleShadow(self, file_handle_shadow):
        try:
            with open(file_handle_shadow, 'r') as shadow:
                print u'/etc/shadow系统账户信息列表:'
                for ins in shadow.readlines():
                    print ins

        except Exception as e:
            print u'打开文件{0}错误'.format(file_handle_shadow)


    # 查看账户是否为空
    def handlePassword(self, file_handle_shadow):
        args = ["awk -F: '($2 == "") {print $1}'", '{0}'.format(file_handle_shadow)]
        result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        res = result.stdout.read()
        if res == '':
            print u'账户不存在空密码'
        else:
            print  u'账户存在空密码 {0} /n'.format(res)

    # 查看系统字段
    def handleSystemAuth(self, handle_system_auth):
        try:
            with open(handle_system_auth, 'r') as systemAuth:
                print u'系统账户信息列表:'
                for lines in systemAuth:
                    lines = lines.strip().replace('\n', '')
                    if not lines.startswith("#"):
                        print lines


        except Exception as e:
            print u'打开文件{0}错误'.format(handle_system_auth)

    # 查看是否存在某些字段
    def existence(self, handle_login_defs):
        try:
            with open(handle_login_defs, 'r') as loginDefs:
                print u'系统账户信息列表:'
                for lines in loginDefs:
                    lines = lines.strip().replace('\n', '')
                    if not lines.startswith("#"):
                        print lines

        except Exception as e:
            print u'打开文件{0}错误'.format(handle_login_defs)

# 文件地址 名称
file1_1 = '/etc/passwd'
file1_2 = '/etc/shadow'
file2 = '/etc/pam.d/system-auth'
file3 = '/etc/login.defs'

funs = identityIdentification()

# 读取/etc/passwd
funs.handlePass(file1_1)

time.sleep(4)

# 读取/etc/shadow
funs.handleShadow(file1_2)

time.sleep(4)

# 查看账户是否为空
funs.handlePassword(file1_2)

time.sleep(4)

# 查看系统字段
funs.handleSystemAuth(file2)

time.sleep(4)

# 查看是否存在某些字段
funs.existence(file3)