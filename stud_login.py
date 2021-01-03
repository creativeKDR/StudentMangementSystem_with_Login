import mysql.connector
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="images/Bench.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=90,
                                                                                                                   y=30)
        desc = Label(Frame_login, text="Student Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90,
                                       y=100)
        lbl_usr = Label(Frame_login, text="Email ID", font=("Goudy old style", 15, "bold"), fg="gray",
                        bg="white").place(x=90,
                                          y=140)
        self.txt_usr = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_usr.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90,
                                           y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(Frame_login, command=self.forget_window, text="Forget Password?", bg="white", fg="#d77337",
                            bd=0,
                            font=("times new roman", 12)).place(x=90, y=280)
        register_btn = Button(Frame_login, command=self.register_win, text="Register", bg="white", fg="#d77337", bd=0,
                              font=("times new roman", 12)).place(x=250, y=280)
        login_btn = Button(self.root, command=self.login, text="Login", fg="white", bg="#d77337",
                           font=("times new roman", 20)).place(x=300, y=470, width=180, height=40)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_usr.delete(0, END)
        self.txt_pass.delete(0, END)

    def forget_pass(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root2)
        else:
            try:
                con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
                cur = con.cursor()
                cur.execute("select * from register where email=%s and question=%s and answer=%s",
                            (self.txt_usr.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select Correct Security Question/Enter Answer",
                                         parent=self.root2)
                else:
                    cur.execute("update register SET password=%s where email=%s",
                                (self.txt_new_pass.get(), self.txt_usr.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been Reset, Please Login with New Password",
                                        parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def forget_window(self):
        if self.txt_usr.get() == "":
            messagebox.showerror("Error", "Please enter valid Email ID to reset password", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
                cur = con.cursor()
                cur.execute("select * from register where email=%s",
                            (self.txt_usr.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Enter Valid Email ID", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white",
                              fg="red").place(
                        x=0, y=10, relwidth=1)

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                     bg="white",
                                     fg="gray").place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly')
                    self.cmb_quest['values'] = (
                        "Select", "Your Birth Place", "Your Best Friend", "Your School Teacher Name")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                                   fg="gray").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),
                                         bg="white",
                                         fg="gray").place(x=50, y=260)
                    self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_pass.place(x=50, y=290, width=250)

                    btn_change_pass = Button(self.root2, command=self.forget_pass, text="Reset Password", bg="green",
                                             fg="white",
                                             font=("times new roman", 15, "bold")).place(x=90, y=340)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def register_win(self):
        self.root.destroy()
        from Student import register

    def login(self):
        if self.txt_usr.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(user='root', port=3306, host='127.0.0.1', database='student_database')
                cur = con.cursor()
                cur.execute("select * from register where email=%s and password=%s",
                            (self.txt_usr.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Email & Password", parent=self.root)
                else:
                    self.student()
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def student(self):
        self.root.destroy()
        from Student import stud_frontend

        # elif self.txt_usr.get() != "Kalpesh" or self.txt_pass.get() != "123456":
        #    messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()
