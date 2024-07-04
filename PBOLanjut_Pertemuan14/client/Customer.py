import requests
import json

class Customer:

    def __init__(self):
        self.__id=None
        self.__ktp=None
        self.__nama=None
        self.__jk=None
        self.__kota=None
        self.__url="http://localhost/webapi/customer_api.php"
               
    @property
    def id(self):
        return self.__id

    @property
    def ktp(self):
        return self.__ktp

    @ktp.setter
    def ktp(self, value):
        self.__ktp = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def kota(self):
        return self.__kota

    @kota.setter
    def kota(self, value):
        self.__kota = value
        
    def getByktp(self, ktp):
        url = self.__url+"?ktp="+ktp
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__ktp=item["ktp"]
            self.__nama=item["nama"]
            self.__jk=item["jk"]
            self.__kota=item["kota"]
        return data
               

    def simpan(self):
        payload = {
            "ktp":self.__ktp,
            "nama":self.__nama,
            "jk":self.__jk,
            "kota":self.__kota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateByktp(self, ktp):
        url = self.__url+"?ktp="+ktp
        payload = {
            "ktp":self.__ktp,
            "nama":self.__nama,
            "jk":self.__jk,
            "kota":self.__kota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteByktp(self,ktp):
        url = self.__url+"?ktp="+ktp
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    