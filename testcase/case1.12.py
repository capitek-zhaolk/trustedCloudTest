#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 服务开启最小化

import subprocess, re

class serverSmall(object):
    def __init__(self, args):
        self.args = args
        self.res_list = []
        self.res_dict = {}
        self.res_new_dict = {}
        self.new_ = {}
        self.handle_calcul_dict = {}
        self.handle_new_calcul_dict = {}

    # 读取个服务列表信息
    def onstart(self):
        result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        while result.poll() is None:
            res = result.stdout.readline()
            line =  res.split()
            self.res_list.append(line)

        for ins in range(len(self.res_list)):
            if len( self.res_list[ins][1:] ) == 0:
                resu = '0'
                self.res_list[ins][1:] = ''.join(resu)
                self.res_dict[self.res_list[ins][0]] = self.res_list[ins][1:]
            else:
                self.res_dict[ self.res_list[ins][0] ] = self.res_list[ins][1:]

        return self.res_dict

    # 记录存在哪些服务开机启动 状态为 'on'
    def handle_calcul(self):

        result = self.onstart()

        for k_, v_ in result.items():
            if k_ and len(v_) != 0:
                for ins in range(len(v_)):
                    for i in range(len( v_[ins].split(':') )):
                        self.new_[ v_[ins].split(':')[0] ] = v_[ins].split(':')[1:]
                        self.res_new_dict[k_] = self.new_
        for k_,v_ in self.res_new_dict.items():
            for _k_, _v_ in v_.items():
                if  _v_[0] == 'on':
                    self.handle_calcul_dict[_k_] = _v_[0]
                    self.handle_new_calcul_dict[k_] = self.handle_calcul_dict

        print self.handle_new_calcul_dict, len(self.handle_new_calcul_dict)

# 查看各服务使用情况 命令
args = 'chkconfig --list'

on_start = serverSmall(args)

# 记录存在哪些服务开机启动
on_start.handle_calcul()
