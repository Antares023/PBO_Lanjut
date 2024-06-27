import tkinter as tk
import json

from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Matakuliah import *

class FrmMatakuliah:
    
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
        Label(mainFrame, text='kodemk:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='namamk:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='sks:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtkodemk = Entry(mainFrame) 
        self.txtkodemk.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkodemk.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtnamamk = Entry(mainFrame) 
        self.txtnamamk.grid(row=1, column=1, padx=5, pady=5) 

        self.txtsks = Entry(mainFrame) 
        self.txtsks.grid(row=2, column=1, padx=5, pady=5) 
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10)
        self.btnCari.grid(row=3, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kodemk', 'namamk','sks','prodi')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='kodemk')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='namamk')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='sks')
        self.tree.column('sks', width="30")
        
        # set tree position
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtkodemk.delete(0,END)
        self.txtkodemk.insert(END,"")
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,"")       
        self.txtsks.delete(0,END)
        self.txtsks.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = Matakuliah()
        result = mhs.getAllData()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["kodemk"], d["namamk"], d["sks"]))
    
    def onCari(self, event=None):
        kodemk = self.txtkodemk.get()
        mhs = Matakuliah()
        a = mhs.getBykodemk(kodemk)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
        
    def TampilkanData(self, event=None):
        kodemk = self.txtkodemk.get()
        mhs = Matakuliah()
        res = mhs.getBykodemk(kodemk)
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,mhs.namamk)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from textbox
        kodemk = self.txtkodemk.get()
        namamk = self.txtnamamk.get()
        sks = self.txtsks.get()
        
        # create new Object
        mhs = Matakuliah()
        
        # set the atribute
        mhs.kodemk = kodemk
        mhs.namamk = namamk
        mhs.sks = sks
        
        if(self.ditemukan==False):
            # save the record
            res = mhs.simpan()
        else:
            # update the record
            res = mhs.updateBykodemk(kodemk)
        
        print("Respons simpan/update:", res)

        if res:
            try:
                data = json.loads(res)
                status = data["status"]
                msg = data["message"]
                messagebox.showinfo("showinfo", status + ', ' + msg)
            except json.JSONDecodeError as e:
                messagebox.showerror("Error", f"Penguraian JSON gagal: {e}\nRespons: {res}")
        else:
            messagebox.showerror("Error", "Respons kosong diterima")

        self.onClear()

    def onDelete(self, event=None):
        kodemk = self.txtkodemk.get()
        mhs = Matakuliah()
        mhs.kodemk = kodemk
        if(self.ditemukan==True):
            res = mhs.deleteBykodemk(kodemk)
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
    aplikasi = FrmMatakuliah(root2, "Aplikasi Data Matakuliah Ilham (220511113)")
    root2.mainloop() 