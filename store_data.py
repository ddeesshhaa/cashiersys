import tkinter as tk
from tkinter import messagebox
import database
import login

def Ownername(name, phone,address,root):
    x = name.get()  # get() to get variable value [mustafa]
    n = x.strip().capitalize()
    y = phone.get().strip()
    z = address.get().strip()
    data = (n, y, z)  # (id,owner_name,store_name) from database
    if n == "" or y== "" or z== "":
        messagebox.showerror("Error","All Feilds Are Requiered")
    else:
        order = "insert into store_data(store_name,phone,address) values(?,?,?)"
        database.WriteData(order,data)
        messagebox.showinfo("Success", "Admin username is admin\nAdmin password is admin")
        root.destroy()
        login.choose()

def start():
    root = tk.Tk()
    root.title("Store Data")
    #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(bg="#262626")
    rootFrame=tk.Frame(root,width = 600 , height = 500 ,bg='#262626')
    rootFrame.place(relx=0.5 , rely=0.5 , anchor = tk.CENTER)
    tk.Label(rootFrame, text="Please Enter Store Data",bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=180, y=20)
    tk.Label(rootFrame, text="Enter Store Name",bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=50, y=100)
    name = tk.StringVar()
    tk.Entry(rootFrame, textvariable=name, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F2F2F2',
             font=('Arial', 16, '')).place(x=300, y=100)

    tk.Label(rootFrame, text="Enter Phone",bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=50, y=150)
    phone = tk.StringVar()
    tk.Entry(rootFrame, textvariable=phone, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F2F2F2',
             font=('Arial', 16, '')).place(x=300, y=150)
             
    tk.Label(rootFrame, text="Enter Address",bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=50, y=200)
    address = tk.StringVar()
    tk.Entry(rootFrame, textvariable=address, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F2F2F2',
             font=('Arial', 16, '')).place(x=300, y=200)

    tk.Button(rootFrame, text="Submit",
              command=lambda: Ownername(name, phone,address,root), bg = '#595959', fg='#F2F2F2',
              font=('Arial', 16, 'bold')).place(x=250, y=270)
    root.mainloop()