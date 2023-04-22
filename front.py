from tkinter import *
from tkinter import messagebox
import empDataBase


class Employee:

    def __init__(self, root):
        self.root = root
        self.root.title("employee DBMS")
        self.root.geometry("1350x750")
        self.root.config(bg="cadet blue")


        empID = StringVar()
        firstname = StringVar()
        lastname = StringVar()
        dob = StringVar()
        age = StringVar()
        gender = StringVar()
        address = StringVar()
        mobile = StringVar()

        # frames
        main_frame = Frame(self.root, bg="cadet blue")
        main_frame.grid()
        title_frame = Frame(main_frame, bd=2, padx=54, pady=8, bg="white", relief=RIDGE)
        title_frame.pack(side=TOP)
        self.title_lbl = Label(title_frame, font=("arial", 47, "bold"),
                               text="Employee database management system", bg="white")
        self.title_lbl.grid()
        btn_frame = Frame(main_frame, bd=2, width=1350, height=70, padx=18, pady=10, bg="white", relief=RIDGE)
        btn_frame.pack(side=BOTTOM)
        df = Frame(main_frame, bd=2, width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        df.pack(side=BOTTOM)
        df_left = LabelFrame(df, bd=1, width=1000, height=600, padx=20, pady=20, bg="white", relief=RIDGE,
                             font=("arial", 20, "bold"), text="Employee info")
        df_left.pack(side=LEFT)
        df_right = LabelFrame(df, bd=1, width=450, height=300, padx=31, pady=3, bg="white", relief=RIDGE,
                              font=("arial", 20, "bold"), text="Employee details")
        df_right.pack(side=RIGHT)

        # functions
        def exit_app():
            response = messagebox.askyesno("Employee DBMS", "confirm exit")
            if response != 0:
                root.destroy()

        def clear_data():
            self.empID_ent.delete(0, END)
            self.fname_ent.delete(0, END)
            self.lname_ent.delete(0, END)
            self.dob_ent.delete(0, END)
            self.age_ent.delete(0, END)
            self.gender_ent.delete(0, END)
            self.addr_ent.delete(0, END)
            self.mobile_ent.delete(0, END)

        def add_data():
            if len(empID.get()) != 0:
                empDataBase.add_emp_rec(empID.get(), firstname.get(), lastname.get(), dob.get(), age.get(), \
                                        gender.get(), address.get(), mobile.get())
                emp_list.delete(0, END)
                emp_list.insert(END, empID.get(), firstname.get(), lastname.get(), dob.get(), age.get(), \
                                gender.get(), address.get(), mobile.get())

        def display_data():
            emp_list.delete(0, END)
            for row in empDataBase.view_data():
                emp_list.insert(END, row + " ")

        def employee_rec(event):
            global ed
            searches = emp_list.curselection()[0]
            sd = emp_list.get(searches)

            self.empID_ent.delete(0, END)
            self.empID_ent.insert(END, sd[1])
            self.fname_ent.delete(0, END)
            self.fname_ent.insert(END, sd[2])
            self.lname_ent.delete(0, END)
            self.lname_ent.insert(END, sd[3])
            self.dob_ent.delete(0, END)
            self.dob_ent.insert(END, sd[4])
            self.age_ent.delete(0, END)
            self.age_ent.insert(END, sd[5])
            self.gender_ent.delete(0, END)
            self.gender_ent.insert(END, sd[6])
            self.addr_ent.delete(0, END)
            self.addr_ent.insert(END, sd[7])
            self.mobile_ent.delete(0, END)
            self.mobile_ent.insert(END, sd[8])

        def del_data():
            if len(empID.get()) != 0:
                empDataBase.delete_rec(ed[0])
                clear_data()
                display_data()

        def search_data():
            emp_list.delete(0, END)
            for row in empDataBase.search(empID.get(), firstname.get(), lastname.get(), dob.get(), age.get(), \
                                          gender.get(), address.get(), mobile.get()):
                emp_list.insert(END, row + " ")

        def update():
            if len(empID.get()) != 0:
                empDataBase.delete_rec(ed[0])
                if len(empID.get()) != 0:
                    empDataBase.add_emp_rec(empID.get(), firstname.get(), lastname.get(), dob.get(), age.get(), \
                                            gender.get(), address.get(), mobile.get())
                    emp_list.delete(0, END)
                    emp_list.insert(END, (empID.get(), firstname.get(), lastname.get(), dob.get(), age.get(), \
                                    gender.get(), address.get(), mobile.get()))












        # labels and entry widgets
        self.empID_lbl = Label(df_left, font=("arial", 20, "bold"),
                               text="Employee ID:", padx=2, pady=2, bg="white")
        self.empID_lbl.grid(row=0, column=0, sticky=W)
        self.empID_ent = Entry(df_left, font=("arial", 20, "bold"),
                               textvariable=empID, width=39)
        self.empID_ent.grid(row=0, column=1)

        self.fname_lbl = Label(df_left, font=("arial", 20, "bold"),
                               text="First name:", padx=2, pady=2, bg="white")
        self.fname_lbl.grid(row=1, column=0, sticky=W)
        self.fname_ent = Entry(df_left, font=("arial", 20, "bold"),
                               textvariable=firstname, width=39)
        self.fname_ent.grid(row=1, column=1)

        self.lname_lbl = Label(df_left, font=("arial", 20, "bold"),
                               text="Last name:", padx=2, pady=2, bg="white")
        self.lname_lbl.grid(row=2, column=0, sticky=W)
        self.lname_ent = Entry(df_left, font=("arial", 20, "bold"),
                               textvariable=lastname, width=39)
        self.lname_ent.grid(row=2, column=1)

        self.dob_lbl = Label(df_left, font=("arial", 20, "bold"),
                             text="Date of Birth:", padx=2, pady=2, bg="white")
        self.dob_lbl.grid(row=3, column=0, sticky=W)
        self.dob_ent = Entry(df_left, font=("arial", 20, "bold"),
                             textvariable=dob, width=39)
        self.dob_ent.grid(row=3, column=1)

        self.age_lbl = Label(df_left, font=("arial", 20, "bold"),
                             text="Age:", padx=2, pady=2, bg="white")
        self.age_lbl.grid(row=4, column=0, sticky=W)
        self.age_ent = Entry(df_left, font=("arial", 20, "bold"),
                             textvariable=age, width=39)
        self.age_ent.grid(row=4, column=1)

        self.gender_lbl = Label(df_left, font=("arial", 20, "bold"),
                                text="Gender:", padx=2, pady=2, bg="white")
        self.gender_lbl.grid(row=5, column=0, sticky=W)
        self.gender_ent = Entry(df_left, font=("arial", 20, "bold"),
                                textvariable=gender, width=39)
        self.gender_ent.grid(row=5, column=1)

        self.addr_lbl = Label(df_left, font=("arial", 20, "bold"),
                              text="Address:", padx=2, pady=2, bg="white")
        self.addr_lbl.grid(row=6, column=0, sticky=W)
        self.addr_ent = Entry(df_left, font=("arial", 20, "bold"),
                              textvariable=address, width=39)
        self.addr_ent.grid(row=6, column=1)

        self.mobile_lbl = Label(df_left, font=("arial", 20, "bold"),
                              text="Mobile:", padx=2, pady=2, bg="white")
        self.mobile_lbl.grid(row=7, column=0, sticky=W)
        self.mobile_ent = Entry(df_left, font=("arial", 20, "bold"),
                                textvariable=mobile, width=39)
        self.mobile_ent.grid(row=7, column=1)

        # Scrollbar and listbox widgets
        scrollbar = Scrollbar(df_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        emp_list = Listbox(df_right, width=41, height=16, font=("arial", 12, "bold"), yscrollcommand=scrollbar.set)
        emp_list.bind('<<ListboxSelect>>', employee_rec)
        emp_list.grid(row=0, column=0, padx=8)
        scrollbar.config(command=emp_list.yview)

        # button widgets
        btn_add = Button(btn_frame, text="Add new", font=("arial", 12, "bold"), width=10, height=1, bd=4,
                         command=add_data)
        btn_add.grid(row=0, column=0)
        btn_display = Button(btn_frame, text="Display", font=("arial", 12, "bold"), width=10, height=1, bd=4,
                             command=display_data)
        btn_display.grid(row=0, column=1)
        btn_clear = Button(btn_frame, text="Clear", font=("arial", 12, "bold"), width=10, height=1, bd=4,
                           command=clear_data)
        btn_clear.grid(row=0, column=2)
        btn_del = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), width=10, height=1, bd=4,
                         command=del_data)
        btn_del.grid(row=0, column=3)
        btn_search = Button(btn_frame, text="Search", font=("arial", 12, "bold"), width=10, height=1, bd=4,
                            command=search_data)
        btn_search.grid(row=0, column=4)
        btn_update = Button(btn_frame, text="Update", font=("arial", 12, "bold"), width=10, height=1, bd=4,
                            command=update)
        btn_update.grid(row=0, column=5)
        btn_exit = Button(btn_frame, text="Exit", font=("arial", 12, "bold"), width=10, height=1, bd=4, command=exit_app)
        btn_exit.grid(row=0, column=6)





if __name__=='__main__':
    root = Tk()
    application = Employee(root)
    root.mainloop()
