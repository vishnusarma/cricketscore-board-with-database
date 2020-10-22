from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)


def search():  #search function
    q2=q.get()
    query="select team1,team2,team1_score,team_2score,winners from cricket_scores where team1 like '%"+q2+"%' or team2 like '%"+q2+"%'"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)

def clear():  #clear function
    query1="select team1,team2,team1_score,team_2score,winners from cricket_scores"
    cursor.execute(query1)
    rows=cursor.fetchall()
    update(rows)

def getrow(event): #getting row
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])

def update_score(): #uppdating values in to database
    Team1=t1.get()
    Team2=t2.get()
    Team1score=t3.get()
    Team2score=t4.get()
    Winner=t5.get()
    if messagebox.askyesno("Confirm Please","Are You Sure Want to Update This Customer?"):
        query4="update cricket_scores set team1=%s,team2=%s,team1_score=%s,team_2score=%s,winners=%s"
        cursor.execute(query4,(Team1,Team2,Team1score,Team2score,Winners))
        con.commit()
        clear()
    else:
        return True



def add_score(): #adding new record to database
    Team1=t1.get()
    Team2=t2.get()
    Team1score=t3.get()
    Team2score=t4.get()
    Winner=t5.get()
    query3="insert into cricket_scores(team1,team2,team1_score,team_2score,winners) values (%s,%s,%s,%s,%s)"
    cursor.execute(query3,(Team1,Team2,Team1score,Team2score,Winner))
    con.commit()
    clear()


def delete_score(): #deleting data from database
    Team1=t1.get()
    if messagebox.askyesno("Confirm Delete?","Are you Sure Want to delete this customer?"):
        query2="delete from cricket_scores where id="+Team1
        cursor.execute(query2)
        con.commit()
        clear()
    else:
        return True

    
#connecting to database
con=mysql.connector.connect(host="localhost",user="root",passwd="V!$#nu@228",database="project3")
cursor=con.cursor()
    

root=Tk()
q=StringVar() #declaring textvariables
t1=StringVar()#declaring textvariables
t2=StringVar()#declaring textvariables
t3=StringVar()#declaring textvariables
t4=StringVar()#declaring textvariables
t5=StringVar()#declaring textvariables

#label frames for cricket scores,search box,and databox
wrapper1=LabelFrame(root,text="cricket scores")
wrapper2=LabelFrame(root,text="search")
wrapper3=LabelFrame(root,text="data")

wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper3.pack(fill="both",expand="yes",padx=20,pady=10)

#treeview
trv=ttk.Treeview(wrapper1,columns=(1,2,3,4,5),show="headings",height="6")
trv.pack()

#giving headings to it
trv.heading(1,text="Team1")
trv.heading(2,text="Team2")
trv.heading(3,text="Team1Score")
trv.heading(4,text="Team2Score")
trv.heading(5,text="Winner")

trv.bind('<Double 1>',getrow) #to get data automatically when we clicked on that row

sql="select team1,team2,team1_score,team_2score,winners from cricket_scores"
cursor.execute(sql)
rows=cursor.fetchall()
update(rows)

#searching
lbl=Label(wrapper2,text="Search")
lbl.pack(side=tk.LEFT,padx=10)
ent=Entry(wrapper2,textvariable=q)
ent.pack(side=tk.LEFT,padx=6)
btn=Button(wrapper2,text="search",command=search)
btn.pack(side=tk.LEFT,padx=6)
cbtn=Button(wrapper2,text="clear",command=clear)
cbtn.pack(side=tk.LEFT,padx=6)

#cricket data
lbl1=Label(wrapper3,text="Team1")
lbl1.grid(row=0,column=0,padx=2,pady=3)
ent1=Entry(wrapper3,textvariable=t1)
ent1.grid(row=0,column=1,padx=5,pady=3)

lbl2=Label(wrapper3,text="Team2")
lbl2.grid(row=1,column=0,padx=5,pady=3)
ent2=Entry(wrapper3,textvariable=t2)
ent2.grid(row=1,column=1,padx=5,pady=3)

lbl3=Label(wrapper3,text="Team1 Score")
lbl3.grid(row=2,column=0,padx=5,pady=3)
ent3=Entry(wrapper3,textvariable=t3)
ent3.grid(row=2,column=1,padx=5,pady=3)

lbl4=Label(wrapper3,text="Team2 Score")
lbl4.grid(row=3,column=0,padx=5,pady=3)
ent4=Entry(wrapper3,textvariable=t4)
ent4.grid(row=3,column=1,padx=5,pady=3)

lbl5=Label(wrapper3,text="Winner")
lbl5.grid(row=4,column=0,padx=5,pady=3)
ent5=Entry(wrapper3,textvariable=t5)
ent5.grid(row=4,column=1,padx=5,pady=3)

up_btn=Button(wrapper3,text="Update",command=update_score)
add_btn=Button(wrapper3,text="Add New",command=add_score)
delete_btn=Button(wrapper3,text="Delete",command=delete_score)

add_btn.grid(row=5,column=0,padx=5,pady=5)
up_btn.grid(row=5,column=1,padx=5,pady=5)
delete_btn.grid(row=5,column=2,padx=5,pady=5)

root.title("Cricket Portal")
root.geometry("800x700")
root.mainloop()