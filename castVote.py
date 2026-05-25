import sqlite3
import tkinter as tk
from tkinter import messagebox


class Vote(tk.Frame):

    def __init__(self, master):
        super(Vote, self).__init__(master)
        self.master = master
        self.master.title("Cast Your Vote")
        self.master.configure(bg="black")
        self.center_window(750, 500)

        # Tkinter variable to capture and store the radio button choice
        self.selected_candidate = tk.StringVar()

        self.create_widgets()

    def center_window(self, width, height):
        """Centers the layout window perfectly on the desktop workspace screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Generates the ballot card sheet structure cleanly using tk master references."""
        # Top Heading
        self.label = tk.Label(
            self.master,
            text="Cast Your Vote",
            fg="white",
            bg="black",
            font=("Tahoma", 40, "bold"),
        )
        self.label.place(x=190, y=20)

        # Candidate Selection Fields (Fixed with tracking variable added)
        tk.Radiobutton(
            self.master,
            text="Abdullah Ogunneye",
            fg="white",
            bg="black",
            selectcolor="black",
            variable=self.selected_candidate,
            value="Abdullah Ogunneye",
            font=("Tahoma", 24),
        ).place(x=100, y=130)

        tk.Radiobutton(
            self.master,
            text="Tayo Ogunneye",
            fg="white",
            bg="black",
            selectcolor="black",
            variable=self.selected_candidate,
            value="Tayo Ogunneye",
            font=("Tahoma", 24),
        ).place(x=100, y=190)

        tk.Radiobutton(
            self.master,
            text="Thomas Müller",
            fg="white",
            bg="black",
            selectcolor="black",
            variable=self.selected_candidate,
            value="Thomas Müller",
            font=("Tahoma", 24),
        ).place(x=100, y=250)

        # Operational Execution Controls
        self.btnvote = tk.Button(
            self.master,
            text="Submit Vote",
            command=self.process_vote,
            font=("Tahoma", 20, "bold"),
            fg="white",
            bg="#b30000",
            activebackground="#800000",
            activeforeground="white",
            width=12,
        )
        self.btnvote.place(x=120, y=360)

        self.btnclose = tk.Button(
            self.master,
            text="Back to Menu",
            command=self.closepage,
            font=("Tahoma", 20, "bold"),
            fg="white",
            bg="#555555",
            activebackground="#333333",
            activeforeground="white",
            width=12,
        )
        self.btnclose.place(x=400, y=360)

    def process_vote(self):
        """Validates vote selection inputs and commits ballot counts to the SQLite database ledger."""
        ballot_choice = self.selected_candidate.get()

        # Validation: Verify the voter didn't click submit on a blank selection
        if not ballot_choice:
            messagebox.showerror(
                "Ballot Error",
                "Please select a candidate before submitting your vote!",
            )
            return

        db = None
        try:
            db = sqlite3.connect("voter.db")
            cursor = db.cursor()

            # Ensure tracking table database parameters exist
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS VotesTally (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    candidate_name TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            )

            # Insert vote selection record row
            cursor.execute(
                "INSERT INTO VotesTally (candidate_name) VALUES (?);",
                (ballot_choice,),
            )
            db.commit()

            messagebox.showinfo(
                "Success!", f"Your vote for {ballot_choice} was successfully cast!"
            )
            self.closepage()

        except sqlite3.Error as e:
            messagebox.showerror(
                "Database Error", f"Could not record vote data: {e}"
            )
            if db:
                db.rollback()
        finally:
            if db:
                db.close()

    def closepage(self):
        """Safely tears down the active window context and transfers navigation workspace loops back to dashboard."""
        self.master.destroy()
        try:
            import frmMenu

            root = tk.Tk()
            if hasattr(frmMenu, "MainMenu"):
                frmMenu.MainMenu(root)
            else:
                frmMenu.mainMenu(root)
            root.mainloop()
        except ImportError:
            messagebox.showerror(
                "System Error", "Could not restore central dashboard module."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = Vote(root)
    root.mainloop()
