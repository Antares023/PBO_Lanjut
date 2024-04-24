import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from JadwalMK import JadwalMK

class FormJadwal:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("550x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode Mata Kuliah:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtKd_MK = Entry(mainFrame) 
        self.txtKd_MK.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKd_MK.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Mata Kuliah:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtMK = Entry(mainFrame) 
        self.txtMK.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Kelas:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = Entry(mainFrame) 
        self.txtKelas.grid(row=2, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Dosen:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtDosen = Entry(mainFrame) 
        self.txtDosen.grid(row=3, column=1, padx=5, pady=5)  
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idmhs', 'kd_mk', 'mk','kelas','dosen')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmhs', text='ID')
        self.tree.column('idmhs', width="30")
        self.tree.heading('kd_mk', text='Kd_MK')
        self.tree.column('kd_mk', width="80")
        self.tree.heading('mk', text='MK')
        self.tree.column('mk', width="120")
        self.tree.heading('kelas', text='Kelas')
        self.tree.column('kelas', width="60")
        self.tree.heading('dosen', text='Dosen')
        self.tree.column('dosen', width="200")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKd_MK.delete(0,END)
        self.txtKd_MK.insert(END,"")
        self.txtMK.delete(0,END)
        self.txtMK.insert(END,"")       
        self.txtKelas.delete(0,END)
        self.txtKelas.insert(END,"")       
        self.txtDosen.delete(0,END)
        self.txtDosen.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = JadwalMK()
        result = mhs.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        Kd_MK = self.txtKd_MK.get()
        mhs = JadwalMK()
        res = mhs.getBykd_mk(Kd_MK)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtMK.focus()
        return res
        
    def TampilkanData(self, event=None):
        Kd_MK = self.txtKd_MK.get()
        mhs = JadwalMK()
        res = mhs.getBykd_mk(Kd_MK)
        self.txtMK.delete(0,END)
        self.txtMK.insert(END,mhs.mk)
        Kelas = mhs.kelas
        if(Kelas=="P"):
            self.P.select()
        else:
            self.L.select()
        self.txtDosen.set(mhs.dosen)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        Kd_MK = self.txtKd_MK.get()
        MK = self.txtMK.get()
        Kelas = self.txtKelas.get()
        Dosen = self.txtDosen.get()
        
        mhs = JadwalMK()
        mhs.kd_mk = Kd_MK
        mhs.mk = MK
        mhs.kelas = Kelas
        mhs.dosen = Dosen
        if(self.ditemukan==True):
            res = mhs.updateBykd_mk(Kd_MK)
            ket = 'Diperbarui'
        else:
            res = mhs.simpan()
            ket = 'Disimpan'
            
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        Kd_MK = self.txtKd_MK.get()
        mhs = JadwalMK()
        mhs.Kd_MK = Kd_MK
        if(self.ditemukan==True):
            res = mhs.deleteBykd_mk(Kd_MK)
            rec = mhs.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormJadwal(root, "Aplikasi Data JadwalMK")
    root.mainloop() 