from tkinter import *
# from PIL import Image,ImageTk
import PIL.Image
import PIL.ImageTk
from login import *
from signup import *
#Designing Main Screen So, first of all, you have to design the main screen.
#two buttons Login and Register.
def main_screen():
    
    mainscreen = Tk()   # create a GUI window 
    mainscreen.geometry("650x350") # set the configuration of GUI window 
    mainscreen.title(" Login Page") # set the title of GUI window

    same=True
    n=0.25
    bgimage = open ("ready-back-school.jpg","rb")
    background_image =PIL.Image.open(bgimage)
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 

    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),PIL.Image.LANCZOS)
    img = PIL.ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(mainscreen)
    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(mainscreen,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to the Library", bg='black', fg='white', font=('Courier',20,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(mainscreen,text="LOGIN",bg='black', fg='white',relief=SOLID, command=login)
    btn1.place(relx=0.33,rely=0.30, relwidth=0.35,relheight=0.05)
    btn2 = Button(mainscreen,text="SIGNUP",bg='black', fg='white',relief=SOLID, command=signup)
    btn2.place(relx=0.33,rely=0.40, relwidth=0.35,relheight=0.05)
    btn3 = Button(mainscreen,text="EXIT",bg='black', fg='white',relief=SOLID, command=exit)
    btn3.place(relx=0.33,rely=0.50, relwidth=0.35,relheight=0.05)

    mainscreen.mainloop() # start the GUI

main_screen() # call the main_account_screen() function