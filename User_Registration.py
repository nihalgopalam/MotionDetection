import tkinter
import sqlite3
from tkinter import messagebox

counter = 0
def login():
    global counter
    db=sqlite3.connect('login.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
    db.execute("INSERT INTO login(username, password) VALUES('user', 'admin')")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?", (userinput.get(), pass_input.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login successful')
        counter=0
    else:
        messagebox.showinfo('info', 'login failed')
        counter+=1
        if counter>=3:
            exit()
    cursor.connection.commit()
    db.close()

main_window=tkinter.Tk()
main_window.title('Login Page')
main_window.geometry('400x300')
padd=20
main_window['padx']=padd
user_input=tkinter.StringVar()
pass_input=tkinter.StringVar()
info_label=tkinter.Label(main_window, text='Login Page')
info_label.grid(row=0, column=0)

info_user=tkinter.Label(main_window, text='Username')
info_user.grid(row=2, column=0)
userinput=tkinter.Entry(main_window, textvariable=user_input)
userinput.grid(row=2, column=1)

info_pass = tkinter.Label(main_window, text='Password')
info_pass.grid(row=3, column=0, pady=20)
passinput=tkinter.Entry(main_window, textvariable=pass_input, show="*")
passinput.grid(row=3, column=1)

login_btn=tkinter.Button(main_window, text='Login', command=login)
login_btn.grid(row=4,column=1)

main_window.mainloop()
