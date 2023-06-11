from tkinter import *
from PIL import Image, ImageTk

#Create a Tkinter window
root = Tk()
root.geometry("900x650")

img1=ImageTk.PhotoImage(Image.open("king1.jpg"))
img2=ImageTk.PhotoImage(Image.open("king2.jpg"))
img3=ImageTk.PhotoImage(Image.open("king3.jpg"))
img4=ImageTk.PhotoImage(Image.open("king4.jpg"))
img5=ImageTk.PhotoImage(Image.open("king5.jpg"))
img6=ImageTk.PhotoImage(Image.open("king6.jpg"))
img7=ImageTk.PhotoImage(Image.open("king7.jpg"))
img8=ImageTk.PhotoImage(Image.open("king8.jpg"))
img9=ImageTk.PhotoImage(Image.open("king9.jpg"))
img10=ImageTk.PhotoImage(Image.open("king10.jpg"))


l=Label(root,font='bold')
l.pack()

x=11

def move():
    global x
    if x==11:
        x=1
    if x==1:
        l.config(image=img1) #Firtst pic will appear with this line
    elif x==2:
        l.config(image=img2)
    elif x==3:
        l.config(image=img3)
    elif x==4:
        l.config(image=img4)
    elif x==5:
        l.config(image=img5)
    elif x==6:
        l.config(image=img6) 
    elif x==7:
        l.config(image=img7)
    elif x==8:
        l.config(image=img8)    
    elif x==9:
        l.config(image=img9)    
    elif x==10:
        l.config(image=img10)    
            
        
    #increses count by one
    x+=1
    
    #call funtion for move an image
    root.after(2000,move)
    
 #call a function
move()

#provide gui surface    
root.mainloop()
   
