from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("CRICKET PORTAL")
        self.root.geometry("1350x700+0+0")
        
        self.bg=ImageTk.PhotoImage(file="images/bg1.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        
        #register frame
        frame1=Frame(self.root,bg="red")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="WELCOME TO CRICKET PORTAL REGISTRATION",font=("times new roman",20,"bold"),bg="black",fg="red").place(x=20,y=30)
        #label and entry for first name
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        #label and entry for last name
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        #label and entry for contact number
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        #label and entry for email
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        #labe and combobox for security question
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("SELECT","What is your fisrst pet name","what is your best friend","what is your birth place","what is your favourite country")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0) #to set the default option in combobox
        #label for answer
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        #label and entry for password
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
        #label and entry for confirm password
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        #creating a check button for terms and conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms&Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="green",fg="black",font=("times new roman",12)).place(x=50,y=380)
        #creating an image as button
        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        #creating button for signin
        btn_login=Button(self.root,text="SIGN IN",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2",bg="green").place(x=700,y=600)
        #cursor=hand2 means to change the structure of cursor when we touched the button
    def login_window(self):
        self.root.destroy()
        import loginpage #importing whole program file from loginpage.py
        
    
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("ERROR","All Fields are Required",parent=self.root) 
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("ERROR","Password and Confirm Password must be same",parent=self.root)
        
        else:
            con=mysql.connector.connect(host="localhost",user="root",passwd="V!$#nu@228",database="project3")
            cursor=con.cursor()
            sql=("insert into user_credentials(FirstName,LastName,ContactNumber,Email,SecurityQuestion,Answer,password) values (%s,%s,%s,%s,%s,%s,%s)")
            val=[(self.txt_fname.get()),(self.txt_lname.get()),(self.txt_contact.get()),(self.txt_email.get()),(self.cmb_quest.get()),(self.txt_answer.get()),(self.txt_password.get())]
            cursor.execute(sql,val)
            con.commit()
            messagebox.showinfo("successfull","registration",parent=self.root)#connecting to database
                              
                              
                              
                              
                              
                              
                             
root=Tk()
obj=Register(root)
root.mainloop()
   
        
