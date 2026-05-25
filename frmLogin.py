import hashlib
import tkinter as tk
from tkinter import messagebox


class Login(tk.Frame):

    def __init__(self, master):
        super(Login, self).__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.configure(bg="black")
        self.center_window(750, 500)

        # Variables to store user input
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def center_window(self, width, height):
        """Centers the login window perfectly on the desktop screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Creates and places UI elements inside the master window."""
        # Title Label
        self.label = tk.Label(
            self.master,
            text="Login",
            fg="white",
            bg="black",
            font=("Tahoma", 45, "bold"),
        )
        self.label.place(x=320, y=30)

        # Username Label and Entry
        self.lbusername = tk.Label(
            self.master,
            text="Username:",
            fg="white",
            bg="black",
            font=("Tahoma", 30, "bold"),
        )
        self.lbusername.place(x=90, y=160)

        self.txtusername = tk.Entry(
            self.master,
            width=30,
            textvariable=self.username,
            bd=2,
            font=("Tahoma", 20),
        )
        self.txtusername.place(x=290, y=168)

        # Password Label and Entry
        self.lbpassword = tk.Label(
            self.master,
            text="Password:",
            fg="white",
            bg="black",
            font=("Tahoma", 30, "bold"),
        )
        self.lbpassword.place(x=90, y=275)

        self.txtpassword = tk.Entry(
            self.master,
            show="*",
            width=30,
            textvariable=self.password,
            bd=2,
            font=("Tahoma", 20),
        )
        self.txtpassword.place(x=290, y=275)

        # Login Button
        self.btnLogin = tk.Button(
            self.master,
            text="Login",
            width=8,
            command=self.processlogin,
            fg="black",
            bg="white",
            font=("Tahoma", 20, "bold"),
        )
        self.btnLogin.place(x=499, y=400)

    def processlogin(self):
        """Validates credentials and hands off the view to the Main Dashboard."""
        struser = self.username.get()
        strpass = self.password.get()

        # 1. Scramble the password the user just typed into the entry box
        hashed_input = hashlib.sha256(strpass.encode()).hexdigest()

        # 2. This is the secure SHA-256 hash string for the password "12345"
        correct_password_hash = (
            "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
        )

        # 3. Check the username normally, but compare the hashed password string
        if struser == "Admin" and hashed_input == correct_password_hash:
            messagebox.showinfo("Confirmation", "User Login is successful.")
            self.master.destroy()  # Safely closes the login window

            # Dynamically open the central dashboard window
            try:
                import frmMenu

                root = tk.Tk()
                app = frmMenu.MainMenu(root)
                root.mainloop()
            except ImportError as e:
                messagebox.showerror(
                    "File Link Error",
                    f"Could not load 'frmMenu.py'.\nDetail: {e}",
                )
        else:
            messagebox.showerror("Error", "Invalid Username or Password.")


# Application startup gateway
if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
