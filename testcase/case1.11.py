#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 登录超时锁定

def timeClock():

    files = '/etc/profile'

    timeout_dict = {}

    try:
        with open(files) as timeout_:
            print u'登录超时锁定时间:'
            for line in timeout_:
                line = line.strip().replace('\n', '')
                if line.find('TIMEOUT') != -1:
                    timeout_dict[line.split('=')[0]] = line.split('=')[1]
                else:
                    continue

        for k, v in timeout_dict.items():
            print '{0} : {1}'.format(k, v)

    except Exception as e:
        print u'{0}文件不存在'.format(files)


timeClock()