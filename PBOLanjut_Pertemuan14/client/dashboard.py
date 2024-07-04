import tkinter as tk
from tkinter import Menu, Label, Button
from FrmBarang import FrmBarang
from FrmCustomer import FrmCustomer

def new_window(title, _class):
    new = tk.Toplevel(root)
    new.title(title)
    _class(new, title)  # Pass the title to the class

def barang():
    new_window("Data Barang", FrmBarang)

def customer():
    new_window("Data Customer", FrmCustomer)

# root window app
root = tk.Tk()
root.title('Menu Demo')
root.geometry("550x300")

# membuat menu bar
menubar = Menu(root)
root.config(menu=menubar)

# membuat menu
file_menu = Menu(menubar)
data_menu = Menu(menubar)

# menambah menu item
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

data_menu.add_command(
    label='Data Barang', command=barang
)
data_menu.add_command(
    label='Data Customer', command=customer
)

# memasukan menu ke menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="Apps", menu=data_menu
)

# membuat label
label_text = "Selamat datang di Toko Ilham"
label = Label(root, text=label_text, font=("Helvetica", 16))
label.pack(pady=20)

# membuat button untuk membuka Data Barang
btn_barang = Button(root, text="Buka Data Barang", command=barang, bg='lightgreen')
btn_barang.pack(side=tk.TOP, pady=5)

# membuat button untuk membuka Data Customer
btn_customer = Button(root, text="Buka Data Customer", command=customer, bg='lightgreen')
btn_customer.pack(side=tk.TOP, pady=5)

# menutup aplikasi
btn_customer = Button(root, text="Tutup Aplikasi", command=root.destroy, bg='red')
btn_customer.pack(side=tk.TOP, pady=5)

# membuat label
label_text = "Nama : Muhammad Ilham Ramdhani"
label = Label(root, text=label_text, font=("Helvetica", 10))
label.pack(pady=5)

# membuat label
label_text = "NIM : 220511113"
label = Label(root, text=label_text, font=("Helvetica", 10))
label.pack(pady=5)

label_text = "Kelas : TI22C"
label = Label(root, text=label_text, font=("Helvetica", 10))
label.pack(pady=5)

root.mainloop()
