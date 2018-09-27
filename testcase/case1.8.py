#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 安全审计

import subprocess

class securityAudit(object):
    def __init__(self, auditrun, audit_logs_list ):
        self.auditrun = auditrun
        self.audit_logs_list = audit_logs_list
        self.dict_list = {}
        self.audit_logs_list_ = []

    # 查看auditd服务是否已经启动
    def audit_run(self):
        result = subprocess.Popen(self.auditrun, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        res = result.stdout.read()
        res_list = res.strip().split(':')
        for ins in range(len(res_list)):
            self.dict_list[res_list[0]] = res_list[1]

        for k, v in self.dict_list.items():
            if k == 'Active':
                if v.find('running') != -1:
                    print u'服务正在运行，状态为{0}'.format(v)
                else:
                    print u'服务已停止，状态为{0}'.format(v)


     # /var/log/audit/audit.log 查看日志
     # 查看是否存在系统安全日志内容
     # 查看是否存在用户行为日志内容
    def audit_log_status(self):
        for list_ in range(len(self.audit_logs_list)):
            args = self.audit_logs_list[list_]
            result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            res = result.stdout.read()
            if res != '':
                rows = res.strip().split('\n')
                for row in rows:
                    self.audit_logs_list_.append(row.split(','))

                if self.audit_logs_list_:
                    print u'{0}已存在日志内容'.format(args)
                else:
                    print u'{0}为空文件'.format(args)

            else:
                print u'{0}文件不存在'.format(args)



# auditd服务是否启动命令
audit_run = 'systemctl status auditd |grep Active'
# 查看日志列表信息
audit_logs_list = [
    'cat /var/log/audit/audit.log',
    'more /var/log/secure',
    'who /var/log/wtmp'
]

security_audit = securityAudit(audit_run, audit_logs_list)

#查看auditd服务是否已经启动
security_audit.audit_run()

# 查看日志
security_audit.audit_log_status()
