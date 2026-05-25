import sqlite3
import tkinter as tk
from tkinter import messagebox


class ElectionResults(tk.Frame):

    def __init__(self, master):
        super(ElectionResults, self).__init__(master)
        self.master = master
        self.master.title("System Live Audit - Election Results")
        self.master.configure(bg="black")
        self.center_window(650, 450)

        self.create_widgets()
        self.calculate_winner()

    def center_window(self, width, height):
        """Centers the math metrics panel viewport perfectly on screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Generates clear visual metric blocks for the election results."""
        # Frame Layout Title Header
        tk.Label(
            self.master,
            text="LIVE ELECTION RESULTS",
            fg="white",
            bg="black",
            font=("Tahoma", 26, "bold"),
        ).pack(pady=25)

        # Winner Visual Display Block
        self.winner_card = tk.Label(
            self.master,
            text="Calculating live ledger records...",
            fg="#00ffcc",
            bg="#111111",
            font=("Tahoma", 18, "bold"),
            bd=4,
            relief="groove",
            width=38,
            height=4,
        )
        self.winner_card.pack(pady=20)

        # Breakdown Container Box
        self.stats_box = tk.Label(
            self.master,
            text="",
            fg="white",
            bg="black",
            font=("Tahoma", 14),
            justify=tk.LEFT,
        )
        self.stats_box.pack(pady=15)

        # Control Navigation Button
        tk.Button(
            self.master,
            text="Return to Dashboard",
            command=self.go_back,
            font=("Tahoma", 16, "bold"),
            fg="white",
            bg="#555555",
            activebackground="#333333",
            activeforeground="white",
            width=20,
            height=2,
        ).pack(side=tk.BOTTOM, pady=30)

    def calculate_winner(self):
        """Executes aggregate SQL queries to determine totals and identify the winner."""
        db = None
        try:
            db = sqlite3.connect("voter.db")
            cursor = db.cursor()

            # Ensure votes ledger table infrastructure exists safely
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS VotesTally (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    candidate_name TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            )

            # Query 1: Extract individual candidate totals sorted descending
            cursor.execute(
                """
                SELECT candidate_name, COUNT(candidate_name) as total_votes 
                FROM VotesTally 
                GROUP BY candidate_name 
                ORDER BY total_votes DESC
            """
            )
            tallies = cursor.fetchall()

            if not tallies:
                self.winner_card.config(
                    text="NO VOTES RECORDED\nBallot box is currently empty."
                )
                return

            # Query 2: Extract absolute sum total of all ballots cast
            cursor.execute("SELECT COUNT(*) FROM VotesTally")
            absolute_total = cursor.fetchone()[0]

            # Parse out top winner record data
            top_candidate, top_votes = tallies[0]

            # Formatting breakdown summary text output values
            breakdown_text = "Detailed Tally Breakdown:\n" + "-" * 35 + "\n"
            for name, count in tallies:
                percentage = (count / absolute_total) * 100
                breakdown_text += (
                    f"• {name}: {count} vote(s) ({percentage:.1f}%)\n"
                )

            # Inject calculated metrics back onto the UI canvas displays
            self.winner_card.config(
                text=f"WINNER ELECT: {top_candidate}\nTotal Votes: {top_votes} out of {absolute_total}"
            )
            self.stats_box.config(text=breakdown_text)

        except sqlite3.Error as e:
            messagebox.showerror(
                "Calculation Error", f"Could not audit voting totals: {e}"
            )
        finally:
            if db:
                db.close()

    def go_back(self):
        """Destroys current frame panel and returns context smoothly back to MainMenu."""
        self.master.destroy()
        try:
            import frmMenu

            root = tk.Tk()
            app = frmMenu.MainMenu(root)
            root.mainloop()
        except ImportError:
            messagebox.showerror(
                "System Error", "Could not restore central dashboard file module."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = ElectionResults(root)
    root.mainloop()
