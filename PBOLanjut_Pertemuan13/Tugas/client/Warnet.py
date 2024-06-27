import requests
import json

class sewa:

    def __init__(self):
        self.__id=None
        self.__idpc=None
        self.__user=None
        self.__tanggal=None
        self.__jam_mulai=None
        self.__jam_selesai=None
        self.__lama_waktu=None
        self.__tarif=None
        self.__total=None
        self.__status=None
        self.__url="http://localhost/webapi/warnet_api.php"
        
        
    @property
    def id(self):
        return self.__id

    @property
    def idpc(self):
        return self.__idpc

    @idpc.setter
    def idpc(self, value):
        self.__idpc = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value

    @property
    def jam_mulai(self):
        return self.__jam_mulai

    @jam_mulai.setter
    def jam_mulai(self, value):
        self.__jam_mulai = value
        
    @property
    def jam_selesai(self):
        return self.__jam_selesai

    @jam_selesai.setter
    def jam_selesai(self, value):
        self.__jam_selesai = value
        
    @property
    def lama_waktu(self):
        return self.__lama_waktu

    @lama_waktu.setter
    def lama_waktu(self, value):
        self.__lama_waktu = value
        
    @property
    def tarif(self):
        return self.__tarif

    @tarif.setter
    def tarif(self, value):
        self.__tarif = value
        
    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value
        
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def getByidpc(self, idpc):
        url = self.__url+"?idpc="+idpc
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__idpc=item["idpc"]
            self.__user=item["user"]
            self.__tanggal=item["tanggal"]
            self.__jam_mulai=item["jam_mulai"]
            self.__jam_selesai=item["jam_selesai"]
            self.__lama_waktu=item["lama_waktu"]
            self.__tarif=item["tarif"]
            self.__total=item["total"]
            self.__status=item["status"]
        return data

    def simpan(self):
        payload = {
            "idpc":self.__idpc,
            "user":self.__user,
            "tanggal":self.__tanggal,
            "jam_mulai":self.__jam_mulai,
            "jam_selesai":self.__jam_selesai,
            "lama_waktu":self.__lama_waktu,
            "tarif":self.__tarif,
            "total":self.__total,
            "status":self.__status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateByidpc(self, idpc):
        url = self.__url+"?idpc="+idpc
        payload = {
            "idpc":self.__idpc,
            "user":self.__user,
            "tanggal":self.__tanggal,
            "jam_mulai":self.__jam_mulai,
            "jam_selesai":self.__jam_selesai,
            "lama_waktu":self.__lama_waktu,
            "tarif":self.__tarif,
            "total":self.__total,
            "status":self.__status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteByidpc(self,idpc):
        url = self.__url+"?idpc="+idpc
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text