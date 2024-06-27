import requests
import json

class Matakuliah:

    def __init__(self):
        self.__id=None
        self.__kodemk=None
        self.__namamk=None
        self.__sks=None
        self.__url="http://localhost/webapi/matakuliah_api.php"
               
    @property
    def id(self):
        return self.__id

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def namamk(self):
        return self.__namamk

    @namamk.setter
    def namamk(self, value):
        self.__namamk = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value
        
    def getBykodemk(self, kodemk):
        url = self.__url+"?kodemk="+kodemk
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__kodemk=item["kodemk"]
            self.__namamk=item["namamk"]
            self.__sks=item["sks"]
        return data
               

    def simpan(self):
        payload = {
            "kodemk":self.__kodemk,
            "namamk":self.__namamk,
            "sks":self.__sks
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateBykodemk(self, kodemk):
        url = self.__url+"?kodemk="+kodemk
        payload = {
            "kodemk":self.__kodemk,
            "namamk":self.__namamk,
            "sks":self.__sks
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteBykodemk(self,kodemk):
        url = self.__url+"?kodemk="+kodemk
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    