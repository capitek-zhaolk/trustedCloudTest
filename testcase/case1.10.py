#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 远程管理IP限制

def remoteLimit():

    # 查看配置内容
    contrast = 'sshd:192.168.1.*:allow'

    # 文件路径
    files = '/etc/hosts.allow'

    # 存储配置文件信息，用于前端显示
    lines_list = []

    try:
        with open(files) as contrast_files:
            for line in contrast_files:
                line = line.strip().replace('\n', '')
                if line.startswith("#"):
                    continue
                else:
                    lines_list.append(line)

        for ins in range(len(lines_list)):
            if lines_list[ins] == contrast:
                print u'{0} 文件中存在这个配置'.format(files)
                break
            else:
                print u'{0} 文件中不存在这个配置'.format(files)


    except Exception as e:
        print u'文件 {0} 不存在'.format(files)


remoteLimit()