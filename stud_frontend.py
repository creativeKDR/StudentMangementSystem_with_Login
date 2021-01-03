from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


# from Student import stud_login


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management and Attendance System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="blue")
        # Title

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="red", fg="yellow")
        title.pack(side=TOP, fill=X)

        # Variables

        self.rollno_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Frames

        Edit_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="skyblue")
        Edit_Frame.place(x=20, y=100, width=450, height=520)

        e_title = Label(Edit_Frame, text="Manage Student", bg="skyblue", fg="black",
                        font=("times new roman", 30, "bold"))
        e_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Edit_Frame, text="Roll No.", bg="skyblue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Edit_Frame, textvariable=self.rollno_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Edit_Frame, text="Name", bg="skyblue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Edit_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Edit_Frame, text="Email", bg="skyblue", fg="black",
                          font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Edit_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Edit_Frame, text="Gender", bg="skyblue", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Edit_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_dob = Label(Edit_Frame, text="Date of Birth", bg="skyblue", fg="black",
                        font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Edit_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_num = Label(Edit_Frame, text="Contact No.", bg="skyblue", fg="black",
                        font=("times new roman", 20, "bold"))
        lbl_num.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_num = Entry(Edit_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_num.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_add = Label(Edit_Frame, text="Address", bg="skyblue", fg="black",
                        font=("times new roman", 20, "bold"))
        lbl_add.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_add = Text(Edit_Frame, font=("times new roman", 10, "bold"), width=30, height=4)
        self.txt_add.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="skyblue")
        Detail_Frame.place(x=500, y=100, width=800, height=560)

        lbl_search = Label(Detail_Frame, text="Search By", bg="skyblue", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10,
                                    font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"),
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, command=self.search_data, text="Search", width=10, pady=5).grid(row=0,
                                                                                                         column=3,
                                                                                                         padx=10,
                                                                                                         pady=10)
        Showallbtn = Button(Detail_Frame, command=self.fetch_data, text="Show All", width=10, pady=5).grid(row=0,
                                                                                                           column=4,
                                                                                                           padx=10,
                                                                                                           pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact No.")
        self.Student_table.heading("dob", text="Date of Birth")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        btn_Frame.place(x=20, y=630, width=450)

        Addbtn = Button(btn_Frame, text="ADD", width=10, command=self.add_students, pady=5).grid(row=0, column=0,
                                                                                                 padx=10, pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_students, pady=5).grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data, pady=5).grid(row=0, column=2,
                                                                                                      padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear, pady=5).grid(row=0, column=3, padx=10,
                                                                                              pady=10)
        createdby_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        createdby_Frame.place(x=500, y=660, width=800)

        lbl_created = Label(createdby_Frame, text="Created By: Creative KDR", bg="blue", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_created.grid(row=0, column=1, pady=10, padx=20)

    def add_students(self):
        if self.rollno_var.get() == "" or self.name_var.get() == "" or self.gender_var.get() == "" or self.dob_var == "" or self.contact_var == "" or self.email_var == "" or self.txt_add == "":
            messagebox.showerror("Error", "All fields are Required!!!")
        else:
            con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
            cur = con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)", (self.rollno_var.get(),
                                                                             self.name_var.get(),
                                                                             self.email_var.get(),
                                                                             self.gender_var.get(),
                                                                             self.contact_var.get(),
                                                                             self.dob_var.get(),
                                                                             self.txt_add.get('1.0', END)
                                                                             ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been Inserted")

    def fetch_data(self):
        con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.rollno_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_add.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.rollno_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_add.delete("1.0", END)
        self.txt_add.insert(END, row[6])

    def update_students(self):
        con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
        cur = con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                    (self.name_var.get(),
                     self.email_var.get(),
                     self.gender_var.get(),
                     self.contact_var.get(),
                     self.dob_var.get(),
                     self.txt_add.get('1.0', END),
                     self.rollno_var.get()
                     ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been Updated")

    def delete_data(self):
        con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
        cur = con.cursor()
        cur.execute("delete from student where roll_no=%s",
                    (self.rollno_var.get(),))  # mysql.1064 (42000) if this got error then tuple for value (,)
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been Deleted")

    def search_data(self):
        con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
        cur = con.cursor()
        # print(self.search_by.get())
        cur.execute(
            "select * from student where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        else:
            messagebox.showerror("Error", "Search Data Not Found")
            con.close()

    """def search_data(self):
        con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
        cur = con.cursor()
        # print(self.search_by.get())
        cur.execute(
            "select * from student where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")

        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()"""


root = Tk()
app = Student(root)
root.mainloop()
