import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.linked_list = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


# Linked list
class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

    def insert_linked_list(node, key):
        if node.linked_list is None:
            node.linked_list = LinkedListNode(key)
        else:
            current = node.linked_list
            while current.next:
                current = current.next
            current.next = LinkedListNode(key)

    def print_linked_list(head):
        current = head
        while current:
            print(current.key, end="\n")
            current = current.next
        print()

    def store_linked_list(head):
        L = []
        current = head
        while current:
            L.append(current.key)
            current = current.next
        return L

    def search(head, user):
        if head is None:
            return None
        pos = 1
        curr = head
        while curr is not None:
            if curr.key[0] == user:
                return curr.key
            pos = pos + 1
            curr = curr.next
        return None

    def search_main(head, user):
        if head is None:
            return None
        pos = 1
        curr = head
        while curr is not None:
            if curr.key[4] == user:
                return curr.key
            pos = pos + 1
            curr = curr.next
        return None


# Insertion
root = Node("Spik and Span")
root.left = Node("Magenta")
root.right = Node("Turquoise")

with open("Magenta.csv", 'r') as magenta_csv:
    magenta_reader = csv.reader(magenta_csv)
    for row in magenta_reader:
        LinkedListNode.insert_linked_list(root.left, row)

with open("Turquoise.csv", 'r') as turquoise_csv:
    turquoise_reader = csv.reader(turquoise_csv)
    for row in turquoise_reader:
        LinkedListNode.insert_linked_list(root.right, row)
        
root.PrintTree()
Magenta = LinkedListNode.store_linked_list(root.left.linked_list)
Turquoise = LinkedListNode.store_linked_list(root.right.linked_list)


user = ''
code = ''


# Check
def check_adm():
    global user
    global code
    user_input = user.get()
    code_input = code.get()
    y = LinkedListNode.search(root.left.linked_list, user_input)
    z = LinkedListNode.search(root.right.linked_list, user_input)
    if (y is not None and user_input == y[0] and y[0] != '' and code_input == y[1] and y[8] == 'A') or (
            z is not None and user_input == z[0] and z[0] != '' and code_input == z[1] and z[8] == 'A'):
        return adm_Profile()
    else:
        return error()


def check_res():
    global user
    global code
    global y
    global z
    user_input = user.get()
    code_input = code.get()
    y = LinkedListNode.search(root.left.linked_list, user_input)
    z = LinkedListNode.search(root.right.linked_list, user_input)
    if (y is not None and user_input == y[0] and y[0] != '' and code_input == y[1]) or (
            z is not None and user_input == z[0] and z[0] != '' and code_input == z[1] and z[8] == 'R'):
        return res_Profile()
    else:
        return error()


def error():
    messagebox.showerror('Invalid Login', 'Username or Passsword is incorrect.\n Try Again')


# Home Page
def home_page():
    root = Tk()
    root.title("Apartment Home Page")
    root.geometry("925x500+400+200")
    root.resizable(False, False)

    image_path = PhotoImage(file="Apartment.png")
    bg_image = Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    text_label = Label(root, text='Welcome to Spik N Span', bg='white', font=('Georgie', 24))
    text_label.pack(pady=50)

    button1 = Button(width=15, text="ADMIN LOGIN", bg='white', border=0, font=('Georgie', 12), command=admin)
    button1.pack(pady=20)

    button2 = Button(width=15, text="RESIDENT LOGIN", bg='white', border=0, font=('Georgie', 12), command=resident)
    button2.pack(pady=20)

    button3 = Button(width=15, text="GUEST LOGIN", bg='white', border=0, font=('Georgie', 12),command=guest)
    button3.pack(pady=20)

    root.mainloop()


# Admin login
def admin():
    global user
    global code

    root = Toplevel()
    root.title("Admin Login")
    root.configure(bg='#fff')
    root.geometry("925x500+400+200")

    root.resizable(False, False)

    img = PhotoImage(file="logo edit.png")
    Label(root, image=img, bg='white').place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=50)

    heading = Label(frame, text='Admin Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI light ', 24, 'bold'))
    heading.place(x=65, y=10)

    u = Label(frame, text='Username:', fg='black', font=('Microsoft YaHei UI light', 11))
    u.place(x=30, y=80)

    username = StringVar()

    user = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                 textvariable=username)
    user.place(x=30, y=110)

    v = Label(frame, text='Password:', fg='black', font=('Microsoft YaHei UI light', 11))
    v.place(x=30, y=150)

    password = StringVar()

    code = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                 textvariable=password,show="*")
    code.place(x=30, y=180)
    Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=check_adm).place(x=35,
                                                                                                                 y=250)

    root.mainloop()


# Resident login
def resident():
    global user
    global code
    root = Toplevel()
    root.title("Resident Login")
    root.configure(bg='#fff')
    root.geometry("925x500+400+200")

    root.resizable(False, False)

    img = PhotoImage(file="logo edit.png")
    Label(root, image=img, bg='white').place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=50)

    heading = Label(frame, text='Resident Login', fg='#57a1f8', bg='white',
                    font=('Microsoft YaHei UI light ', 24, 'bold'))
    heading.place(x=65, y=10)

    u = Label(frame, text='Username:', fg='black', font=('Microsoft YaHei UI light', 11))
    u.place(x=30, y=80)

    username = StringVar()

    user = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                 textvariable=username)
    user.place(x=30, y=110)

    v = Label(frame, text='Password:', fg='black', font=('Microsoft YaHei UI light', 11))
    v.place(x=30, y=150)
    password = StringVar()
    code = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                 textvariable=password,show="*")
    code.place(x=30, y=180)
    Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=check_res).place(x=35,
                                                                                                                 y=250)
    root.mainloop()


# Resident Home Page
def res_Profile():
    root = Toplevel()
    global y
    global z
    root.title("Resident Profile")
    root.geometry("925x500+400+200")
    root.resizable(False, False)

    image_path = PhotoImage(file="Apartment.png")
    bg_image = Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    frame = Frame(root, width=725, height=450, bg="white")
    frame.place(x=100, y=25)
    heading = Label(frame, text='PROFILE', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI light ', 24, 'bold'))
    heading.place(x=60, y=25)

    img = PhotoImage(file="logo.png")
    Label(frame, image=img, bg='#fff').place(x=25, y=80)

    u = Label(frame, text='NAME:', width=14, bg='white', fg='black', font=('Microsoft YaHei UI light', 13))
    u.place(x=300, y=100)
    a = Label(frame, text=y[0] if z == None else z[0], width=20, bg='white', fg='black',
              font=('Microsoft YaHei UI light', 13))
    a.place(x=450, y=100)

    v = Label(frame, text='BLOCK NAME:', width=14, bg='white', fg='black', font=('Microsoft YaHei UI light', 13))
    v.place(x=300, y=140)
    b = Label(frame, text=y[3] if z == None else z[3], width=20, bg='white', fg='black',
              font=('Microsoft YaHei UI light', 13))
    b.place(x=450, y=140)

    w = Label(frame, text='FLAT NO:', width=14, bg='white', fg='black', font=('Microsoft YaHei UI light', 13))
    w.place(x=300, y=180)
    c = Label(frame, text=y[4] if z == None else z[4], width=20, bg='white', fg='black',
              font=('Microsoft YaHei UI light', 13))
    c.place(x=450, y=180)

    x = Label(frame, text='PHONE NO:', width=14, bg='white', fg='black', font=('Microsoft YaHei UI light', 13))
    x.place(x=300, y=220)
    d = Label(frame, text=y[5] if z == None else z[5], width=20, bg='white', fg='black',
              font=('Microsoft YaHei UI light', 13))
    d.place(x=450, y=220)

    r = Label(frame, text='Email ID:', width=14, bg='white', fg='black', font=('Microsoft YaHei UI light', 13))
    r.place(x=300, y=260)
    d = Label(frame, text=y[6] if z == None else z[6], width=20, bg='white', fg='black',
              font=('Microsoft YaHei UI light', 13))
    d.place(x=450, y=260)

    k = Label(frame, text='MAINTENANCE :', width=14, bg='white', fg='black', font=('Microsoft YaHei UI light', 13))
    k.place(x=300, y=300)
    f = Label(frame, text=y[7] if z == None else z[7], width=20, bg='white', fg='black',
              font=('Microsoft YaHei UI light', 13))
    f.place(x=450, y=300)

    root.mainloop()


# Admin Profile
def adm_Profile():
    root = Toplevel()
    root.geometry("925x500+400+200")
    root.title("Admin Home Page")
    root.resizable(False, False)
    bg_img = PhotoImage(file="Apartment.png")

    label1 = Label(root, image=bg_img)
    label2 = Label(root, text="Welcome Admin!", font=("Georgie", 24, 'bold'), bg='white')

    label1.pack()
    label2.place(x=150, y=230)

    frame1 = Frame(root, height=450, width=450, bg="light grey")
    frame1.place(x=500, y=80)

    button1 = Button(frame1, text="Add Resident", width=20, bg='white', border=0,
                     font=('Georgie', '12'),command =add_resident)
    button2 = Button(frame1, text="Remove Resident", width=20, bg='white', border=0,
                     font=('Georgie', '12'),command=rem_resident)
    button3 = Button(frame1, text="Show Residents", width=20, bg='white', border=0, font=('Georgie', '12'),
                     command=res_details)
    button4 = Button(frame1, text="Maintenance Status", width=20, bg='white', border=0, font=('Georgie', '12'),
                     command=main_details)
    button5 = Button(frame1, text="Edit Maintenance", width=20, bg='white', border=0, font=('Georgie', '12'),
                     command=edit_maint)

    button1.grid(row=1, column=0, pady=20, padx=20)
    button2.grid(row=2, column=0, pady=20)
    button3.grid(row=3, column=0, pady=20)
    button4.grid(row=4, column=0, pady=20)
    button5.grid(row=5, column=0, pady=20)

    root.mainloop()
    
#Add Resident
def add_resident():

    global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8

    root = Toplevel()
    root.geometry("925x500+400+200")
    root.title("Add Residents")
    root.resizable(False, False)

    image_path = PhotoImage(file="Apartment.png")
    img = Label(root, image=image_path)
    img.place(relheight=1, relwidth=1)
        
    frame = Frame(root, width=800, height=400, bg="white")
    frame.place(x=70, y=50)

    resiname = StringVar()
    flatno = StringVar()
    blockname = StringVar()
    username = StringVar()
    password = StringVar()
    phonenum = StringVar()
    email_id = StringVar()
    maintenance = StringVar()

    label=Label(frame, text="Add Residents",bg="white",fg="#57a1f8", font=("bold", 24)).place(x=300, y=40)
    
    label2=Label(frame, text="Name:", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=120)
    label3=Label(frame, text="Flat No:", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=170)
    label4=Label(frame, text="Block Name:", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=220)
    label5=Label(frame, text="User Name:", bg="white", font=("Microsoft YaHei UI light", 13)).place(x=100, y=270)
    label6=Label(frame, text="Password:", bg="white", font=("Microsoft YaHei UI light", 13),width =15).place(x=420, y=120)
    label7=Label(frame, text="Phone No:", bg="white", font=("Microsoft YaHei UI light", 13),width =12).place(x=420, y=170)
    label8=Label(frame, text="Email ID:", bg="white", font=("Microsoft YaHei UI light", 13),width =12).place(x=420, y=220)
    label9=Label(frame, text="Maintenance:", bg="white", font=("Microsoft YaHei UI light", 13),width =12).place(x=420, y=270)

    entry1 = Entry(frame, textvariable=resiname)
    entry1.place(x=250, y=120)
    entry2 = Entry(frame, textvariable=flatno)
    entry2.place(x=250, y=170)
    entry3 = Entry(frame, textvariable=blockname)
    entry3.place(x=250, y=220)
    entry4 = Entry(frame, textvariable=username)
    entry4.place(x=250, y=270)
    entry5 = Entry(frame, textvariable=password)
    entry5.place(x=550, y=120)
    entry6 = Entry(frame, textvariable=phonenum)
    entry6.place(x=550, y=170)
    entry7 = Entry(frame, textvariable=email_id)
    entry7.place(x=550, y=220)
    entry8 = Entry(frame, textvariable=maintenance)
    entry8.place(x=550, y=270)

    Button(frame, text="Submit",bg='#FF69B4', fg="white", font=("Microsoft YaHei UI light", 13, 'bold'), command=addlist).place(x=350, y=350)
    root.mainloop()

def addlist():
    global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8

    name = entry1.get()
    flat = entry2.get()
    block = entry3.get()
    username = entry4.get()
    password = entry5.get()
    phone = entry6.get()
    email = entry7.get()
    maintenance = entry8.get()

    k= LinkedListNode.search_main(root.left.linked_list,flat)
    b = LinkedListNode.search_main(root.right.linked_list,flat)
    if k and flat == k[4]:
        k[0] = username
        k[1] = password
        k[2] = name
        k[3] = block
        k[5] = phone
        k[6] = email
        k[7] = maintenance
        k[8] = 'R'
        print(k)

        with open('Magenta.csv', 'r') as add_csv:
            add_reader = csv.reader(add_csv)
            data = list(add_reader)
            for i in data:
                if i and flat == i[4]:
                    i[0],i[1],i[2],i[3],i[5],i[6],i[7] = username,password,name,block,phone,email,maintenance
        with open('Magenta.csv', 'w', newline='') as add_csv:
            add_writer = csv.writer(add_csv)
            add_writer.writerows(data)
            
    elif b and flat == b[4]:
        b[0] = username
        b[1] = password
        b[2] = name
        b[3] = block
        b[5] = phone
        b[6] = email
        b[7] = maintenance
        b[8] = 'R'
        print(b)

        with open('Turquoise.csv', 'r') as add_csv:
            add_reader = csv.reader(add_csv)
            data = list(add_reader)
            for i in data:
                if i and flat == i[4]:
                    i[0],i[1],i[2],i[3],i[5],i[6],i[7] = username,password,name,block,phone,email,maintenance
        with open('Turquoise.csv', 'w', newline='') as add_csv:
            add_writer = csv.writer(add_csv)
            add_writer.writerows(data)

    return messagebox.showinfo('Success', 'Resident added successfully!')

#Remove Resident
def rem_resident():

    global entry1

    root = Toplevel()
    root.title("Remove Resident")
    root.geometry("925x500+400+200")
    root.resizable(False, False)

    img_path = PhotoImage(file="Apartment.png")
    img = Label(root, image=img_path)
    img.place(relheight=1, relwidth=1)

    frame = Frame(root, width=725, height=450, bg="white")
    frame.place(x=100, y=25)
    heading = Label(frame, text='Remove Resident',bg='white', fg='#57a1f8',
                    font=('Microsoft YaHei UI light ', 24, 'bold'))
    heading.place(x=200, y=25)

    u = Label(frame, text='Flat No:', width=15, fg='black',font=('Microsoft YaHei UI light', 13))
    u.place(x=100, y=130)

    v = Label(frame, text='Block Name:', width=15, fg='black',font=('Microsoft YaHei UI light', 13))
    v.place(x=100, y=210)

    name1 = StringVar()
    entry1 = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                  textvariable=name1)
    entry1.place(x=300, y=130)

    del_res = StringVar()
    enter1 = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                  textvariable=del_res)
    enter1.place(x=300, y=210)

    but = Button(frame, text="SUBMIT", bg='#FF69B4', fg='white', font=('Microsoft YaHei UI light ', 14),
                 command=check_rem_resident)
    but.place(x=300, y=300)
    root.mainloop()

def check_rem_resident():
    global entry1
    user_input = entry1.get()
    w = LinkedListNode.search_main(root.left.linked_list, user_input)
    x = LinkedListNode.search_main(root.right.linked_list, user_input)
    if w and user_input == w[4]:
        w[0],w[1],w[2],w[5],w[6],w[7],w[8] = '','','','','','',''
        print(w)

        with open('Magenta.csv', 'r') as del_csv:
            del_reader = csv.reader(del_csv)
            data = list(del_reader)
            for i in data:
                if i and user_input == i[4]:
                    i[0],i[1],i[2],i[5],i[6],i[7],i[8] = '','','','','','',''
        with open('Magenta.csv', 'w', newline='') as del_csv:
            del_writer = csv.writer(del_csv)
            del_writer.writerows(data)

    elif x and user_input == x[4]:
        x[0],x[1],x[2],x[5],x[6],x[7],x[8] = '','','','','','',''
        print(x)
        
        with open('Turquoise.csv', 'r') as del_csv:
            del_reader = csv.reader(del_csv)
            data = list(del_reader)
            for i in data:
                if i and user_input == i[4]:
                    i[0],i[1],i[2],i[5],i[6],i[7],i[8] = '','','','','','',''
        with open('Turquoise.csv', 'w', newline='') as del_csv:
            del_writer = csv.writer(del_csv)
            del_writer.writerows(data)
    return messagebox.showinfo('Success', 'Resident removed successfully!')

#View Resident
def res_details():
    root = Toplevel()
    root.title("Resident details")
    root.geometry("925x500+400+200")

    root.resizable(False, False)

    frame1 = Frame(root, height=400, width=720,bg='white')
    frame1.place(x=100, y=50)

    img_path = PhotoImage(file="Apartment.png")
    label1 = Label(root, image=img_path)

    label2 = Label(frame1, text="RESIDENT DETAILS", fg='#57a1f8', bg='white',
                   font=('Microsoft YaHei UI light ', 24, 'bold'))

    # Labels placement
    label1.pack()
    label2.place(x=200, y=20)

    # Treeview initialisation
    treeview = ttk.Treeview(frame1, columns=['fl', 'name', 'num', 'mail'])
    treeview.column('#0', width=120, anchor='center', stretch=False)
    treeview.column('name', width=120, anchor='center', stretch=False)
    treeview.column('num', width=120, anchor='center', stretch=False)
    treeview.column('mail', width=170, anchor='center', stretch=False)
    treeview.column('fl', width=100, anchor='center', stretch=False)

    # Column Headers
    treeview.heading('#0', text="Block Name")
    treeview.heading('name', text="Name")
    treeview.heading('mail', text="Email ID")
    treeview.heading('num', text="Contact No")
    treeview.heading('fl', text="Flat No")

    # TreePlacement
    treeview.place(x=50, y=100)

    # Blocks
    treeview.insert('', '0', 'Block1', text="Magenta")
    treeview.insert('', '1', 'Block2', text="Turquoise")

    # Block1 insertion
    for i in Magenta:
        treeview.insert('Block1', 'end', values=[i[4], i[0], i[5], i[6]])

    # Block2 insertion
    for j in Turquoise:
        treeview.insert('Block2', 'end', values=[j[4], j[0], j[5], j[6]])

    scrollbar = ttk.Scrollbar(treeview, orient=VERTICAL, command=treeview.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    treeview.config(yscrollcommand=scrollbar.set)

    # Style
    style = ttk.Style(root)
    (style.theme_use("default"))

    # Overlay of Frame
    frame1.lift()

    root.mainloop()

#View Maintenance
def main_details():
    root = Toplevel()
    root.title("Maintenance")
    root.geometry("925x500+400+200")

    root.resizable(False, False)

    frame1 = Frame(root, height=400, width=720,bg='white')
    frame1.place(x=100, y=50)

    img_path = PhotoImage(file="Apartment.png")
    label1 = Label(root, image=img_path)

    label2 = Label(frame1, text="MAINTENANCE ", fg='#57a1f8', bg='white',
                   font=('Microsoft YaHei UI light ', 24, 'bold'))

    # Labels placement
    label1.pack()
    label2.place(x=210, y=20)

    # Treeview initialisation
    treeview = ttk.Treeview(frame1, columns=['name', 'fl', 'main'])
    treeview.column('#0', width=120, anchor='center', stretch=False)
    treeview.column('name', width=120, anchor='center', stretch=False)
    treeview.column('main', width=170, anchor='center', stretch=False)
    treeview.column('fl', width=100, anchor='center', stretch=False)

    # Column Headers
    treeview.heading('#0', text="Block Name")
    treeview.heading('name', text="Name")
    treeview.heading('main', text="Maintenance")
    treeview.heading('fl', text="Flat No")

    # TreePlacement
    treeview.place(x=100, y=100)

    # Blocks
    treeview.insert('', '0', 'Block1', text="Magenta")
    treeview.insert('', '1', 'Block2', text="Turquoise")
    # Block1 insertion
    for i in Magenta:
        treeview.insert('Block1', 'end', values=[i[0], i[4], i[7]])

    # Block2 insertion
    for j in Turquoise:
        treeview.insert('Block2', 'end', values=[j[0], j[4], j[7]])

    scrollbar = ttk.Scrollbar(treeview, orient=VERTICAL, command=treeview.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    treeview.config(yscrollcommand=scrollbar.set)

    # Style
    style = ttk.Style(root)
    (style.theme_use("default"))

    # Overlay of Frame
    frame1.lift()

    root.mainloop()

#Edit Maintenance
def edit_maint():
    global entry
    global enter
    root = Toplevel()
    root.title("Edit maintainance")
    root.geometry("925x500+400+200")
    root.resizable(False, False)

    img_path = PhotoImage(file="Apartment.png")
    img = Label(root, image=img_path)
    img.place(relheight=1, relwidth=1)

    frame = Frame(root, width=725, height=450, bg="white")
    frame.place(x=100, y=25)
    heading = Label(frame, text='EDIT MAINTAINANCE', fg='#57a1f8', bg='white',
                    font=('Microsoft YaHei UI light ', 24, 'bold'))
    heading.place(x=200, y=25)

    u = Label(frame, text='FLAT NO:', width=15, fg='black', font=('Microsoft YaHei UI light', 13))
    u.place(x=100, y=130)

    v = Label(frame, text='MAINTAINANCE:', width=15, fg='black', font=('Microsoft YaHei UI light', 13))
    v.place(x=100, y=210)

    name = StringVar()
    entry = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                  textvariable=name)
    entry.place(x=300, y=130)

    maint = StringVar()
    enter = Entry(frame, width=35, fg='black', border=2, bg='white', font=('Microsoft YaHei UI light', 11),
                  textvariable=maint)
    enter.place(x=300, y=210)

    but = Button(frame, text="SUBMIT", bg='#FF69B4', fg='white', font=('Microsoft YaHei UI light ', 14),
                 command=check_main)
    but.place(x=300, y=300)
    root.mainloop()


def check_main():
    global entry
    global enter
    user_input = entry.get()
    code_input = enter.get()
    w = LinkedListNode.search_main(root.left.linked_list, user_input)
    x = LinkedListNode.search_main(root.right.linked_list, user_input)
    if w and user_input == w[4]:
        w[7] = code_input
        print(w)
        with open('Magenta.csv', 'r') as maint_csv:
            maint_reader = csv.reader(maint_csv)
            data = list(maint_reader)
            for i in data:
                if i and user_input == i[4]:
                    i[7] = code_input
                     
        with open('Magenta.csv', 'w', newline='') as maint_csv:
            maint_writer = csv.writer(maint_csv)
            maint_writer.writerows(data)
       
    elif x and code_input == x[4]:
        x[7] = code_input
        
        
        with open('Turquoise.csv', 'r') as maint_csv:
            maint_reader = csv.reader(maint_csv)
            data = list(maint_reader)
            for i in data:
                if i and user_input == i[4]:
                    i[7] = code_input
        with open('Turquoise.csv', 'w', newline='') as maint_csv:
            maint_writer = csv.writer(maint_csv)
            maint_writer.writerows(data)
       
    messagebox.showinfo("showinfo","Maintenance Updated")
        

#Guest Home Page
def guest():
    root=Toplevel()
    root.title("Guest Home Page")
    root.geometry("925x500+400+200")
    root.resizable(False,False)

    image_path=PhotoImage(file="Apartment.png")
    img=Label(root,image=image_path)
    img.place(relheight=1,relwidth=1)

    frame=Frame(root,width=360,height=360,bg='white')
    frame.place(x=75,y=115)

    frames=Frame(root,width=360,height=360,bg='white')
    frames.place(x=500,y=115)

    img=PhotoImage(file="Contact us.png")
    width, height = 120,120
    img = img.subsample(int(img.width() // width), int(img.height() // height))
    Label(frame,image=img,bg='#fff').place(x=95,y=50)

    lab=Label(frame,text='For details contact:\n Tariq​ \n 9019901122 \n ​spiknspan@gmail.com​ \n Spik And Span \n Kalaivanar Street \n Ramnagar North Extn \n Madipakkam \n Chennai–600091',width=40,height=10)
    lab.place(x=40,y=170)

    lab1=Label(frames,text="VACANT HOUSES",font=('Microsoft YaHei UI light',13,'bold'),width=20,height=1,fg='#57a1f8',bg='white')
    lab1.place(x=60,y=40)

    label=Label(root,text="SPIK AND SPAN",font=('Microsoft YaHei UI light',13,'bold'),width=20,height=1,fg='#57a1f8',bg='white')
    label.place(x=350,y=15)

    labels=Label(root,text="GUEST LOGIN",font=('Microsoft YaHei UI light',13,'bold'),width=20,height=1,fg='#57a1f8',bg='white')
    labels.place(x=350,y=60)
    
# Treeview initialization
    treeview = ttk.Treeview(frames, columns=['fl'])
    treeview.column('#0', width=120, anchor='center', stretch=False)
    treeview.column('fl', width=120, anchor='center', stretch=False)

    # Column Headers
    treeview.heading('#0', text="Block name")
    treeview.heading('fl', text="Flat no")

    # TreePlacement
    treeview.place(x=55, y=90)

    # Blocks
    treeview.insert('', '0', 'Block1', text="Magenta (3 BHK)")
    treeview.insert('', '1', 'Block2', text="Turquoise(2 BHK)")


    #Block1 insertion
    for i in Magenta:
        if i[0]=='':
           treeview.insert('Block1','end',values=i[4])

    #Block2 insertion
    for j in Turquoise:
        if j[0]=='':
           treeview.insert('Block2','end',values=j[4])

    scrollbar = ttk.Scrollbar(frames, orient=VERTICAL, command=treeview.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
    treeview.config(yscrollcommand=scrollbar.set)

    # Style
    style = ttk.Style(root)
    style.theme_use("default")

    frames.lift()
    root.mainloop()     
          

home_page()
