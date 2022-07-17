from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBooks import *
from DeleteBooks import *
from ViewBooks import *
from IssueBooks import *
from ReturnBooks import *

password = input ("Enter the password for your database:")
mypass = password
mydatabase="Books"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


def logged():
    # Designing Window
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.maxsize(width=1000,height=1100)
    root.geometry("750x850")

    # Adding a background image
    same=True
    n=0.25

    background_image =Image.open("ready-back-school.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 

    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)
    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    #Adding Head Frame
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to the Library", bg='black', fg='white', font=('Courier',20,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # Adding Buttons
    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.05)


    btn2 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.05)

    btn3 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.05)

    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn4.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.05)

    btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
    btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.05)

    btn6 = Button(root,text="Exit Library",bg='black', fg='white', command = exit)
    btn6.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.05)
    root.mainloop()