from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Courier', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS records(
                    name text, 
                    email text, 
                    contact number, 
                    password text
                )
            ''')
con.commit()
cur.execute("Select * from records")
cur.fetchall()
def clear():
    register_name.delete(0,END)
    register_email.delete(0,END)
    register_mobile.delete(0,END)
    register_pwd.delete(0,END)
    pwd_again.delete(0,END)


def insert_record():
    global ws,register_name, register_email, register_mobile, register_pwd, pwd_again
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1
    if register_mobile.get() == "":
       warn = "Contact can't be empty"
    else:
        check_counter += 1
    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1
    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1
    if check_counter == 6:        
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO records VALUES (:name, :email, :contact, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'password': register_pwd.get()
            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
            ws.destroy()
            
        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)
        ws.destroy()
        
def signup():
    global register_name, register_email,register_mobile,register_pwd,pwd_again,ws

    ws = Tk()
    ws.title('Signup for the Library')
    ws.geometry('750x500')
    ws.maxsize(800,550)
    ws.config(bg='#0B5A81')

    
    right_frame = Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',
        relief=SOLID, 
        padx=10, 
        pady=10
        )

    Label(
        right_frame, 
        text="Enter Name", 
        bg='#CCCCCC',
        font=f
        ).grid(row=0, column=0, sticky=W, pady=10)

    Label(
        right_frame, 
        text="Enter Email", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, sticky=W, pady=10)

    Label(
        right_frame, 
        text="Contact Number", 
        bg='#CCCCCC',
        font=f
        ).grid(row=2, column=0, sticky=W, pady=10)

    
    Label(
        right_frame, 
        text="Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=5, column=0, sticky=W, pady=10)

    Label(
        right_frame, 
        text="Re-Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=6, column=0, sticky=W, pady=10)


    register_name = Entry(
        right_frame, 
        font=f
        )

    register_email = Entry(
        right_frame, 
        font=f
        )

    register_mobile = Entry(
        right_frame, 
        font=f
        )


    register_pwd = Entry(
        right_frame, 
        font=f,
        show='*'
    )
    pwd_again = Entry(
        right_frame, 
        font=f,
        show='*'
    )

    register_btn = Button(
        right_frame, 
        width=15, 
        text='Register', 
        font=f, 
        relief=SOLID,
        cursor='hand2',
        command=insert_record
    )

    clear_btn = Button(
        right_frame, 
        width=15, 
        text='Clear', 
        font=f, 
        relief=SOLID,
        cursor='hand2',
        command=clear
    )
    
    quit_btn = Button(
        right_frame, 
        width=15, 
        text='Exit', 
        font=f, 
        relief=SOLID,
        cursor='hand2',
        command=ws.destroy
    )

    # widgets placement

    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    pwd_again.grid(row=6, column=1, pady=10, padx=20)
    register_btn.grid(row=2, column=2, pady=10, padx=20)
    clear_btn.grid(row=4, column=2, pady=10, padx=20)
    quit_btn.grid(row=5, column=2, pady=10, padx=20)
    right_frame.place(x=30, y=40)


    # infinite loop
    ws.mainloop()