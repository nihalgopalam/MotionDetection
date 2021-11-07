from tkinter import Tk, Label, StringVar, Entry, Checkbutton, Button

root = Tk()
def getvals():
    print("Accepted")

#Size of Grid
root.geometry("500x300")
#Heading of Page
Label(root, text="User Registration", font="ar 15 bold").grid(row=0, column=3)
#Fields within the form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
UserID = Label(root, text="UserID")
Password = Label(root, text="Password")

#Sizing Field boxes
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
UserID.grid(row=4, column=2)
Password.grid(row=5, column=2)

#Assigning fields to string variable for storing Data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
UserIDvalue = StringVar
Passwordvalue = StringVar
#Creating entry fields
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
UserIDentry = Entry(root, textvariable = UserIDvalue)
Passwordentry = Entry(root, textvariable = Password)

#Sizing Entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
UserIDentry.grid(row=4, column=3)
Passwordentry.grid(row=5, column=3)
#Submit button
Button(text= "Submit", command= getvals).grid(row=7, column=5)

root.mainloop()