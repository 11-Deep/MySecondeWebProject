from tkinter import *        # it will import all fuction from tkinter module
from tkinter import Image,messagebox,ttk   #it will import class from tkinter module
from PIL import ImageTk
main=Tk()                       # it will create main or first windows
main.geometry ("500x500")      # it will size of th main windows
main.resizable (0,0)            # it will fix height and width of the main windows
main.title("HSMS-HUBNET")       # it will set title of main windows
main.config (background="lightgreen")  # it will set change background of main windows
l1=Label(main,text="User SignUp / SignIn From", font=("monotype corsiva",18,"bold"),bg="lightgreen") 
l1.pack(pady=10)
img=PhotoImage(file="C:\\User\\DELL\\Desktop\\Logo.png")
main.iconphoto(False,img)




main.mainloop()


