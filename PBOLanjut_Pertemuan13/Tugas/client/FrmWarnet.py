import tkinter as tk
import json
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from tkcalendar import DateEntry
from Warnet import sewa  # Assuming `sewa` is the correct class name from `Warnet` module

class FrmWarnet:

    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("850x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = False
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg="#316879")
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='Kode PC:', bg="#316879", fg="#f0f0f0").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtidpc = Entry(mainFrame) 
        self.txtidpc.grid(row=0, column=1, padx=5, pady=5) 
        self.txtidpc.bind("<Return>", self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='User:', bg="#316879", fg="#f0f0f0").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtuser = Entry(mainFrame) 
        self.txtuser.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Tanggal:', bg="#316879", fg="#f0f0f0").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txttanggal = DateEntry(mainFrame, date_pattern='yyyy-mm-dd') 
        self.txttanggal.grid(row=2, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jam Mulai:', bg="#316879", fg="#f0f0f0").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtjam_mulai = Entry(mainFrame) 
        self.txtjam_mulai.grid(row=3, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jam Selesai:', bg="#316879", fg="#f0f0f0").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtjam_selesai = Entry(mainFrame) 
        self.txtjam_selesai.grid(row=4, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Lama Waktu:', bg="#316879", fg="#f0f0f0").grid(row=1, column=4, sticky=W, padx=5, pady=5)
        self.txtlama_waktu = Entry(mainFrame) 
        self.txtlama_waktu.grid(row=1, column=5, padx=5, pady=5) 

        Label(mainFrame, text='Tarif:', bg="#316879", fg="#f0f0f0").grid(row=2, column=4, sticky=W, padx=5, pady=5)
        self.txttarif = Entry(mainFrame) 
        self.txttarif.grid(row=2, column=5, padx=5, pady=5) 

        Label(mainFrame, text='Total:', bg="#316879", fg="#f0f0f0").grid(row=3, column=4, sticky=W, padx=5, pady=5)
        self.txttotal = Entry(mainFrame) 
        self.txttotal.grid(row=3, column=5, padx=5, pady=5) 

        Label(mainFrame, text='Status:', bg="#316879", fg="#f0f0f0").grid(row=4, column=4, sticky=W, padx=5, pady=5)
        self.txtstatus = StringVar()
        self.Lunas = Radiobutton(mainFrame, text='Lunas', value='Lunas', variable=self.txtstatus, bg="#316879")
        self.Lunas.grid(row=4, column=5, padx=5, pady=5, sticky=W)
        self.Lunas.select() # set pilihan yg pertama
        self.Belum = Radiobutton(mainFrame, text='Belum', value='Belum', variable=self.txtstatus, bg="#316879")
        self.Belum.grid(row=4, column=6, padx=5, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='lightgreen')
        self.btnSimpan.grid(row=0, column=7, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='darkgrey')
        self.btnClear.grid(row=1, column=7, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='red')
        self.btnHapus.grid(row=2, column=7, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, bg='lightgrey')
        self.btnCari.grid(row=3, column=7, padx=5, pady=5)

        columns = ('id', 'idpc', 'user', 'tanggal', 'jam_mulai', 'jam_selesai', 'lama_waktu', 'tarif', 'total', 'status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', style="Custom.Treeview")
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use any theme, here we use "clam"
        self.style.configure("Custom.Treeview.Heading", background="#7fe7dc", foreground="black", font=('Helvetica', 10, 'bold'))
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)  # Adjust the width as needed
        self.tree.place(x=0, y=250)

    def onClear(self, event=None):
        self.txtidpc.delete(0, END)
        self.txtidpc.insert(END, "")
        self.txtuser.delete(0, END)
        self.txtuser.insert(END, "")       
        self.txttanggal.delete(0, END)
        self.txttanggal.insert(END, "") 
        self.txtjam_mulai.delete(0, END)
        self.txtjam_mulai.insert(END, "")       
        self.txtjam_selesai.delete(0, END)
        self.txtjam_selesai.insert(END, "")       
        self.txtlama_waktu.delete(0, END)
        self.txtlama_waktu.insert(END, "")       
        self.txttarif.delete(0, END)
        self.txttarif.insert(END, "")       
        self.txttotal.delete(0, END)
        self.txttotal.insert(END, "")           
        self.btnSimpan.config(text="Simpan")
        self.Lunas.select()
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        mhs = sewa()
        result = mhs.getAllData()
        if result:
            try:
                parsed_data = json.loads(result)
                for item in self.tree.get_children():
                    self.tree.delete(item)

                for i, d in enumerate(parsed_data):
                    self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["idpc"], d["user"], d["tanggal"], d["jam_mulai"], d["jam_selesai"], d["lama_waktu"], d["tarif"], d["total"], d["status"]))
            except json.JSONDecodeError as e:
                messagebox.showerror("Error", f"Error decoding JSON: {e}")
                print(f"Error decoding JSON: {e}\nResult: {result}")
        else:
            messagebox.showerror("Error", "No data received from getAllData()")

    def onCari(self, event=None):
        idpc = self.txtidpc.get()
        mhs = sewa()
        data = mhs.getByidpc(idpc)

        if data:
            if isinstance(data, list) and len(data) > 0:  # Check if data is a non-empty list
                self.TampilkanData(data[0])
                self.ditemukan = True
                messagebox.showinfo("Show Info", "Data Ditemukan")
            else:
                self.ditemukan = False
                messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")

    def TampilkanData(self, data):
        self.txtidpc.delete(0, END)
        self.txtidpc.insert(END, data['idpc'])
        self.txtuser.delete(0, END)
        self.txtuser.insert(END, data['user'])
        self.txttanggal.set_date(data['tanggal'])  # Use set_date() for DateEntry
        self.txtjam_mulai.delete(0, END)
        self.txtjam_mulai.insert(END, data['jam_mulai'])
        self.txtjam_selesai.delete(0, END)
        self.txtjam_selesai.insert(END, data['jam_selesai'])
        self.txtlama_waktu.delete(0, END)
        self.txtlama_waktu.insert(END, data['lama_waktu'])
        self.txttarif.delete(0, END)
        self.txttarif.insert(END, data['tarif'])
        self.txttotal.delete(0, END)
        self.txttotal.insert(END, data['total'])
        if data['status'] == 'Lunas':
            self.Lunas.select()
        else:
            self.Belum.select()
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        idpc = self.txtidpc.get()
        user = self.txtuser.get()
        tanggal = self.txttanggal.get_date() # Ambil tanggal dalam format yang sesuai
        jam_mulai = self.txtjam_mulai.get()
        jam_selesai = self.txtjam_selesai.get()
        lama_waktu = self.txtlama_waktu.get()
        tarif = self.txttarif.get()
        total = self.txttotal.get()
        status = self.txtstatus.get()

        mhs = sewa()
        mhs.idpc = idpc
        mhs.user = user
        mhs.tanggal = tanggal
        mhs.jam_mulai = jam_mulai
        mhs.jam_selesai = jam_selesai
        mhs.lama_waktu = lama_waktu
        mhs.tarif = tarif
        mhs.total = total
        mhs.status = status

        if self.ditemukan == False:
            res = mhs.simpan()
        else:
            res = mhs.updateByidpc(idpc)

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
        idpc = self.txtidpc.get()
        mhs = sewa()
        if self.ditemukan:
            mhs.deleteByidpc(idpc)
            messagebox.showinfo("showinfo", "Data berhasil dihapus")
            self.onClear()
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root2 = Tk()
    aplikasi = FrmWarnet(root2, "Aplikasi Rental Warnet Ilham (220511113)")
    root2.mainloop()
