import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

password = ''
name = ''
lenght=''
def generate_password():
    global name 
    global lenght
    name = name_entry.get()
    length = int(length_entry.get())
    
    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return
    
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    global password
    password = ''.join(random.choice(characters) for _ in range(length))

    generated_box.insert(0,password)
    
    
def copy_to_clipboard():
    
    pyperclip.copy(password)
    
    messagebox.showinfo("Password Generated", f"Hi {name}, your password is:\n{password}\n\nIt has been copied to the clipboard.")
    


if __name__=="__main__":
    pass_app = tk.Tk()
    pass_app.title("Password Generator")
    pass_app.geometry("500x350")
    pass_app.config(bg="cyan")

    header = tk.Label(pass_app,text="Password Generator",font=('Arohani',25,'bold'),fg="black",bg='lightcyan')
    header.pack(ipadx=800,ipady=20)
    
    name_label = tk.Label(pass_app, text="Enter your name:",font=('arial',12),fg='black',bg='cyan')
    name_label.place(x=50,y=100)

    name_entry = tk.Entry(pass_app,font=("arial",12),width=20,fg="black")
    name_entry.place(x=180,y=101)
    name_entry.config(highlightthickness=2,highlightbackground='black')

    length_label = tk.Label(pass_app, text="Enter password length:",font=('arial',12),fg='black',bg='cyan')
    length_label.place(x=50,y=140)

    length_entry = tk.Entry(pass_app,font=("arial",12),width=16,fg="black")
    length_entry.place(x=220,y=141)
    length_entry.config(highlightthickness=2,highlightbackground='black')

    generated_label = tk.Label(pass_app,text="Genrated Password:",font=('arial',12),fg='black',bg='cyan')
    generated_label.place(x=50,y=180)

    generated_box = tk.Entry(pass_app,font=('arial',12),width=28,fg="black")
    generated_box.place(x=220,y=180)
    generated_box.config(highlightthickness=2,highlightbackground='black')

    
    generate_button = tk.Button(pass_app, text="Generate Password",font=('arial',10),fg='purple',bg='green2', command=generate_password)
    generate_button.place(x=100,y=250)

   
    copy_button = tk.Button(pass_app, text="Copy to Clipboard",fg='red', command=copy_to_clipboard,bg='yellow')
    copy_button.place(x=300,y=250)
    
    pass_app.mainloop()
