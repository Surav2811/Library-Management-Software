from tkinter import *
from tkinter import messagebox
import sqlite3
from signup import *
from main import logged

f = ('Courier', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
            
def login_response():
    global email_tf, pwd_tf, login_btn, register_btn, quit_btn,ws
    login_btn.destroy()
    register_btn.destroy()
    quit_btn.destroy()
    
    try:
        con = sqlite3.connect('userdata.db')
        cursor = con.execute("SELECT * from records")
        for row in cursor:
           email_tf = row[0]
           pwd_tf = row[3]
    except Exception as ep:
        messagebox.showerror('', ep)
        
    check_counter=0

    while check_counter > 3:
        uname = email_tf.get()
        upwd = pwd_tf.get()
        if uname == "":
           warn = "Username can't be empty"
        else:
            check_counter += 1
        if upwd == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            if (uname == username and upwd == pwd):
                messagebox.showinfo('Login Status', 'Logged in Successfully!')
                ws.destroy()
                logged()
            else:
                messagebox.showerror('Login Status', 'invalid username or password')
        else:
            messagebox.showerror('There seems to be a problem', warn)
            ws.destroy()

def login():
    global email_tf, pwd_tf, login_btn, register_btn, quit_btn,ws

    ws = Tk()
    ws.title('Login to the Library')
    ws.geometry('780x290')
    ws.minsize(730,250)
    ws.maxsize(780,280)
    ws.config(bg='#0B5A81')
    # widgets
    left_frame = Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',   
        relief=SOLID, 
        padx=10, 
        pady=10
        )

    Label(
        left_frame, 
        text="Enter Email", 
        bg='#CCCCCC',
        font=f).grid(row=0, column=0, sticky=W, pady=10)

    Label(
        left_frame, 
        text="Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, pady=10)

    email_tf = Entry(
        left_frame, 
        font=f
        )
    pwd_tf = Entry(
        left_frame, 
        font=f,
        show='*'
        )
    login_btn = Button(
        left_frame, 
        width=15, 
        text='Login', 
        font=f, 
        relief=SOLID,
        cursor='hand2',
        command=login_response
        )
    quit_btn = Button(
        left_frame, 
        width=15, 
        text='Exit', 
        font=f, 
        relief=SOLID,
        cursor='hand2',
        command=ws.destroy    
        )
    register_btn = Button(
        left_frame, 
        width=15, 
        text='New? Sign Up', 
        font=f, 
        relief=SOLID,
        cursor='hand2',
        command=signup
        )

    # widgets placement
    email_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=0, column=2, pady=10, padx=20)
    quit_btn.grid(row=1, column=2, pady=10, padx=20)
    register_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.place(x=50, y=50)


    # infinite loop
    ws.mainloop()
