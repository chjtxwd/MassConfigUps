# -*- coding:utf-8 -*-
import json
import requests
import socket
import os
def zabbix_api_add(ip):
    hv=ups_ip[:-2]+'23'
    print(hv)
    site=socket.gethostbyaddr(hv)[0].split(".",1)[0][:-4]
    print(site)
    if(ups_ip[-2:]=='13'):
        ups_name=site+'UPS01'
    if (ups_ip[-2:] == '14'):
        ups_name = site + 'UPS02'
    url = 'http://zabbix-cn.dktapp.cloud/zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    post_data = {
        "jsonrpc" : "2.0",
        "method" : "user.login",
        "params" : {
            "user" : "z13hchen",
            "password" : "qwert123.."
        },
        "id" : 1
    }

    ret = requests.post(url, data = json.dumps(post_data), headers = post_headers)
    print(ret.text)
    token=ret.text[27:59]


    post_data={
      "jsonrpc": "2.0",
      "method": "host.create",
      "params": {
        "host": ups_name,
        "interfaces": [
          {
            "type": 2,
            "main": 1,
            "useip": 1,
            "ip": ups_ip,
            "dns": "",
            "port": "161"
          }
        ],
        "groups": [
          {
            "groupid": "247"
          }
        ],
        "templates": [
          {
            "templateid": "10738"
          }
        ],
        "inventory": {
          "macaddress_a": "",
          "macaddress_b": ""
        }
      },
      "auth": token,
      "id": 1
    }
    ret = requests.post(url, data = json.dumps(post_data), headers = post_headers)
    print(ret.text)
for filename in os.listdir('C://Users//BACKUP//Desktop//ups//'):
    check_ip=filename.find('.ini')
    if (check_ip != int('-1')) :
        ups_ip=filename[:-4]
        zabbix_api_add("ups_ip")


