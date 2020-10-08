from tkinter import *

window = Tk()


def getvals():
    getname = namevalue.get()
    getphone = phonevalue.get()
    getgender = gendervalue.get()
    getemergency = emergencyvalue.get()
    getpaymentmode = payment_modevalue.get()
    getfoodservice = foodservicevalue.get()

    with open("1.txt", "a") as file:
        file.write(f"{getname}, {getphone}, {getgender}, {getemergency}, {getpaymentmode}, {getfoodservice}\n")


window.geometry("644x344")

Label(text="welcome to Manish Travels", font="comicsanms 13 bold").grid(row=0, column=3)

name = Label(window, text="Name")
phone = Label(window, text="Phone")
gender = Label(window, text="Gender")
emergency = Label(window, text="Emergency")
payment_mode = Label(window, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
payment_modevalue = StringVar()
foodservicevalue = IntVar()  # this is for the check box and check box return either 0 or 1

name_entry = Entry(window, textvariable=namevalue)
phone_entry = Entry(window, textvariable=phonevalue)
gender_entry = Entry(window, textvariable=gendervalue)
emergency_entry = Entry(window, textvariable=emergencyvalue)
payment_mode_entry = Entry(window, textvariable=payment_modevalue)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_mode_entry.grid(row=5, column=3)

# lets create a checkbox

foodservice = Checkbutton(window, text="want to prebook your meal?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

Button(window, text="Submit", command=getvals).grid(row=7, column=3)

window.mainloop()
