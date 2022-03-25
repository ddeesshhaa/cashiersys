import tkinter as tk
from tkinter import messagebox
import database
import session

def login(name, password,root,checker):
    x = name.get() 
    y = password.get()
    data = database.ReadData("SELECT * from users")
    for row in data:
        if row[1] == x and row[2] == y :
            root.destroy()
            session.start(row[0],row[1],row[3])
        else:
            name.set("")
            password.set("")
            checker.set("Wrong Data!!")


def register(name,password,root,checker):
    x = name.get().strip().lower()
    y = password.get()
    if x =="" or y=="":
        checker.set("All Feilds are Required")
    elif x == "admin" or x == "administrator":
        checker.set("Unallowed Username")
        name.set("")
        password.set("")
    else:
        data = database.ReadData("SELECT * from users")
        check = True
        priv = 0
        for row in data:
            if row[1] == x  :
                name.set("")
                password.set("")
                checker.set("Already Registered")
                check = False
        if check == True:
            users_id = len(data)+1
            order = "insert into users(user_id,user_name,user_pass,priv)values(?,?,?,?)"
            d = (users_id,x,y,priv)
            database.WriteData(order,d)
            checker.set("Successfully Registerd")
            
    


def choose():
    root = tk.Tk()
    root.title("Login")
    root.geometry("800x600")
    #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.resizable(False, False)
    root.configure(bg="#262626")
    rootFrame=tk.Frame(root,width = 600 , height = 500 ,bg='#262626')
    rootFrame.place(relx=0.5 , rely=0.5 , anchor = tk.CENTER)

    tk.Label(rootFrame, text="Log In", bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=250, y=20)
    tk.Label(rootFrame, text="Enter User Name", bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=50, y=100)
    name = tk.StringVar()
    tk.Entry(rootFrame, textvariable=name, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=300, y=100)

    tk.Label(rootFrame, text="Enter password", bg='#262626', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=50, y=150)
    password = tk.StringVar()
    tk.Entry(rootFrame, show="*",textvariable=password, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F2F2F2',
             font=('Arial', 16, 'bold')).place(x=300, y=150)
    
    checker = tk.StringVar()
    tk.Label(rootFrame,textvariable=checker,bg='#262626', fg='#F2F2F2',font=('Arial',16,'bold')).place(x=240,y=320)
             
    tk.Button(rootFrame, text="Register",
              command=lambda: register(name,password,root,checker), width=10, fg='#262626',
              font=('Arial', 16, 'bold')).place(x=100, y=250)
    tk.Button(rootFrame, text="Login",
              command=lambda: login(name,password,root,checker), width=10, fg='#262626',
              font=('Arial', 16, 'bold')).place(x=350, y=250)
    


    root.mainloop()