import tkinter as tk
from functools import partial
import os
import mysqlpswd
import EzhilGUI2 


def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	user = username.get()
	pwd = password.get()
	users = mysqlpswd.getuserids()
	if (user,pwd) in users:
		EzhilGUI2.temp()
		
		starter()

def adduser():
	username = newusername.get()
	password = newpassword.get()
	mysqlpswd.insertvalues(username,password)

def deleteuser():
	todelete = username.get()
	todeletepwd = password.get()
	users = mysqlpswd.getuserids()
	if (todelete,todeletepwd) in users:

		mysqlpswd.deleteuserids(todelete)

def create_window():
	window = tk.Toplevel(master)
	window.geometry('270x300')  
	window.title('ADD USER')
	master['bg'] = '#ffe277'
	window['bg'] = '#ffe277'

	#username label and text entry box
	newusernameLabel = tk.Label(window, text="User Name",bg='#36b5b0',height=2,width=20,).place(x=60,y=6)
	
	newusernameEntry = tk.Entry(window, textvariable=newusername).place(x=70,y=60) 

	#password label and password entry box
	newpasswordLabel = tk.Label(window,text="Password",bg='#36b5b0',height=2,width=20,).place(x=60,y=90) 
	newpasswordEntry = tk.Entry(window, textvariable=newpassword, show='*').place(x=70,y=145)  

	username = newusername.get()
	password = newpassword.get()

	#login button
	newuser = tk.Button(window, text="Add user", command=adduser,height=2,
        width=20,
        bg='#ffb367',
        relief='flat',
        anchor='center',
        font=buttonfont,).place(x=50,y=205)   
#window
master = tk.Tk()  

newusername = tk.StringVar()
  
newpassword = tk.StringVar()
master.geometry('270x300')  
master.title('LOGIN')
master['bg'] = '#ffe277'

buttonfont = ('Roboto', 10, 'bold')
#username label and text entry box
usernameLabel = tk.Label(master, text="User Name",bg='#36b5b0',height=2,width=20,).place(x=60,y=6)
username = tk.StringVar()
usernameEntry = tk.Entry(master, textvariable=username).place(x=70,y=60)  

#password label and password entry box
passwordLabel = tk.Label(master,text="Password",bg='#36b5b0',height=2,width=20,).place(x=60,y=90) 
password = tk.StringVar()
passwordEntry = tk.Entry(master, textvariable=password, show='*').place(x=70,y=145)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = tk.Button(master, text="Login", command=validateLogin,height=1,
        width=20,
        bg='#ffb367',
        relief='flat',
        anchor='center',
        font=buttonfont,).place(x=50,y=175)  
newuserbutton = tk.Button(master, text="Add user", command=create_window,height=1,
        width=20,
        bg='#36b5b0',
        relief='flat',
        anchor='center',
        font=buttonfont,).place(x=50,y=205)  
deleteuserbutton = tk.Button(master, text="Delete user", command=deleteuser,height=1,
        width=20,
        bg='#ffb367',
        relief='flat',
        anchor='center',
        font=buttonfont,).place(x=50,y=235) 
master.mainloop()

