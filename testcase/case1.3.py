#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class loginError(object):
    def __init__(self):
        self.dict_list = {}

    def handlePamLogin(self, file_dir):
        try:
            with open(file_dir, 'r') as handle_pam_login:
                print u'登录失败锁定策略:'
                for lines in handle_pam_login:
                    lines = lines.strip().replace('\n', '')
                    if not lines.startswith("#"):
                        print lines

        except Exception as e:
            print u'打开文件{0}错误'.format(file_dir)


lgin_Error = loginError()
lgin_Error.handlePamLogin('/etc/pam.d/login')