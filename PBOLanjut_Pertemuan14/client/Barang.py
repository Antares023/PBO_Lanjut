import requests
import json

class Barang:

    def __init__(self):
        self.__id=None
        self.__kode=None
        self.__nama_barang=None
        self.__harga=None
        self.__url="http://localhost/webapi/barang_api.php"
               
    @property
    def id(self):
        return self.__id

    @property
    def kode(self):
        return self.__kode

    @kode.setter
    def kode(self, value):
        self.__kode = value

    @property
    def nama_barang(self):
        return self.__nama_barang

    @nama_barang.setter
    def nama_barang(self, value):
        self.__nama_barang = value

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value
        
    def getBykode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__kode=item["kode"]
            self.__nama_barang=item["nama_barang"]
            self.__harga=item["harga"]
        return data
               

    def simpan(self):
        payload = {
            "kode":self.__kode,
            "nama_barang":self.__nama_barang,
            "harga":self.__harga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateBykode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {
            "kode":self.__kode,
            "nama_barang":self.__nama_barang,
            "harga":self.__harga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteBykode(self,kode):
        url = self.__url+"?kode="+kode
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    