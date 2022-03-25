import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import database
import datetime
import tables


day = datetime.datetime.today().strftime("%A")
today = datetime.date.today()
d1 = today.strftime("%Y/%m/%d")
cartItems = []
DataOfDB = ()
OrderOfDB = ""


def users(showFrame,root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=600, bg='#262626')
    showFrame.place(x=400, y=150)
    data = database.ReadData("SELECT * FROM users")
    tables.Table4(showFrame,len(data),len(data[0]),data)


def WriteToDb(name, quantity, price, success):
    global DataOfDB
    global OrderOfDB
    n = name.get().strip().capitalize()
    p = price.get()
    quan = quantity.get()
    if n == "" or p <= 0 or quan <= 0:
        success.set("Enter Valid Item!!!")
    else:
        data = database.ReadData("select * from items")
        id = len(data)+1
        for i in data:
            if i[0] == id:
                id += 1
        DataOfDB = (id, n, quan, p)
        OrderOfDB = "INSERT into items(item_id,name,quantity,price)values(?,?,?,?)"
        for i in data:
            if i[1] == n and i[3] == p:
                q = quan + i[2]
                DataOfDB = (q, i[0])
                OrderOfDB = "update items set quantity = ? where item_id = ?"

            elif i[1] == n and i[3] != p:
                n = n + "_ " + str(i[0])
                DataOfDB = (id, n, quan, p)

        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        name.set("")
        quantity.set("")
        price.set("")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")


def addItem(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#3F5955')
    showFrame.place(x=300, y=130)

    tk.Label(showFrame, text="Enter Item Name", bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=50, y=30)
    itemname = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=itemname, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=300, y=30)

    tk.Label(showFrame, text="Enter Quantity", bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=50, y=90)
    itemQuantity = tk.IntVar(showFrame)
    tk.Entry(showFrame, textvariable=itemQuantity, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=300, y=90)

    tk.Label(showFrame, text="Enter item price", bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=50, y=150)
    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=190, y=320)
    itemPrice = tk.IntVar(showFrame)
    tk.Entry(showFrame, textvariable=itemPrice, width=20, borderwidth=0, highlightthickness=0,  bg='#262626', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=300, y=150)

    tk.Button(showFrame, text="Add Item", command=lambda: [WriteToDb(itemname, itemQuantity, itemPrice, success)], width=20,fg='#D99A25',bg='#3F5955',
              font=('Arial', 16, 'bold')).place(x=180, y=250)


def view_items(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#3F5955')
    showFrame.place(x=300, y=130)
    showFrame.tkraise()
    total_rows = 0
    total_columns = 0
    data = database.ReadData("select * from items")
    try:
        total_rows = len(data)
        total_columns = len(data[0])
        tables.Table(showFrame, total_rows, total_columns, data)

    except IndexError:
        messagebox.showinfo("Error", "There's no data to show!")


def pay(data, realdata, showFrame):
    cash = 0
    for i in data:
        id = i[0]
        cash += i[4]
        x = (i[0], i[1], i[2], i[3], i[4], d1)
        for j in realdata:
            if i[0] == j[0]:
                realquan = j[2]-i[2]
        database.WriteData(
            "insert into transition(item_id,name,quantity,price,money,date)values(?,?,?,?,?,?)", x)
        database.WriteData(
            "update items set quantity = ? where item_id = ?", (realquan, id))
    cartItems.clear()
    showFrame.destroy()
    messagebox.showinfo("Paid Successfully",
                        "Thanks for using our services !!")


def viewCart(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#25403B')
    showFrame.place(x=300, y=130)
    showFrame1 = tk.Frame(root, width=1000, height=100, bg='#25403B')
    showFrame1.place(x=300, y=500)
    realdata = database.ReadData("SELECT * from items")
    try:
        total_rows = len(cartItems)
        total_columns = len(cartItems[0])
        tables.Table2(showFrame, total_rows, total_columns, cartItems)
        tk.Button(showFrame1, text="Check out", command=lambda: pay(cartItems, realdata, showFrame), width=10, height=3, bg='#25403B', fg='#D99A25',
                  font=('Arial', 16, 'bold')).place(x=800, y=0)

    except IndexError:
        messagebox.showerror("Error", "Cart is Empty!")


def watch(ca):
    data = database.ReadData("SELECT * FROM transition")
    t = []
    for i in data:
        if str(ca)[0:4] == str(i[5])[0:4] and str(ca)[5:7] == str(i[5])[5:7]  and str(ca)[8:10]== str(i[5])[8:10]:
            t += [(i)]
    root=tk.Tk()
    root.title(str(ca) + " Log")
    tables.Table3(root,len(t),5,t)


def trans(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#25403B')
    showFrame.place(x=300, y=130)
    cal = Calendar(showFrame,
                   font="Arial 14", selectmode='day',
                    year=int(today.strftime("%Y")), month=int(today.strftime("%m")), day=int(today.strftime("%d")))
    cal.place(x=250, y=70)
    tk.Label(showFrame, text="Pick A Date", bg='#25403B', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=360, y=30)
    tk.Button(showFrame, text="Show", width=18, bg='#25403B', fg='#D99A25',
              font=('Arial', 16, 'bold'), command=lambda: [
                  watch(cal.selection_get())]).place(x=300, y=350)


def cart(id, name, quantity, price, cost):
    global cartItems
    Item = (id, name, quantity, price, cost)
    cartItems += [(Item)]


def check_quan(value, quantity, state, showFrame, q):
    id = 0
    realquan = 0
    name = value.get()
    quan = quantity.get()
    data = database.ReadData("select * from items")

    for i in range(len(data)):
        if data[i][1] == name:
            realquan = data[i][2]
            id = i

    if realquan < quan:
        messagebox.showinfo("Failed", "No Enough Peices")
    elif realquan >= quan:
        realquan -= quan
        totalprice = data[id][3] * quan
        state.set("Added to cart")
        messagebox.showinfo("Success", "Added To Cart")
        value.set("")
        quantity.set("")
        state.set("")
        q.set(realquan)
        x = id+1
        cart(x, data[id][1], quan, data[id][3], totalprice)
        return realquan


def sell_items(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#3F5955')
    showFrame.place(x=300, y=130)

    def CurSelet(evt):
        x = L1.get(L1.curselection())
        var2.set(x)
        data = database.ReadData("select * from items")
        for i in data:
            if i[1] == x:
                item = i
                quant.set(item[2])

    tk.Label(showFrame, text="Choose Item", bg='#3F5955', fg='#D99A25',
             font=('Arial', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#3F5955', borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('Arial', 16, 'bold'))
    data = database.ReadData("select * from items")
    for i in range(len(data)):
        L1.insert(data[i][0], data[i][1])
        L1.place(x=30, y=i+80)
    L1.bind('<<ListboxSelect>>', CurSelet)
    var2 = tk.StringVar(showFrame)
    quant = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Available : ", bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=400, y=30)
    tk.Label(showFrame, textvariable=quant,  bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=520, y=30)
    tk.Label(showFrame, text="Enter Quantity",  bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=400, y=100)
    tk.Label(showFrame, text="Peice", bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=650, y=30)
    quan = tk.IntVar(showFrame)
    tk.Entry(showFrame, textvariable=quan, width=15, bg='#262626', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=600, y=100)
    state = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=state, bg='#3F5955', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=500, y=300)
    tk.Button(showFrame, text="Add to Cart", width=18, bg='#25403B', fg='#D99A25',
              font=('Arial', 16, 'bold'), command=lambda: [
                  check_quan(var2, quan, state, showFrame, quant)]).place(x=500, y=200)


def delete(var):
    ids = 0
    messagebox.showinfo("Done", "Deleted Successfuly")
    name = var.get()
    data = database.ReadData("select * from items")
    for i in range(len(data)):
        if data[i][1] == name:
            ids = data[i][0]
    database.DeleteData("delete from items where item_id = ?", (ids,))


def delete_item(showFrame,root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#25403B')
    showFrame.place(x=300, y=130)

    def CurSelet(evt):
        x = L1.get(L1.curselection())
        var2.set(x)

    var1 = tk.StringVar(showFrame)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#3F5955', borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('Arial', 16, 'bold'))
    data = database.ReadData("select * from items")
    for i in range(len(data)):
        L1.insert(data[i][0], data[i][1])
        L1.place(x=10, y=i+50)
    L1.bind('<<ListboxSelect>>', CurSelet)
    x = var1.get()
    var2 = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Choose Item", bg='#25403B', fg='#D99A25',
             font=('Arial', 20, 'bold')).place(x=75, y=0)
    tk.Button(showFrame, text="Delete Item", width=18,height=5, bg='#25403B', fg='#D99A25',
              font=('Arial', 16, 'bold'), command=lambda: [
                  delete(var2)]).place(x=400, y=200)


def start(id, username, priv):
    data = database.ReadData("SELECT * from store_data")
    root = tk.Tk()
    root.title(data[0][0] + " Store")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                       root.winfo_screenheight()))
    root.state('zoomed')
    root.configure(bg="#25403B")
    root.iconbitmap(r"title.ico")
    ud = tk.Frame(root,width=210,height=100,bg='#25403B')
    ud.place(x=20 , y = 20)
    tk.Label(ud, text="User : " + username, bg='#25403B', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=0, y=20)
    tk.Label(ud, text="Today is : " + day, bg='#25403B', fg='#D99A25',
             font=('Arial', 16, 'bold')).place(x=0, y=50)
    tabsFrame = tk.Frame(root, width=210, height=550, bg='#25403B')
    tabsFrame.place(x=20, y=130)
    showFrame = tk.Frame(root, width=1000, height=550, bg='#25403B')
    showFrame.place(x=300, y=130)
    if priv == 0:
        tk.Button(tabsFrame, text="Sell", command=lambda: sell_items(showFrame, root),  width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=1, row=0)
        tk.Button(tabsFrame, text="View", command=lambda: view_items(showFrame, root), width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=0, row=0)
        tk.Button(tabsFrame, text="Cart", command=lambda: viewCart(showFrame, root), width=6, height=5,  fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=0, row=1)
    else:
        tk.Button(tabsFrame, text="Add", command=lambda: addItem(showFrame, root), width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=0, row=0)
        tk.Button(tabsFrame, text="Sell", command=lambda: sell_items(showFrame, root),  width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=1, row=0)
        tk.Button(tabsFrame, text="View", command=lambda: view_items(showFrame, root), width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=0, row=1)
        tk.Button(tabsFrame, text="Log", command=lambda: trans(showFrame, root), width=6, height=5,  fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=1, row=1)
        tk.Button(tabsFrame, text="Delete",command=lambda: delete_item(showFrame,root), width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=0, row=2)
        tk.Button(tabsFrame, text="Users",command=lambda: users(showFrame,root), width=6, height=5, fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=1, row=2)
        tk.Button(tabsFrame, text="Cart", command=lambda: viewCart(showFrame, root), width=6, height=5,  fg='#D99A25',bg='#3F5955',
                  font=('Arial', 16, 'bold')).grid(column=0, row=3)

    root.mainloop()
