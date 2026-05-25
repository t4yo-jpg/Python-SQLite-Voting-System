import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox


class CandidateDetails(tk.Frame):

    def __init__(self, master):
        super(CandidateDetails, self).__init__(master)
        self.master = master
        self.master.title("Add Candidate Details")
        self.master.configure(bg="black")
        self.center_window(800, 860)

        # Tkinter StringVars to safely hold dynamic selection fields
        self.gender = tk.StringVar(value="Male")

        self.create_widgets()

    def center_window(self, width, height):
        """Centers the window perfectly on the desktop screen view."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Builds registration input forms cleanly using tk master targets."""
        # Main Header Title Text
        self.label = tk.Label(
            self.master,
            text="Candidate-Registration",
            fg="white",
            bg="black",
            font=("Tahoma", 45, "bold"),
        )
        self.label.place(x=100, y=15)

        # Name Field
        tk.Label(
            self.master,
            text="Name:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=140)
        self.txtname = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtname.place(x=300, y=140)

        # Phone Number Field
        tk.Label(
            self.master,
            text="Phone No:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=210)
        self.txtPhonenum = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtPhonenum.place(x=300, y=210)

        # Gender Row (Fixed Radiobutton bindings)
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

        # Age Field
        tk.Label(
            self.master,
            text="AGE:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=350)
        self.txtDob = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtDob.place(x=300, y=350)

        # Department Field
        tk.Label(
            self.master,
            text="Department:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=420)
        self.txtDep = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtDep.place(x=300, y=420)

        # Year Level Field
        tk.Label(
            self.master,
            text="Year OR Level:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=490)
        self.txtYear = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtYear.place(x=300, y=490)

        # Grade/CGPA Field
        tk.Label(
            self.master,
            text="Grade / CGPA:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=560)
        self.txtGrade = tk.Entry(self.master, width=25, font=("Tahoma", 23))
        self.txtGrade.place(x=300, y=560)

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

        # Post of Contest Selection Dropdown
        tk.Label(
            self.master,
            text="Post Of Contest:",
            fg="white",
            bg="black",
            font=("Tahoma", 23, "bold"),
        ).place(x=80, y=700)
        self.txtPost = Combobox(
            self.master,
            width=24,
            font=("Tahoma", 23),
            values=("HEAD OF DEPARTMENT", "S-U-G PRESIDENT"),
            state="readonly",
        )
        self.txtPost.place(x=300, y=700)
        self.txtPost.current(0)  # Default select first choice

        # Action Execution Interface Controls
        self.save = tk.Button(
            self.master,
            text="Register",
            width=11,
            command=self.savedata,
            font=("Tahoma", 25, "bold"),
            fg="white",
            bg="#004a99",
        )
        self.save.place(x=80, y=770)

        self.close_btn = tk.Button(
            self.master,
            text="Back to Menu",
            width=11,
            command=self.go_back,
            font=("Tahoma", 25, "bold"),
            fg="white",
            bg="#555555",
        )
        self.close_btn.place(x=360, y=770)

    def savedata(self):
        """Validates academic rules and metadata fields before storing candidate rows safely."""
        strname = self.txtname.get().strip()
        strphone = self.txtPhonenum.get().strip()
        strgender = self.gender.get()
        strdob = self.txtDob.get().strip()
        strdepartment = self.txtDep.get().strip()
        strgrade = self.txtGrade.get().strip()
        stryear = self.txtYear.get().strip()
        strstate = self.txtState.get().strip()
        strpost = self.txtPost.get()

        if (
            not strname
            or not strphone
            or not strdob
            or not strdepartment
            or not strgrade
            or not stryear
        ):
            messagebox.showerror(
                "Validation Error", "All registration input fields are required."
            )
            return

        try:
            age = int(strdob)
            gpa = float(strgrade)
            level = int(stryear)

            if age < 18:
                messagebox.showerror(
                    "Eligibility Rejection",
                    "Candidate must be 18 years or older.",
                )
                return
            if gpa < 3.0:
                messagebox.showerror(
                    "Academic Rejection",
                    "Candidate CGPA must be 3.0 or higher to contest.",
                )
                return
            if level < 300:
                messagebox.showerror(
                    "Level Rejection",
                    "Candidate must be at least in 300 Level.",
                )
                return

        except ValueError:
            messagebox.showerror(
                "Input Syntax Error",
                "Ensure Age, Grade, and Level contain numerical digits only.",
            )
            return

        # 3. Secure SQLite Database Persistence
        db = None
        try:
            db = sqlite3.connect("voter.db")
            cursor = db.cursor()

            # Renamed table structure to fix missing column runtime issue
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS CandidateRegV2 (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT, phone TEXT, gender TEXT, dob TEXT, 
                    department TEXT, grade TEXT, year TEXT, state TEXT, post TEXT
                )
            """
            )

            insertqry = "INSERT INTO CandidateRegV2 (name, phone, gender, dob, department, grade, year, state, post) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
            cursor.execute(
                insertqry,
                (
                    strname,
                    strphone,
                    strgender,
                    strdob,
                    strdepartment,
                    strgrade,
                    stryear,
                    strstate,
                    strpost,
                ),
            )
            db.commit()

            messagebox.showinfo(
                "Success!", "Candidate added to the ballot successfully."
            )
            self.go_back()

        except sqlite3.Error as e:
            messagebox.showerror(
                "Database Connection Error", f"Could not save candidate: {e}"
            )
            if db:
                db.rollback()
        finally:
            if db:
                db.close()

    def go_back(self):
        """Closes form frame structures cleanly to pop open the principal workspace dashboard."""
        self.master.destroy()
        try:
            import frmMenu

            root = tk.Tk()
            app = frmMenu.MainMenu(root)
            root.mainloop()
        except ImportError:
            messagebox.showerror("System Error", "Could not locate 'frmMenu.py'.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CandidateDetails(root)
    root.mainloop()
