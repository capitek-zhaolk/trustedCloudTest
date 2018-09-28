#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# DNS服务指向



class DNSServer(object):
    def __init__(self, dns_files):
        self.dns_files = dns_files
        self.dns_list = []
        self.dns_dict = {}

    # 处理数据
    def data_processing(self):
        try:
            with open(self.dns_files) as dns_file:
                print u'{0}数据为：'.format(self.dns_files)
                for line in dns_file:
                    if not line.startswith('#'):
                        self.dns_list.append(line.strip().replace('\n', ''))
            return self.dns_list
        except Exception as e:
            print u'配置文件不存在'

    # 接收数据并打印数据
    def data_receive(self):
        result = self.data_processing()
        for ins in range(len(result)):
            self.dns_dict[ result[ins].split(' ')[0] ] = result[ins].split(' ')[1]

        for k, v in self.dns_dict.items():
            if k == 'nameserver':
                print '{0} : {1}'.format(k, v)


dns_files = '/etc/resolv.conf'

dns_server = DNSServer(dns_files)

dns_server.data_receive()