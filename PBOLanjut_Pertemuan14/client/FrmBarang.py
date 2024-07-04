import tkinter as tk
import json

from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Barang import *

class FrmBarang:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg="#316879")
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode Barang:', bg="#316879", fg="#f0f0f0").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama Barang:', bg="#316879", fg="#f0f0f0").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Harga:', bg="#316879", fg="#f0f0f0").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtkode = Entry(mainFrame) 
        self.txtkode.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkode.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtnama_barang = Entry(mainFrame) 
        self.txtnama_barang.grid(row=1, column=1, padx=5, pady=5) 

        self.txtharga = Entry(mainFrame) 
        self.txtharga.grid(row=2, column=1, padx=5, pady=5) 
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='lightgreen')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='darkgrey')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='red')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, bg='lightgrey')
        self.btnCari.grid(row=3, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kode', 'nama_barang','harga')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', style="Custom.Treeview")
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use any theme, here we use "clam"
        self.style.configure("Custom.Treeview.Heading", background="#7fe7dc", foreground="black", font=('Helvetica', 10, 'bold'))

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kode', text='kode')
        self.tree.column('kode', width="60")
        self.tree.heading('nama_barang', text='nama_barang')
        self.tree.column('nama_barang', width="200")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="70")
        
        # set tree position
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtkode.delete(0,END)
        self.txtkode.insert(END,"")
        self.txtnama_barang.delete(0,END)
        self.txtnama_barang.insert(END,"")       
        self.txtharga.delete(0,END)
        self.txtharga.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = Barang()
        result = mhs.getAllData()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["kode"], d["nama_barang"], d["harga"]))
    
    def onCari(self, event=None):
        kode = self.txtkode.get()
        mhs = Barang()
        a = mhs.getBykode(kode)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
            messagebox.showinfo("showinfo", "Data Ditemukan")
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
        
    def TampilkanData(self, event=None):
        kode = self.txtkode.get()
        mhs = Barang()
        res = mhs.getBykode(kode)
        self.txtnama_barang.delete(0,END)
        self.txtnama_barang.insert(END,mhs.nama_barang)
        self.txtharga.delete(0,END)
        self.txtharga.insert(END,mhs.harga)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from textbox
        kode = self.txtkode.get()
        nama_barang = self.txtnama_barang.get()
        harga = self.txtharga.get()
        
        # create new Object
        mhs = Barang()
        
        # set the atribute
        mhs.kode = kode
        mhs.nama_barang = nama_barang
        mhs.harga = harga
        
        if(self.ditemukan==False):
            # save the record
            res = mhs.simpan()
        else:
            # update the record
            res = mhs.updateBykode(kode)
        
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
        kode = self.txtkode.get()
        mhs = Barang()
        mhs.kode = kode
        if(self.ditemukan==True):
            res = mhs.deleteBykode(kode)
            messagebox.showinfo("showinfo", "Data Berhasil Dihapus!")
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
    aplikasi = FrmBarang(root2, "Aplikasi Data Barang Ilham (220511113)")
    root2.mainloop() 