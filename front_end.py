import tkinter as tk
from tkinter import *
import filetype
import cv2
from back_end import read_imgQ, read_imgD, save_in_db
from tkinter import filedialog, messagebox
def DBCheck():
    def file3():
        global tes
        global data
        file3 = filedialog.askopenfilename(initialdir = "\\Desktop",
                                         title = "Select File for adding to Databse",
                                          filetype =(("jpg","*.jpg"),("All Files","*.*")))
        tes = str(file3)
        
        
    def tryp():
        x = compName.get()
        read_imgD(x, tes)
        
    def addEntry():
        with open(tes, 'rb') as f:
            data=f.read()
        x = compName.get()
        save_in_db(data, x)
            
    dbc = tk.Toplevel(app)
    dbc.title("Databse Verification")
    dbc.resizable(False, False)
    namelabel = Label(dbc, text = "Name:")
    namelabel.grid(column = 0, row = 0,sticky = 'E')
    compName = Entry(dbc, width = 20)
    compName.grid(column = 1, row = 0)
    select = tk.Button(dbc, text="Browse",command=file3,width = 20)
    select.grid(column = 1,row = 1)
    addEntry = tk.Button(dbc, text="Add Entry",command=addEntry)
    addEntry.grid(column = 0,row = 1)
    check = tk.Button(dbc, text="Verify from Datadase",command=tryp)
    check.grid(columnspan = 2)
    dbc.columnconfigure(0, pad=10)
    dbc.columnconfigure(1, pad=20)
    dbc.rowconfigure(0, pad=30)
    dbc.rowconfigure(1, pad=30)
    dbc.rowconfigure(2, pad=30)
    
def QCheck():
    
    def qc1():
        global file1
        file1 = filedialog.askopenfilename(initialdir = "\\Desktop",
                                          title = "Select File for Comparing",
                                          filetype =(("jpg","*.jpg"),("All Files","*.*")))
        
    def qc2():
        global file2
        file2 = filedialog.askopenfilename(initialdir = "\\Desktop",
                                          title = "Select File for Comparing",
                                          filetype =(("jpg","*.jpg"),("All Files","*.*")))
    def check():
        g1 = filetype.guess(file1)
        g2 = filetype.guess(file2)
        if g1!=g2:
            messagebox.showwarning("Warning!",message = "File Formats are different, Result might be affected.")
        else:
            f1=cv2.imread(file1)
            f2=cv2.imread(file2)
            read_imgQ(f1,f2) 
        
    qc = tk.Toplevel(app)
    qc.title("Quick Comparison")
    qc.resizable(False, False)
    select1 = tk.Button(qc, text="Select 1",command=qc1,width = 20,height = 3)
    select1.grid(column = 0,row = 0)
    select2 = tk.Button(qc, text="Select 2",command=qc2,width = 20,height = 3)
    select2.grid(column = 1,row = 0)
    check = tk.Button(qc, text="Verify Both",command=check,width = 40,height = 3)
    check.grid(columnspan = 2)
    qc.columnconfigure(0, pad=10)
    qc.columnconfigure(1, pad=20)
    qc.rowconfigure(0, pad=30)
    qc.rowconfigure(1, pad=30)


    
app = tk.Tk()
app.title("Signature Verification")
app.resizable(False, False)
DBCheck = tk.Button(app, text="Verify from Datadase",command=DBCheck, height = 7, width = 50)
DBCheck.grid(column = 0,row = 0)
QCheck = tk.Button(app, text="Quick Verification",command=QCheck,height = 7, width = 50)
QCheck.grid(column = 0,row = 1)
app.mainloop()
