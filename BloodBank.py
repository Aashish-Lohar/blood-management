import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import Calendar, DateEntry

db=mysql.connector.connect(host="localhost",user="root",passwd="",database="bbms")
cursor=db.cursor()
root = Tk()
favicon=PhotoImage(file="icon.png")
root.iconphoto(False,favicon)
image1=PhotoImage(file="ok.png")
panel=Label(root,image=image1,bg="grey").place(x=0,y=0,relwidth=1,relheight=1)
root.title("BLOOD BANK")
root.geometry("1000x700")
root.configure(background='white')
l3=Label(root,text="BLOOD MANAGEMENT SYSTEM",relief=SOLID,bg='#E7E7E7',font = "Helvetica 20 bold").place(x=275,y=20,w=450,h=60)
l1=Label(root,text="Want to be the donor enter the details",bg='#C0C0C0',font="Helvetica 12").place(x=80,y=120,w=300,h=40)
b1=Button(root,text=" Donor Details ",command=lambda : donordetails()).place(x=185,y=170)
l0=Label(root,text="Update Blood Donation date",bg='#C0C0C0',font="Helvetica 12").place(x=80,y=220,w=300,h=40)
b0=Button(root,text=" Update ",command=lambda : updatedonordetails()).place(x=200,y=270)
l3=Label(root,text="Search for blood",bg='#C0C0C0',font="Helvetica 12").place(x=80,y=320,w=300,h=40)
b3=Button(root,text=" Search ",command=lambda : requestblood()).place(x=200,y=370)
b2=Button(root,text="       Exit       ",command=lambda : stop(root)).place(x=470,y=550)	
v = StringVar()

msg=Message(root,text="Our Blood management system is a platform  which connects directly needful person to the blood donor.This platform is very good for arranging blood in emergency it can save someone's precious life.",bg="#87CEEB",font="Bold 10",justify=CENTER).place(x=750,y=120,h=250,w=230)

def insertDonor(name,dob,gender,address,city,state,contactno,bloodgroup,lastdonation):
	insert = "INSERT INTO donors(name,dob,gender,address,city,state,contactno,bloodgroup,lastdonation) VALUES('"+name+"','"+dob+"','"+gender+"','"+address+"','"+city+"','"+state+"',"+"'"+contactno+"','"+bloodgroup+"','"+lastdonation+"')"

	messagebox.showinfo("Registration","Congrats you are saving many lives")
	try:
		cursor.execute(insert)
		db.commit()
	except:
		db.rollback()


# def insertBlood(bloodgroup,platelet,rbc):
# 	insert= "INSERT INTO blood(bloodgroup,platelet,rbc,date) VALUES('"+bloodgroup+"',"+"'"+platelet+"',"+"'"+rbc+"',"+"CURDATE())"
		
# 	try:
# 		cursor.execute(insert)
# 		db.commit()
# 	except:
# 		db.rollback()
		
def retrieve(bg,city,state):
	request="select * from donors where bloodgroup ='"+bg+"' and city = '"+city+"' and state = '"+state+"'"
	
	try:
		cursor.execute(request)		
		rows=cursor.fetchall()		
		db.commit()
		if(len(rows)):
			return rows
		else:
			return '0'

	except:
		
		db.rollback() 



def donordetails():
	global v
	root=Toplevel()
	favicon=PhotoImage(file="icon.png")
	root.iconphoto(False,favicon)
	img2 = PhotoImage(file="blood.png")	
	panel = Label(root, image = img2,bg="grey").place(x=0,y=0,width=1000,height=700)
	root.title("Donor Details")
	root.geometry("1000x700")
	root.configure(background ='grey')
	l0=Label(root,text="PROUD TO BE A BLOOD DONOR",relief=SOLID,bg='#BE1E2D',font = "Helvetica 20 bold").place(x=250,y=20,w=500,h=60)
	l1=Label(root,text="Name:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=100,w=100)
	l2=Label(root,text="DOB\n(yyyy-mm-dd):",bg='#C0C0C0',font="Helvetica 10").place(x=40,y=140,w=100)
	l3=Label(root,text="Gender:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=180,w=100)
	l4=Label(root,text="Address:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=220,w=100)
	l5=Label(root,text="City:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=260,w=100)
	l6=Label(root,text="State:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=300,w=100)
	l7=Label(root,text="Contact:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=340,w=100)
	l8=Label(root,text="Bloodgroup:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=380,w=100)
	l9=Label(root,text="Lastdonation\n(yyyy-mm-dd):",bg='#C0C0C0',font="Helvetica 10").place(x=40,y=420,w=100)

	e1=Entry(root)
	e1.place(x=160,y=100,w=200,h=25)
	e2=Entry(root)
	e2.place(x=160,y=140,w=200,h=25)
	v.set(0)
	r1=Radiobutton(root,text="Male",variable=v,value="Male").place(x=160,y=180)
	r2=Radiobutton(root,text="Female",variable=v,value="Female").place(x=217,y=180)
	r3=Radiobutton(root,text="Other",variable=v,value="Other").place(x=286,y=180)
	e4=Entry(root)
	e4.place(x=160,y=220,w=200,h=25)
	e5=Entry(root)
	e5.place(x=160,y=260,w=200,h=25)
	e6=Entry(root)
	e6.place(x=160,y=300,w=200,h=25)
	e7=Entry(root)
	e7.place(x=160,y=340,w=200,h=25)
	e9=Entry(root)
	e9.place(x=160,y=380,w=200,h=25)
	e10=Entry(root)
	e10.place(x=160,y=420,w=200,h=25)
	
	b2=Button(root,text="Back",command=lambda : stop(root)).place(x=160,y=480)
	
	b1=Button(root,text="Submit ",command=lambda : insertDonor(e1.get(),e2.get(),v.get(),e4.get(),e5.get(),e6.get(),e7.get(),e9.get(),e10.get())).place(x=40,y=480)
	

	msg=Message(root,text=" “A single pint can save three lives, a single gesture can create a million smiles”",bg="#87CEEB",font="Bold 10",justify=CENTER).place(x=800,y=100,h=100,w=160)
	msg1=Message(root,text=" “Blood Donation will cost you nothing, but it will save a life!”",bg="#FFDEAD",font="Bold 10",justify=CENTER).place(x=800,y=200,h=100,w=160)
	msg2=Message(root,text=" “We make a living by what we get. We make a life by what we give.” ",bg="#F0E68C",font="Bold 10",justify=CENTER).place(x=800,y=300,h=100,w=160)
	msg3=Message(root,text="“Never feel yourself weak, you have the ability to save a life. Just donate blood.”",bg="#F5F5DC",font="Bold 10",justify=CENTER).place(x=800,y=400,h=100,w=160)
	l10=Label(root,text="Important!!\nHumble Request to donor is that after fulfilling blood donation,donor must update 'last donation date' in 'Update Blood Donation Date' section,to avoid unwanted requests for blood donation. ",bg='#EEE8AA',font="Helvetica 10 bold",wraplength=500).place(x=225,y=600,w=550)

	root.mainloop()

def updatedonordetails():
	root=Toplevel()
	favicon=PhotoImage(file="icon.png")
	root.iconphoto(False,favicon)
	img = PhotoImage(file="donate.png")	
	panel2 = Label(root, image = img,bg="grey").place(x=0,y=0,width=1000,height=700)
	root.title("Update Blood Donation Date")
	root.geometry("1000x700")
	root.configure(background='grey')
	l0=Label(root,text="UPDATE BLOOD DONATION DATE",relief=SOLID,bg='#457984',font = "Helvetica 20 bold").place(x=250,y=20,w=500,h=50)
	l1=Label(root,text="Name:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=90,h=35,w=100)
	l2=Label(root,text="DOB\n(yyyy-mm-dd):",bg='#C0C0C0',font="Helvetica 10").place(x=40,y=140,h=35,w=100)
	l3=Label(root,text="Contact:",bg='#C0C0C0',font="Helvetica 12").place(x=40,y=190,h=35,w=100)
	l4=Label(root,text="Lastdonation\n(yyyy-mm-dd):",bg='#C0C0C0',font="Helvetica 10").place(x=40,y=240,h=35,w=100)
	
	e1=Entry(root)
	e1.place(x=160,y=90,w=200,h=30)	
	e2=Entry(root)
	e2.place(x=160,y=140,w=200,h=30)	
	e3=Entry(root)
	e3.place(x=160,y=190,w=200,h=30)	
	e4=Entry(root)
	e4.place(x=160,y=240,w=200,h=30)
	b=Button(root,text="  Update last  ",command=lambda : lastupdate(e1.get(),e2.get(),e3.get(),e4.get())).place(x=40,y=290)
	b2=Button(root,text="  Back  ",command=lambda : stop(root)).place(x=160,y=290)

	msg3=Message(root,text="“If you’re a blood donor, you’re a hero to someone, somewhere, who received your gracious gift of life.”\n\nEvery blood donor is a life saver.",bg="#ADD8E6",font="Bold 11",justify=CENTER).place(x=750,y=90,h=180,w=230)
	root.mainloop()

def lastupdate(name,dob,contactno,lastdonation):
	update = "UPDATE donors set lastdonation = '"+lastdonation+"' where name='"+name+"' and dob='"+dob+"' and contactno = '"+contactno+"'"
	messagebox.showinfo("Update","Last Donation Date Updated")

	try:
		cursor.execute(update)
		db.commit()
	except:
		db.rollback()
	
	
def grid1(bg,city,state):
	root=Toplevel()
	favicon=PhotoImage(file="icon.png")
	root.iconphoto(False,favicon)
	root.title("LIST OF MATCHING DONORS")
	root.geometry("600x500")
	root.configure(background='grey')
	rows=retrieve(bg,city,state)
	x=0
	if rows!='0':
		for row in rows:
			l1=Label(root,text=("Name:"+row[0]),bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			# l2=Label(root,text=row[1],bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			# l3=Label(root,text=row[2],bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			# l4=Label(root,text=row[3],bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			# l5=Label(root,text=row[4],bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			# l6=Label(root,text=row[5],bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			l7=Label(root,text=("Contactno:"+row[6]),bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=6,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			# l8=Label(root,text=row[7],bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=7,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			l9=Label(root,text=("LastDonation: {}".format(row[8])),bg="#1EDEF2",font = "Verdana 10 bold").grid(row=x,column=8,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
			
			x=x+1
	else:
		l=Label(root,text="No Bloodgroup Found").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	root.mainloop()

def requestblood():
	root=Toplevel()
	favicon=PhotoImage(file="icon.png")
	root.iconphoto(False,favicon)
	img2 = PhotoImage(file="request.png")	
	panel = Label(root, image = img2,bg="grey").place(x=0,y=0,width=1000,height=700)
	root.title("Search For Blood")
	root.geometry("1000x700")
	root.configure(background='grey')
	l0=Label(root,text="SEARCH FOR DONOR",relief=SOLID,bg='#C0C0C0',font = "Helvetica 20 bold").place(x=325,y=20,w=350,h=60)
	l1=Label(root,text="Bloodgroup:",bg='#C0C0C0').place(x=50,y=100,w=150,h=30)
	l2=Label(root,text="City:",bg='#C0C0C0').place(x=50,y=150,w=150,h=30)
	l3=Label(root,text="State:",bg='#C0C0C0').place(x=50,y=200,w=150,h=30)
	# l5=Label(root,text="Important!\n\nPlease do not disturb donor\n if its last donation date\n was not 3months before.\nDonating blood is a noble\n act which saves many lives.\n On average, a personcan\n donate blood after every 3 months.",bg="pink",font="Bold 10").place(x=750,y=40,h=160,w=230)

	msg=Message(root,text="Important!\n\nPlease do not disturb donor if its last donation date was not 3months before.Donating blood is a noble act which saves many lives.On average, a person can donate blood after every 3 months.",bg="#ED1C24",font="Bold 10",justify=CENTER).place(x=750,y=100,h=160,w=230)

	e1=Entry(root)
	e1.place(x=230,y=100,w=150,h=30)
	e2=Entry(root)
	e2.place(x=230,y=150,w=150,h=30)
	e3=Entry(root)
	e3.place(x=230,y=200,w=150,h=30)
	b2=Button(root,text="  Back  ",command=lambda : stop(root)).place(x=230,y=250)
	b=Button(root,text="  Search  ",command=lambda : grid1(e1.get(),e2.get(),e3.get())).place(x=50,y=250)
	root.mainloop()


def stop(root):
	root.destroy()


root.mainloop()
