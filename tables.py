import tkinter as tk
class Table:
    def __init__(self, root, total_rows, total_columns, lst):
        ids = ("ID", "Item Name", "Quantity", "Price")
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#D99A25',borderwidth=1,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=30,bg='#3F5955', fg='#D99A25',borderwidth=1,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#D99A25',borderwidth=1,
                
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=30,bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                    
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 2:
                    if lst[i][2] == 0:
                        self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#D99A25',borderwidth=1,
                        
                                        font=('Arial', 16, ''))
                        self.e.grid(row=i+1, column=2)
                        self.e.insert(tk.END, lst[i][2])
                    else :
                        self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                        
                                        font=('Arial', 16, ''))
                        self.e.grid(row=i+1, column=2)
                        self.e.insert(tk.END, lst[i][2])


                else:
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                    
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])


class Table2:
    def __init__(self, root, total_rows, total_columns, lst):
        ids = ("ID", "Item Name", "Quantity", "Price", "Total Price")
        cash = 0
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        

        for i in range(total_rows):
            cash += lst[i][4]
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                else:
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])

            self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
            self.e.grid(row=total_rows+2, column=2)
            self.e.insert(tk.END, "Total Cash :")
            self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
            self.e.grid(row=total_rows+2, column=total_columns-1)
            self.e.insert(tk.END, str(cash)+" L.E")


class Table3:
    def __init__(self, root, total_rows, total_columns, lst):
        ids = ("ID", "Item Name", "Price", "Quantity", "Total Money")
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                else:
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])


class Table4:
    def __init__(self, root, total_rows, total_columns, lst):
        ids = ("ID", "Userame", "Password", "Privilege")
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#D99A25',highlightthickness=0,
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j ==3 :
                    if lst[i][3] == 0:
                        self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                        self.e.grid(row=i+1, column=j)
                        self.e.insert(tk.END, "USER")
                    else:
                        self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                        font=('Arial', 16, 'italic'))
                        self.e.grid(row=i+1, column=j)
                        self.e.insert(tk.END, "ADMIN")
                else:
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('Arial', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])