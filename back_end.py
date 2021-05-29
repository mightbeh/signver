#SSIM
from skimage.metrics import structural_similarity
import cv2
from tkinter import messagebox
import tkinter as tk
import sqlite3
from PIL import Image
from io import BytesIO
import numpy as np
global conn,curs
conn=sqlite3.connect('image.db')
cursor=conn.cursor()

def disp_res(ssim):
    if ssim>=0.95:
        messagebox.showinfo("Match",message = "The sample(s) maatch "+str(ssim))
    else:messagebox.showinfo("Not Match",message = "The sample(s) doesnt maatch "+str(ssim))

def read_imgQ(imageA,imageB):
    if check_size:
        ssim = compute_ssim(imageA,imageB)
        disp_res(ssim)
    else:
        tk.messagebox.showerror("Error",message = "The File Sizes are Different, try using same file size.")
        
def read_imgD(name, img):
    m=cursor.execute("""select * from emp where name = ?""",(name,))
    for l in m:
        rec_data=l[1]
        if(len(rec_data)!=0):
            imgB = cv2.imdecode(np.frombuffer(rec_data, np.uint8), -1)
            imgA = cv2.imread(img)
            read_imgQ(imgB,imgA)
            return
    tk.messagebox.showerror("Error",message = "The file Does not Exist")
    

def compute_ssim(imgA,imgB):
    grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print(diff)
    return score

def check_size(imgA,imgB):
    h1, w1, _ = imgA.shape
    h2, w2, _ = imgB.shape
    return True if h1==h2 and w1==w2 else False

def save_in_db(data,name):
    m=cursor.execute("""select * from emp where name = ?""",(name,))
    for n in m:
        if(name == n[0] and data==n[1]):
            messagebox.showinfo("Error",message = "The file Exist")
            return
        elif(name ==n[0] and data !=n[1]):
            messagebox.showinfo("Error",message = "Name Already Exist")
            return
    cursor.execute("""insert into emp(name,sign) values (?,?)""",(name,data))
    conn.commit()
    messagebox.showinfo("Done",message = "Entry Added")
