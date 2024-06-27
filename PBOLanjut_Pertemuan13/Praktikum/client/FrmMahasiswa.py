import tkinter as tk
import json

from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Mahasiswa import *

class FrmMahasiswa:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='NIM:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kode Prodi:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 
        
        # Radio Button
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
       
        # Combo Box
        self.txtKodeProdi = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtKodeProdi) 
        Cbo.grid(row=4, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        Cbo['values'] = ('TIF','IND','PET')
        Cbo.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'nim', 'nama','jk','prodi')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nim', text='NIM')
        self.tree.column('nim', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        self.tree.heading('prodi', text='Kode Prodi')
        self.tree.column('prodi', width="100")
        
        # set tree position
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.txtKodeProdi.set("")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = Mahasiswa()
        result = mhs.getAllData()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["nim"], d["nama"], d["jk"], d["prodi"]))
    
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        mhs = Mahasiswa()
        a = mhs.getByNIM(nim)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = Mahasiswa()
        res = mhs.getByNIM(nim)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,mhs.nama)
        jk = mhs.jk
        if(jk=="P"):
            self.P.select()
        else:
            self.L.select()
        self.txtKodeProdi.set(mhs.prodi)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from textbox
        nim = self.txtNIM.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        prodi = self.txtKodeProdi.get() 
        
        # create new Object
        mhs = Mahasiswa()
        
        # set the atribute
        mhs.nim = nim
        mhs.nama = nama
        mhs.jk = jk
        mhs.prodi = prodi
        
        if(self.ditemukan==False):
            # save the record
            res = mhs.simpan()
        else:
            # update the record
            res = mhs.updateByNIM(nim)
        
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        #clear the form input
        self.onClear()

    def onDelete(self, event=None):
        nim = self.txtNIM.get()
        mhs = Mahasiswa()
        mhs.nim = nim
        if(self.ditemukan==True):
            res = mhs.deleteByNIM(nim)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmMahasiswa(root2, "Aplikasi Data Mahasiswa")
    root2.mainloop() 