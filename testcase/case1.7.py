#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 帐号文件保护

import subprocess

class accountProtection(object):
    def __init__(self, lists):
        self.lists = lists

    # 获取文件权限
    def account_files(self):
        for list in range(len(self.lists)):
            args = 'ls -l {0}'.format( self.lists[list] )
            result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            res = result.stdout.read()

            if res == '':
                print u'{0}文件不存在'.format( self.lists[list] )
            else:
                print u'{0}文件权限为{1}'.format(self.lists[list], res)



account_lists = ['/etc/passwd', '/etc/shadow', '/etc/group']

account_protection = accountProtection(account_lists)

# 获取文件权限
account_protection.account_files()
