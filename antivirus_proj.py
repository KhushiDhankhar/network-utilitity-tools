from tkinter import Tk,filedialog,messagebox
from tkinter import *
import subprocess
from tkinter.filedialog import askopenfilename
import os

def file_open():
    while True:
        Tk().withdraw()
        file_path=askopenfilename()
        if file_path:
            if scan_file(file_path):
                messagebox.showwarning("Virus Detected",f"virus found in file: {file_path}")
                c=messagebox.askyesno("Delete the virus file",f"Do you want to delete this file {file_path}")
                if c:
                    os.remove(file_path)
            else:
                messagebox.showinfo("No Virus Found",f"No Virus found in file: {file_path}")
            result=messagebox.askyesno("Continue Scanning?","Do you want to scan more file?")
            if not result:
                messagebox.showinfo("THANKYOU !!","SUCESSFULLY LOGGED OUT")
                break
        else:
            messagebox.showinfo("No Selection","No file selected")
            break

def scan_file(file_path):
    try:
        with open(file_path,"rb") as f:
            file_content=f.read()
            virus_signature=rb"X50!P%@AP[4\PZX54(P^)7CC)7}$ESPRIT-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
            if virus_signature in file_content:
                return True
            return False
    except Exception as e:
        messagebox.showerror("ERROR",f"Error in scanning file {file_path}:{e}")

file_open()
                              
