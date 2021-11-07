from tkinter import Tk, Label, StringVar, Entry,  Button

root = Tk()
def getvals():
    print("Logged In!")

#Size of Grid
root.geometry("500x300")
#Heading of Page
Label(root, text="Login Page", font="ar 15 bold").grid(row=0, column=3)
#Fields within the form
UserID = Label(root, text="UserID")
Password = Label(root, text="Password")

#Sizing Field boxes
UserID.grid(row=4, column=2)
Password.grid(row=5, column=2)

#Assigning fields to string variable for storing Data
UserIDvalue = StringVar
Passwordvalue = StringVar
#Creating entry fields
UserIDentry = Entry(root, textvariable = UserIDvalue)
Passwordentry = Entry(root, textvariable = Password)

#Sizing Entry fields
UserIDentry.grid(row=4, column=3)
Passwordentry.grid(row=5, column=3)
#Submit button
Button(text= "Submit", command= getvals).grid(row=7, column=5)

root.mainloop()