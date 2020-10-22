#analog clock
from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from tkinter import ttk,messagebox
from datetime import*
import time
from math import*
import mysql.connector
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Cricket Time")
        self.root.geometry("1350x700")
        self.root.config(bg="#021e2f")
        
        #left side label
        left_lbl=Label(self.root,bg="red",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        
        #login frame
        login_frame=Frame(self.root,bg="black")
        login_frame.place(x=250,y=100,width=800,height=500)
        
        #title for frame
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="black",fg="yellow").place(x=250,y=50)
        
        #label  and entry for email
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",30,"bold"),bg="black",fg="yellow").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=190,width=350,height=35)
        
        #label and entry for password
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",30,"bold"),bg="black",fg="yellow").place(x=250,y=240)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)
        
        #button for registration and login
        btn_reg=Button(login_frame,text="Register New Account?",font=("times new roman",14),bg="black",fg="yellow",command=self.register_window,bd=0,cursor="hand2").place(x=250,y=320)
        btn_login=Button(login_frame,text="Login",font=("times new roman",20),bg="black",fg="yellow",cursor="hand2",command=self.login).place(x=250,y=350,width=180,height=40)

        self.lbl=Label(self.root,bg="white",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()
        
    def register_window(self):
        self.root.destroy()#closing the current window
        import registerpage #importing whole program from registerpage.py
        
    def show_data(self):
        self.root.destroy()#closing the current window
        import displaydata #importing whole program from displaydata.py
        
        
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_=="":
            messagebox.showerror("ERROR","EMAIL & PASSWORD are required",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",user="root",passwd="V!$#nu@228",database="project3")
            cursor=con.cursor()
            cursor.execute("select * from user_credentials where Email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
            row=cursor.fetchone()
            print(row) #connecting and fetching to database
        if row==None:
            messagebox.showerror("ERROR","Invalid Username & Password",parent=self.root)
        else:
            self.show_data()
        
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255)) #for clock in left side of login page
        draw=ImageDraw.Draw(clock)
        
        bg=Image.open("clock.png")#opening image
        bg=bg.resize((300,300),Image.ANTIALIAS)#antialias=resizing image without loosing its clarity
        clock.paste(bg,(50,50))#pasting
        
        
        
        #hour's line
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="red",width=4)#formula
        #minutes linewidth=3)
        draw.line((origin,200+60*sin(radians(min_)),200-60*cos(radians(hr))),fill="blue",width=3)
        #second's line
        draw.line((origin,200+70*sin(radians(sec_)),200-70*cos(radians(hr))),fill="green",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        
        clock.save("clock_new.png")
        
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        #working of clock
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
        
        
        
        
root=Tk()
obj=Login_window(root)
root.mainloop()