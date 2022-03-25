import tkinter as tk
from tkinter import messagebox
import tables
import database
from pathlib import Path
import store_data
import login
import session

sizeofdb = Path('mangement.db').stat().st_size


if sizeofdb <= 0:
    database.SetTables()
    store_data.start()
    
else:
    x = database.ReadData("SELECT * FROM store_data")
    if len(x) == 0:
        store_data.start()
    else:
        login.choose()
        #session.start(1,"Admin",1)
    