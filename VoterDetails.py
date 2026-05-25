import sqlite3
import tkinter as tk
from tkinter import messagebox


class Student(tk.Frame):

    def __init__(self, master):
        super(Student, self).__init__(master)
        self.master = master
        self.master.title("Add Voters Details")
        self.master.configure(bg="black")
        self.center_window(800, 800)

        # String variable to capture radiobutton choices
        self.gender = tk.StringVar(value="Male")

        self.create_widgets()

    def center_window(self, width, height):
        """Centers the window perfectly on your monitor screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Creates the full voter entry form interface."""
        # Title Header Text
        self.label = tk.Label(
            self.master,
            text="Voter-Registration",
            fg="white",
            bg="black",
            font=("Tahoma", 45, "bold"),
        )
        self.label.place(x=120, y=15)

        # First Name Field
        tk.Label(
            self.master,
            text="First Name:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=140)
        self.txtFirstname = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtFirstname.place(x=300, y=140)

        # Other Name Field
        tk.Label(
            self.master,
            text="Other Name:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=210)
        self.txtOthername = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtOthername.place(x=300, y=210)

        # Gender Section (Linked directly to tracking variable)
        tk.Label(
            self.master,
            text="Gender:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=280)
        tk.Radiobutton(
            self.master,
            text=" Male ",
            fg="white",
            bg="black",
            selectcolor="black",
            variable=self.gender,
            value="Male",
            font=("Tahoma", 18),
        ).place(x=300, y=285)
        tk.Radiobutton(
            self.master,
            text=" Female ",
            fg="white",
            bg="black",
            selectcolor="black",
            variable=self.gender,
            value="Female",
            font=("Tahoma", 18),
        ).place(x=420, y=285)

        # Phone Field
        tk.Label(
            self.master,
            text="Phone:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=350)
        self.txtPhonenum = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtPhonenum.place(x=300, y=350)

        # Age Field
        tk.Label(
            self.master,
            text="Age:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=420)
        self.txtDob = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtDob.place(x=300, y=420)

        # Department Field
        tk.Label(
            self.master,
            text="Department:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=490)
        self.txtDep = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtDep.place(x=300, y=490)

        # Course Field
        tk.Label(
            self.master,
            text="Course:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=560)
        self.txtCourse = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtCourse.place(x=300, y=560)

        # State of Origin Field
        tk.Label(
            self.master,
            text="State of Origin:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=630)
        self.txtState = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtState.place(x=300, y=630)

        # Operational Buttons
        self.save = tk.Button(
            self.master,
            text="Register",
            width=11,
            command=self.savedata,
            font=("Tahoma", 25, "bold"),
            fg="white",
            bg="#004a99",
        )
        self.save.place(x=80, y=710)

        self.close_btn = tk.Button(
            self.master,
            text="Back to Menu",
            width=11,
            command=self.go_back,
            font=("Tahoma", 25, "bold"),
            fg="white",
            bg="#555555",
        )
        self.close_btn.place(x=350, y=710)

    def savedata(self):
        """Validates all inputs first, then safely inserts them into the SQLite database."""
        strfname = self.txtFirstname.get().strip()
        stroname = self.txtOthername.get().strip()
        strgender = self.gender.get()
        strphone = self.txtPhonenum.get().strip()
        strsdob = self.txtDob.get().strip()
        strdep = self.txtDep.get().strip()
        strcourse = self.txtCourse.get().strip()
        strstate = self.txtState.get().strip()

        # 1. Validation Check: Ensure no mandatory field is empty
        if not strfname or not strphone or not strsdob or not strdep or not strcourse:
            messagebox.showerror("Validation Error", "All mandatory fields must be filled out!")
            return

        # 2. Validation Check: Ensure age is a valid integer and at least 18
        try:
            age = int(strsdob)
            if age < 18:
                messagebox.showerror("Eligibility Error", "Sorry, you can't register. You must be 18 or older to vote.")
                return
        except ValueError:
            messagebox.showerror("Input Error", "Age must be entered as a numerical value.")
            return

        # 3. Secure Database Operation
        db = None
        try:
            db = sqlite3.connect("voter.db")
            cursor = db.cursor()

            # Ensure the table is correctly built with all columns
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Voterinfo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT, othername TEXT, gender TEXT, 
                    phonenumber TEXT, dob TEXT, department TEXT, 
                    course TEXT, state TEXT
                )
            """)

            insertqry = "INSERT INTO Voterinfo (firstname, othername, gender, phonenumber, dob, department, course, state) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
            cursor.execute(insertqry, (strfname, stroname, strgender, strphone, strsdob, strdep, strcourse, strstate))
            db.commit()

            messagebox.showinfo("Success!", "Voter record added successfully.")
            self.go_back()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Voter Registration Not Successful: {e}")
            if db:
                db.rollback()
        finally:
            if db:
                db.close()

    def go_back(self):
        """Closes this window context and cleanly switches back to the main menu dashboard."""
        self.master.destroy()
        try:
            import frmMenu
            root = tk.Tk()
            app = frmMenu.MainMenu(root)
            root.mainloop()
        except ImportError:
            messagebox.showerror("System Error", "Could not safely restore the Dashboard interface.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Student(root)
    root.mainloop()
