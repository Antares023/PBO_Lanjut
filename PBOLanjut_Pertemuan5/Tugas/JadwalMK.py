from db import DBConnection as mydb

class JadwalMK:

    def __init__(self):
        self.__id=None
        self.__kd_mk=None
        self.__mk=None
        self.__kelas=None
        self.__dosen=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def kd_mk(self):
        return self.__kd_mk

    @kd_mk.setter
    def kd_mk(self, value):
        self.__kd_mk = value

    @property
    def mk(self):
        return self.__mk

    @mk.setter
    def mk(self, value):
        self.__mk = value

    @property
    def kelas(self):
        return self.__kelas

    @kelas.setter
    def kelas(self, value):
        self.__kelas = value

    @property
    def dosen(self):
        return self.__dosen

    @dosen.setter
    def dosen(self, value):
        self.__dosen = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kd_mk, self.__mk, self.__kelas, self.__dosen)
        sql="INSERT INTO jadwal (kd_mk, mk, kelas, dosen) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kd_mk, self.__mk, self.__kelas, self.__dosen, id)
        sql="UPDATE jadwal SET kd_mk = %s, mk = %s, kelas=%s, dosen=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykd_mk(self, kd_mk):
        self.conn = mydb()
        val = (self.__mk, self.__kelas, self.__dosen, kd_mk)
        sql="UPDATE jadwal SET mk = %s, kelas=%s, dosen=%s WHERE kd_mk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM jadwal WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykd_mk(self, kd_mk):
        self.conn = mydb()
        sql="DELETE FROM jadwal WHERE kd_mk='" + str(kd_mk) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM jadwal WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kd_mk = self.result[1]
        self.__mk = self.result[2]
        self.__kelas = self.result[3]
        self.__dosen = self.result[4]
        self.conn.disconnect
        return self.result

    def getBykd_mk(self, kd_mk):
        a=str(kd_mk)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM jadwal WHERE kd_mk='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kd_mk = self.result[1]
            self.__mk = self.result[2]
            self.__kelas = self.result[3]
            self.__dosen = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kd_mk = ''
            self.__mk = ''
            self.__kelas = ''
            self.__dosen = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM jadwal"
        self.result = self.conn.findAll(sql)
        return self.result

# delete Data
A = JadwalMK()
B = A.getAllData()
print(B)