#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import datetime
import json
import struct

import requests

import password


class BgBillingApi:
    url = 'http://127.0.0.1:8080/bgbilling/executer/json/'
    _login = password.login
    _password = password.password

    def __init__(self, cid):
        self.cid = cid

    def contract_parameter_get(self, param):
        """

        :param param = id параметра договора:
        :param url:
        :return: Возвращает значение параметра договора, как адрес, номер телефона и т.д..
        """
        params = {'method': 'contractParameterGet',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'contractId': self.cid,
                          'parameterId': param
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.kernel.contract.api/ContractService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return").get('value')
        except:
            value = None
        return value

    def get_contract_balance(self):
        """

        :param url:
        :return: balance of contract
        """
        url = self.url + 'ru.bitel.bgbilling.kernel.contract.balance/BalanceService'
        now = datetime.datetime.now()
        param = {
            "method": "contractBalanceGet",
            "user":
                {"user": self._login,
                 "pswd": self._password},
            "params":
                {"contractId": self.cid,
                 "year": now.year,
                 "month": now.month}
        }
        balance = requests.post(url, json=param)
        json_data = json.loads(balance.text)
        try:
            incoming_saldo = json_data.get('data').get('return').get('incomingSaldo')
            payments = json_data.get('data').get('return').get('payments')
            accounts = json_data.get('data').get('return').get('accounts')
            total = int(incoming_saldo + payments - accounts)
        except:
            total = None
        return total

    def get_contract(self):
        """
        {'id': 20566, 'title': '0002413', 'groups': 9, 'password': '5045455', 'dateFrom': '2017-03-23', 'dateTo': None,
        'balanceMode': 1, 'paramGroupId': 1, 'personType': 0, 'comment': 'Октябрьская дом 52 кв 5 Будунова Асият ',
        'hidden': False, 'superCid': 0, 'dependSubList': '', 'status': 0, 'statusTimeChange': '2022-11-04',
        'titlePatternId': 1, 'balanceSubMode': 0, 'domainId': 0, 'dependSub': False, 'balanceLimit': 0.0,
        'sub': False, 'super': False, 'independSub': False}
        """
        params = {'method': 'contractGet',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'contractId': self.cid
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.kernel.contract.api/ContractService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return")
        except:
            value = None
        return value

    def hasModuleInstanceInet(self):
        params = {'method': 'hasModuleInstance',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'contractId': self.cid,
                          'moduleId': 1
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.kernel.contract.api/ContractService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return")
        except:
            value = None
        return value

    def hasModuleInstanceAbon(self):
        params = {'method': 'hasModuleInstance',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'contractId': self.cid,
                          'moduleId': 3
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.kernel.contract.api/ContractService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return")
        except:
            value = None
        return value

    def get_tariff(self):
        """
        {'id': 20566, 'contractId': 20584, 'tariffPlanId': 14, 'dateFrom': '2017-03-01T00:00:00+03:00',
        'dateTo': '2017-11-30T00:00:00+03:00', 'comment': '', 'position': 0, 'entityMid': 0, 'entityId': 0, 'replacedFromContractTariffId': 0
        """
        params = {'method': 'contractTariffGet',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'id': self.cid
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.kernel.contract.api/ContractTariffService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return")
        except:
            value = None
        return value

    def inetServGet(self):
        """
        {'id': 22059, 'title': 'port:26_10.107.142.26', 'parentId': 0, 'children': None, 'contractTitle': None, 'contractComment': None,
        'typeTitle': 'use - IPoe по трафику', 'deviceTitle': 'ELTEX_MES1124MB: [172.31.7.142]', 'interfaceTitle': 'Порт 26',
        'vlan': 2142, 'identifierList': [], 'macAddressList': [], 'dateFrom': '2021-06-28', 'dateTo': None, 'status': 0,
        'comment': '', 'accessCodeTitle': 'Ok', 'accessCode': 0, 'config': None, 'state': 1, 'cid': 20566, 'scid': 0,
        'typeId': 7, 'uname': '', 'passw': '', 'did': 230, 'ifaceId': 26, 'ipResId': 187, 'ipResSubsriptionId': 27346,
        'addrFrom': 'CmuOGg==', 'addrTo': None, 'sessCntLimit': 2, 'devState': 1, 'devOpts': [17, 18, 34], 'coid': 0}
        """
        params = {'method': 'inetServList',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'contractId': self.cid
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.modules.inet.api/1/InetServService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return")
        except:
            value = None
        return value[-1]

    def InetDeviceService(self):
        """
        {'id': 230, 'title': 'ELTEX_MES1124MB: [172.31.7.142]', 'entitySpecId': 1, 'entityAttributes': {},
        'entityId': 249, 'entityTitle': 'ELTEX_MES1124MB: [172.31.7.142] ()', 'deviceTypeId': 16,
        'host': '172.31.7.142', 'deviceGroupIds': [], 'username': '', 'password': '',
        'secret': '', 'config': '', 'comment': 'Ирчи Казака - Октябрьская (ГОРОТДЕЛ)', 'parentId': 124,
        'children': None, 'uptime': '', 'uptimeTime': None, 'dateFrom': None, 'dateTo': None,
        'orderManagerDisabled': False, 'invDeviceId': 249, 'invDeviceTypeId': 16,
        'invTitle': 'ELTEX_MES1124MB: [172.31.7.142]', 'invIdentifier': '', 'invHost': '172.31.7.142',
        'invConfig': '', 'invDeviceGroupIds': [], 'ident': ''}
        """
        params = {'method': 'inetDeviceGet',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  'params':
                      {
                          'id': self.inetServGet().get('did')
                      }
                  }
        url = self.url + 'ru.bitel.bgbilling.modules.inet.api/1/InetDeviceService'
        response = requests.post(url, json=params)
        json_data = json.loads(response.text)
        try:
            value = json_data.get("data").get("return")
        except:
            value = None
        return value

    def get_cid(self, contract):
        """
        Вызывает инет сервис по номеру договора
        по которому нужно извлечь id
        :return:
        """
        params = {
            "method": "inetSessionAliveList",
            "user":
                {"user": self._login,
                 "pswd": self._password},
            "params":
                {"contract": contract}
        }
        url = self.url + 'ru.bitel.bgbilling.modules.inet.api/1/InetSessionService'
        responce = requests.post(url, json=params)
        pack = json.loads(responce.text)
        unpack = pack.get('data').get('return').get('list')
        cid = unpack[0]['cid']
        return cid

    def inetServUpdate(self, uname, typeId, did, ifaceId, addrFrom, vlan):
        """
        :param
        dateFrom - Дата создания сервиса
        state - статус сервиса
        cid - Номер договора
        typeId - ид типа сервиса
        uname - Username сервиса (по необходимости)
        did - ид устройства
        ifaceId - номер порта
        addrFrom - статика ип. Перевести ип в 4 байта и шифровать в Base64
        sessCntLimit - кол-ство сессий
        """
        time = datetime.date.today()
        d = time.today()
        cid = self.get_cid(uname)
        ip = addrFrom
        ip = ip.split(".")
        ip = [int(i) for i in ip]
        ip = struct.pack("BBBB", ip[0], ip[1], ip[2], ip[3])
        ip = codecs.encode(ip, 'base64')
        ip = ip.replace(b'\n', b'')
        uname = 't' + uname
        params = {'method': 'inetServUpdate',
                  'user':
                      {
                          'user': self._login,
                          'pswd': self._password
                      },
                  "params":
                      {
                          "inetServ": {
                              "vlan": vlan,
                              "dateFrom": str(d),
                              "state": 1,
                              "cid": cid,
                              "typeId": int(typeId),
                              "uname": str(uname),
                              "did": did,
                              "ifaceId": ifaceId,
                              "addrFrom": ip.decode("utf-8"),
                              "sessCntLimit": 2
                          },
                          "optionList": [],
                          "generateLogin": 0,
                          "generatePassword": True,
                          "saWaitTimeout": "0"}
                  }
        url = self.url + 'ru.bitel.bgbilling.modules.inet.api/1/InetServService'
        result = requests.post(url, json=params)
        return result.status_code
