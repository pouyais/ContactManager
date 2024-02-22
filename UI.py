from tkinter import *
from ClassFile import *
from tkinter import messagebox

db = Database("D:/CloneRepositoryFromGithub/Contactmanagerforpythonclass/mydatabase.db")

# ===== Def =====
def insert():
    db.insert(ent_name.get(),ent_lname.get(),ent_city.get(),int(ent_tel.get()))
    lst_box.insert(END,db.show())
    clear()


def fetch():
    recordsfromlistbox = lst_box.get(lst_box.curselection()).split(",")
    ent_name.insert(0,recordsfromlistbox[1])
    ent_lname.insert(0,recordsfromlistbox[2])
    ent_city.insert(0,recordsfromlistbox[3])
    ent_tel.insert(0,recordsfromlistbox[4])
    lst_box.delete(lst_box.curselection())


def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
    ent_name.focus_set()


def exit():
    root.destroy()


def remove():
    someonefromedatabase = lst_box.get(lst_box.curselection()).split(",")
    index = someonefromedatabase[0]
    db.remove(index)
    messagebox.showinfo(message="Your objects has deleted",title="Infor from data base")
    lst_box.delete(lst_box.curselection())


def show():
    lst_box.insert(0,db.showinlistbox())


# ===== UI =====
root = Tk()
screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
cx = screen_x / 2 
cy = screen_y / 2
ww = 600
wh = 400
wx = int(cx - ww / 2)
wy = int(cy - wh / 2)
root.geometry(f"{ww}x{wh}+{wx}+{wy}")


# ===== Labels =====
lbl_name = Label(root,text="Name : ",font="Arial 12 bold")
lbl_name.place(x=10,y=10)

lbl_lastname = Label(root,text="Lastname : ",font="Arial 12 bold")
lbl_lastname.place(x=280,y=10)

lbl_city = Label(root,text="City : ",font="Arial 12 bold")
lbl_city.place(x=10,y=80)

lbl_tel = Label(root,text="Tel : ",font="Arial 12 bold")
lbl_tel.place(x=320,y=80)


# ===== Entries =====
ent_name = Entry(root,font="Arial 12 bold")
ent_name.place(x=80,y=10)

ent_lname = Entry(root,font="Arial 12 bold")
ent_lname.place(x=380,y=10)

ent_city = Entry(root,font="Arial 12 bold")
ent_city.place(x=80,y=80)

ent_tel = Entry(root,font="Arial 12 bold")
ent_tel.place(x=380,y=80)


# ===== ListBox =====
lst_box = Listbox(root,font="Arial 14 bold",width=25)
lst_box.place(x=10,y=150)


# ===== Buttons =====
btn_insert = Button(root,text="Insert",width=5,height=1,font="Arial 12 bold",command=insert)
btn_insert.place(x=350,y=160)

btn_Fetch = Button(root,text="Fentch",width=5,height=1,font="Arial 12 bold",command=fetch)
btn_Fetch.place(x=350,y=210)

btn_clear = Button(root,text="Clear",width=5,height=1,font="Arial 12 bold",command=clear)
btn_clear.place(x=350,y=260)

btn_Exit = Button(root,text="Exit",width=5,height=1,font="Arial 12 bold",command=exit)
btn_Exit.place(x=350,y=310)

btn_delete = Button(root,text="Delete",width=5,height=1,font="Arial 12 bold",command=remove)
btn_delete.place(x=450,y=160)

btn_show = Button(root,text="Show",width=5,height=1,font="Arial 12 bold",command=show)
btn_show.place(x=450,y=210)




root.mainloop()