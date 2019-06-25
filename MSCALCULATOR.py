from tkinter import *
import sqlite3
import  os
from tkinter import messagebox
import numpy as np

root=Tk()
root.geometry('1000x1000')
root["bg"]="SeaGreen1"
root.title("Post Adcampaign Market Share Calculator ")

orgname=StringVar()
c=StringVar()
MSValues=DoubleVar()
ad=StringVar()
adcduration=IntVar()
op=StringVar()

def ProjectDataBase():
    orgn=orgname.get()
    otype=c.get()
    msv=MSValues.get()
    medium=ad.get()
    duration=adcduration.get()
    optimisation=op.get()
    path='Z:\databases\database1.db'
    conn=sqlite3.connect(path)
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS OrgDetails(Name TEXT,type TEXT,Msvalues REAL,Medium TEXT,Time REAL,opti TEXT)')
    cursor.execute('INSERT INTO OrgDetails(Name,type,Msvalues,Medium,Time,opti)VALUES(?,?,?,?,?,?)',(orgn,otype,msv,medium,duration,optimisation,))
    conn.commit()
    messagebox.showinfo("save wizard","Values Saved Succesfully")

labeltitle=Label(root,text=" Market Share Calculator",width=20,font=("bold",20))
labeltitle.place(x=300,y=53)

labelname=Label(root,text="Organisation Name",width=20,font=("bold",10))
labelname.place(x=250,y=130)



labeltype=Label(root,text="Organisation Type",width=20,font=("bold",10))
labeltype.place(x=250,y=180)



labelmarketshare=Label(root,text="Current Market Share",width=20,font=("bold",10))
labelmarketshare.place(x=250,y=230)



labelmedium=Label(root,text="Advertisement Medium",width=20,font=("bold",10))
labelmedium.place(x=250,y=280)




labelduration=Label(root,text="Adcampaign Duration\n(In Months)",width=20,font=("bold",10))
labelduration.place(x=250,y=400)



labelopti=Label(root,text="Adcampaign Optimisation",width=20,font=("bold",10))
labelopti.place(x=250,y=450)
dv=DoubleVar()
finslv=DoubleVar()
tb1=DoubleVar()
tb2=DoubleVar()
ta1=DoubleVar()
ta2=DoubleVar()

def calculate():
    dv.set(entryms.get())
    oms=MSValues.get()/100
    omns=1-oms
    t=adcduration.get()
    statematrix=[[oms,omns]]
    t1=tb1.get()/100
    t2=tb2.get()/100
    t3=ta1.get()/100
    t4=ta2.get()/100
    
    statevector=np.array([oms,omns])
    transition=np.array([[t1,t2],[t3,t4]])
    states=[statevector]
    for i in range(t):
        statevector=np.dot(statevector,transition)
    states.append(statevector)

    for x in states:
        finslv.set(x)














entryname=Entry(root,width=30,textvar=orgname)
entryname.place(x=500,y=130)


list1=['Industry','Corporation','Agency','Firm','Banking and Finance','Sports','Goverment','E-Commerce'];
c=StringVar()
droplist1=OptionMenu(root,c,*list1)
droplist1.config(width=30)
c.set('select organisation type')
droplist1.place(x=500,y=180)

entryms=Entry(root,width=30,textvar=MSValues)
entryms.place(x=500,y=230)
entryms.bind(calculate)


medium1=Radiobutton(root,text='Print Advertising Newspapers Magazines',state=ACTIVE,value='Print Advertising Newspapers Magazines',tristatevalue=0,variable=ad).place(x=500,y=280)
medium2=Radiobutton(root,text='Billboards',state=ACTIVE,value='Billboards',tristatevalue=0,variable=ad).place(x=750,y=280)
medium3=Radiobutton(root,text='Radio Advertising',state=ACTIVE,value='Radio Advertising',tristatevalue=0,variable=ad).place(x=500,y=300)
medium4=Radiobutton(root,text='Television Advertising',state=ACTIVE,value='Television Advertising',tristatevalue=0,variable=ad).place(x=750,y=300)
medium5=Radiobutton(root,text='Covert Advertising',state=ACTIVE,value='Covert Advertising',tristatevalue=0,variable=ad).place(x=500,y=320)
medium6=Radiobutton(root,text='Surrogate Advertising',state=ACTIVE,value='Surrogate Advertising',tristatevalue=0,variable=ad).place(x=750,y=320)
medium7=Radiobutton(root,text='Public Service Advertising',state=ACTIVE,value='Public Service Advertising',tristatevalue=0,variable=ad).place(x=500,y=340)
medium8=Radiobutton(root,text='In-Store Advertising',state=ACTIVE,value='In-Store Advertising',tristatevalue=0,variable=ad).place(x=750,y=340)
medium9=Radiobutton(root,text='Digital/Online Advertising',state=ACTIVE,value='Digital/Online Advertising',tristatevalue=0,variable=ad).place(x=500,y=360)


entryduration=Entry(root,width=30,textvar=adcduration)
entryduration.place(x=500,y=400)



op1=Radiobutton(root,text='Minimum',state=ACTIVE,value='Minimum',tristatevalue=0,variable=op).place(x=500,y=450)
op2=Radiobutton(root,text='Moderate',state=ACTIVE,value='Moderate',tristatevalue=0,variable=op).place(x=600,y=450)
op3=Radiobutton(root,text='Maximum',state=ACTIVE,value='Maximum',tristatevalue=0,variable=op).place(x=700,y=450)










Button(root,text="Save",width=20,bg="orange",fg='white',command=ProjectDataBase).place(x=400,y=489)

labetite=Label(root,text="Transitionvalues",width=20,font=('bold',12))
labetite.place(x=40,y=660)

labelt1b=Label(root,text="% Of users kept\n kept using product",width=20,font=('bold',10))
labelt1b.place(x=10,y=490)

et1b=Entry(root,textvar=tb1)
et1b.place(x=200,y=490)

labelt2b=Label(root,text="% Of users switched tot\n other product",width=20,font=('bold',10))
labelt2b.place(x=10,y=530)

et2b=Entry(root,textvar=tb2)
et2b.place(x=200,y=530)

labelt1a=Label(root,text="% of non users switched\n to product",width=20,font=('bold',10))
labelt1a.place(x=10,y=570)

et1a=Entry(root,textvar=ta1)
et1a.place(x=200,y=570)

labelt2a=Label(root,text="% Of non users did not\nswitch to product",width=20,font=('bold',10))
labelt2a.place(x=10,y=610)

et2a=Entry(root,textvar=ta2)
et2a.place(x=200,y=610)

Button(root,text="Calculate",width=20,bg='blue',fg='white',command=calculate).place(x=300,y=660)
labelcentre=Label(root,width=20,text="FINAL RESULTS ARE",font=('bold',13))
labelcentre.place(x=500,y=560)

labelms1=Label(root,width=20,text="Market Share Values\nBefore Ad Campaign",font=('bold',12))
labelms1.place(x=500,y=600)


lsm1=Label(root,width=20,textvar=dv)
lsm1.place(x=500,y=660)

labelms2=Label(root,width=20,text="Markov Chain Values\n generated after ad campaign",font=('bold',12))
labelms2.place(x=800,y=600)

lsm2=Label(root,width=20,textvar=finslv)
lsm2.place(x=800,y=660)

mainloop()









