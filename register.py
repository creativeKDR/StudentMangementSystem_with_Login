from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="images/jason.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="images/4539592.jpg")
        bg = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        register_frame = Frame(self.root, bg="white")
        register_frame.place(x=480, y=100, width=700, height=500)

        title = Label(register_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=50, y=30)

        fname = Label(register_frame, text="First Name", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        lname = Label(register_frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(register_frame, text="Contact", font=("times new roman", 15, "bold"), bg="white",
                        fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(register_frame, text="Email", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=370, y=170)
        self.txt_email = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        question = Label(register_frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white",
                         fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(register_frame, font=("times new roman", 13), state='readonly')
        self.cmb_quest['values'] = ("Select", "Your Birth Place", "Your Best Friend", "Your School Teacher Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(register_frame, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        password = Label(register_frame, text="Password", font=("times new roman", 15, "bold"), bg="white",
                         fg="gray").place(x=50, y=310)
        self.txt_password = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        con_pass = Label(register_frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                         fg="gray").place(x=370, y=310)
        self.txt_con_pass = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_con_pass.place(x=370, y=340, width=250)

        self.var_chk = IntVar()
        chk = Checkbutton(register_frame, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1,
                          offvalue=0, bg="white",
                          font=("times new roman", 12)).place(x=50, y=380)
        self.btn_img = ImageTk.PhotoImage(file="images/unnamed.png")
        reg = Button(register_frame, command=self.register, image=self.btn_img, bd=0, cursor="hand2").place(x=50, y=420)

        self.btn2_img = ImageTk.PhotoImage(file="images/download.jpg")
        log = Button(register_frame, command=self.login, image=self.btn2_img, bd=0, cursor="hand2").place(x=240, y=420)

    def login(self):
        self.root.destroy()
        from Student import stud_login

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_con_pass.delete(0, END)
        self.cmb_quest.current(0)

    def register(self):
        if self.txt_fname.get() == "" or self.cmb_quest.get() == "Select" or self.txt_email.get() == "" or self.txt_answer.get() == "" or self.txt_contact.get() == "" or self.txt_con_pass == "" or self.txt_password == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_con_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password should be Same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree our Terms & Conditions", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
                cur = con.cursor()
                cur.execute("select * from register where email=%s", (self.txt_email.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already Exist, Please try with another Email", parent=self.root)
                else:
                    cur.execute("insert into register (f_name,l_name,contact,email,question,answer,password) values(%s,"
                                "%s,%s,%s,%s,%s,%s)", (
                                    self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfully", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()
