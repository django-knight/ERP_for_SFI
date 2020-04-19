from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import Calendar
from tkcalendar import DateEntry
import tkcalendar
import sqlite3

from PIL import Image,ImageTk


window = Tk()
window.geometry("500x600")
window.title("Registration Form")

imge = Image.open("C:/Users/momin/Desktop/SFI.png")
photo = ImageTk.PhotoImage(imge)



lab = Label(image = photo)
lab.pack()

fn = StringVar()
fn1 = StringVar()
dob = StringVar()
var = StringVar()
var_c1 = BooleanVar()
var_c2 = BooleanVar()
radio_var = StringVar()

def database():
    pass
    first = fn.get()
    last = fn1.get()
    DOB = cal.get()
    country = var.get()
    Manufacture =  var_c1.get()
    
    Trade = var_c2.get()
    prog_langs = []

    if (Manufacture): 
        prog_langs.append("Manufacturing")
    elif ("Manufacturing" in prog_langs):
        prog_langs.remove("Manufacturing")
    
    if (Trade): 
        prog_langs.append("Trading")
    elif ("Trading" in prog_langs):
        prog_langs.remove("Trading")
    Gender = radio_var.get()
    import json
    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Students (Name TEXT,Last TEXT, DOB TEXT, Country TEXT, Programming JSON, Gender TEXT)")
        cursor.execute("INSERT INTO Students (Name, Last, DOB, Country, Programming, Gender) VALUES(?,?,?,?,?,?)",(first,last,DOB,country,json.dumps(prog_langs),Gender))
        conn.commit()
    





def printt():
    first = fn.get()
    last = fn1.get()
    DOB = cal.get()
    country = var.get()
    python =  var_c1.get()
    
    JAVA = var_c2.get()
    prog_langs = []

    if (python): 
        prog_langs.append("Python")
    elif ("Python" in prog_langs):
        prog_langs.remove("Python")
    
    if (JAVA): 
        prog_langs.append("JAVA")
    elif ("JAVA" in prog_langs):
        prog_langs.remove("JAVA")
    Gender = radio_var.get()


    print(f"Your Fullname --> {first} {last}")
    print(f"Your Date of Birth --> {DOB}")
    print(f"Your Country --> {country}")
    print(f"Your Programming Languages --> {prog_langs}")
    print(f"Your Gender --> {Gender}\n")
    tkinter.messagebox.showinfo("Welcome","Signed Up Successfully")

def exit1(event=None):
    #exit()
    window.destroy()

def second_window():
    #implement it
    pass
    window1 = Tk()
    window1.geometry("500x600")
    window1.title("Registration Successful")
    label1 = Label(window1, text = "Registration Successful",font = ('ariel', 19,"bold"), relief = 'solid',width = 20)
    #label1.place(x = 90, y = 53)
    label1.pack(pady = 20)
    window1.mainloop()


menu = Menu(window)
window.config(menu = menu)

subm1 = Menu(menu)
menu.add_cascade(label='File', menu=subm1)
subm1.add_command(label="Exit",command = exit1)
subm1.add_command(label="Exit",command = exit1)

subm2 = Menu(menu)
menu.add_cascade(label='Option', menu=subm2)
subm2.add_command(label="Login",command = printt)



label1 = Label(window, text = "Registration Form",font = ('ariel', 19,"bold"), relief = 'solid',width = 20)
#label1.place(x = 90, y = 53)
label1.pack(pady = 20)

label2 = Label(window, text = "First Name:",font = ('ariel', 10,"bold"))
label2.place(x = 80, y = 230)

entry_1 = Entry(window, textvar = fn)
entry_1.place(x = 240,y = 232)

label3 = Label(window, text = "Last Name:",font = ('ariel', 10,"bold"))
label3.place(x = 80, y = 275)

entry_2 = Entry(window, textvar = fn1)
entry_2.place(x = 240,y = 277)

label4 = Label(window, text = "D.O.B:",font = ('ariel', 10,"bold"))
label4.place(x = 80, y = 320)

#entry_3 = Entry(window, textvar = dob)
#entry_3.place(x = 240,y = 322)


cal = DateEntry(window, width=12, background='darkblue',foreground='white', borderwidth=2)
#cal.pack(padx=10, pady=10)
cal.place(x=240, y = 322)


label5 = Label(window, text = "Country:",font = ('ariel', 10,"bold"))
label5.place(x = 80, y = 365)

list1 = ["Pakistan", 'India', "Nepal", "Sri Lanka",'Australia']
droplist = OptionMenu(window,var,*list1)
var.set("Select Country")
droplist.config(width = 15)
droplist.place(x=240 ,y=367)

label6 = Label(window, text = "Prog Lang",font = ('ariel', 10,"bold"))
label6.place(x = 80, y = 410)

c1 = Checkbutton(window, text = "Manufaturing", variable = var_c1)
c1.place(x= 240,y=412)
c2 = Checkbutton(window, text = "Trading", variable = var_c2)
c2.place(x= 340,y=412)

label7 = Label(window, text = "Gender:",font = ('ariel', 10,"bold"))
label7.place(x = 80, y = 455)

r1 = Radiobutton(window,text = "Male", variable = radio_var, value = "Male")
r1.place(x = 240, y= 457)

r2 = Radiobutton(window,text = "Female", variable = radio_var, value = "Female")
r2.place(x = 300, y= 457)


button1 = Button(window, text = "Login",width = 12,bg = 'brown',fg = 'white', command = database)
button1.place(x = 150, y= 500)                                          
    

button2 = Button(window, text = "Exit", width = 12,bg = 'brown',fg = 'white', command = exit1)
button2.place(x = 280, y= 500)
window.bind("<Return>", exit1)                                          

button3 = Button(window, text = "Second Window", width = 12,bg = 'brown',fg = 'white', command = second_window)
button3.place(x = 210, y= 560)                                          


#cal =Calendar(window,font="Arial 14", selectmode='day', cursor="hand1", year=2018, month=2, day=5)
#cal.pack(fill="both", expand=True)



window.mainloop()