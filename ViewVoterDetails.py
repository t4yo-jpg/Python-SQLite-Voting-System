import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ViewVoters(tk.Frame):

    def __init__(self, master):
        super(ViewVoters, self).__init__(master)
        self.master = master
        self.master.title("System Records - Voter Details")
        self.master.configure(bg="black")
        self.center_window(1150, 600)

        self.create_widgets()
        self.load_database_records()

    def center_window(self, width, height):
        """Centers the layout window perfectly on the desktop screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Creates the tabular treeview interface."""
        title_lbl = tk.Label(
            self.master,
            text="Registered Voters Records Ledger",
            fg="white",
            bg="black",
            font=("Tahoma", 24, "bold"),
        )
        title_lbl.pack(pady=20)

        # Style Configuration Engine for Treeview Elements
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#1e1e1e",
            foreground="white",
            rowheight=30,
            fieldbackground="#1e1e1e",
            font=("Tahoma", 12),
        )
        style.configure(
            "Treeview.Heading",
            font=("Tahoma", 13, "bold"),
            background="#333333",
            foreground="black",
        )
        style.map("Treeview", background=[("selected", "#004a99")])

        tree_frame = tk.Frame(self.master, bg="black")
        tree_frame.pack(pady=10, fill="both", expand=True, padx=30)

        tree_scroll = tk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.my_tree = ttk.Treeview(
            tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended"
        )
        self.my_tree.pack(fill="both", expand=True)
        tree_scroll.config(command=self.my_tree.yview)

        self.my_tree["columns"] = (
            "FirstName",
            "OtherName",
            "Gender",
            "Phone No",
            "Age",
            "Department",
            "Course",
            "State",
        )

        self.my_tree.column("#0", width=0, stretch=tk.NO)
        self.my_tree.column("FirstName", anchor=tk.CENTER, width=130)
        self.my_tree.column("OtherName", anchor=tk.CENTER, width=130)
        self.my_tree.column("Gender", anchor=tk.CENTER, width=90)
        self.my_tree.column("Phone No", anchor=tk.CENTER, width=130)
        self.my_tree.column("Age", anchor=tk.CENTER, width=80)
        self.my_tree.column("Department", anchor=tk.CENTER, width=140)
        self.my_tree.column("Course", anchor=tk.CENTER, width=140)
        self.my_tree.column("State", anchor=tk.CENTER, width=130)

        self.my_tree.heading("#0", text="", anchor=tk.W)
        self.my_tree.heading("FirstName", text="First Name", anchor=tk.CENTER)
        self.my_tree.heading("OtherName", text="Other Name", anchor=tk.CENTER)
        self.my_tree.heading("Gender", text="Gender", anchor=tk.CENTER)
        self.my_tree.heading("Phone No", text="Phone Number", anchor=tk.CENTER)
        self.my_tree.heading("Age", text="Age", anchor=tk.CENTER)
        self.my_tree.heading("Department", text="Department", anchor=tk.CENTER)
        self.my_tree.heading("Course", text="Course Path", anchor=tk.CENTER)
        self.my_tree.heading("State", text="State of Origin", anchor=tk.CENTER)

        self.my_tree.tag_configure("oddrow", background="#2a2a2a", foreground="white")
        self.my_tree.tag_configure("evenrow", background="#1e1e1e", foreground="white")

        btn_frame = tk.Frame(self.master, bg="black")
        btn_frame.pack(pady=20)

        self.btnclose = tk.Button(
            btn_frame,
            text="Return to Dashboard",
            command=self.go_back,
            font=("Tahoma", 16, "bold"),
            fg="white",
            bg="#555555",
            activebackground="#333333",
            activeforeground="white",
            width=20,
            height=2,
        )
        self.btnclose.pack()

    def load_database_records(self):
        """Safely extracts table rows from voter.db to fill the view ledger."""
        db = None
        try:
            db = sqlite3.connect("voter.db")
            cursor = db.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Voterinfo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT, othername TEXT, gender TEXT, 
                    phonenumber TEXT, dob TEXT, department TEXT, 
                    course TEXT, state TEXT
                )
            """
            )

            cursor.execute("SELECT * FROM Voterinfo")
            records = cursor.fetchall()

            for item in self.my_tree.get_children():
                self.my_tree.delete(item)

            for count, record in enumerate(records):
                row_tag = "evenrow" if count % 2 == 0 else "oddrow"

                # Dynamic tuple mapping to avoid out-of-index boundary slips
                val_tuple = (
                    record[1], record[2], record[3], record[4],
                    record[5], record[6], record[7], record[8] if len(record) > 8 else ""
                )

                self.my_tree.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text="",
                    values=val_tuple,
                    tags=(row_tag,),
                )

        except sqlite3.Error as e:
            messagebox.showerror(
                "Data Query Error", f"Unable to read data safely: {e}"
            )
        finally:
            if db:
                db.close()

    def go_back(self):
        """Safely tears down the active view and restores the main workspace context."""
        self.master.destroy()
        try:
            import frmMenu

            root = tk.Tk()
            app = frmMenu.MainMenu(root)
            root.mainloop()
        except ImportError:
            messagebox.showerror(
                "System Error", "Could not safely restore the dashboard dashboard loop."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = ViewVoters(root)
    root.mainloop()
