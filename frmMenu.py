import tkinter as tk
from tkinter import messagebox


class MainMenu(tk.Frame):

    def __init__(self, master):
        super(MainMenu, self).__init__(master)
        self.master = master
        self.master.title("Voting Application - Dashboard")
        self.master.configure(bg="black")
        self.center_window(750, 500)

        self.create_widgets()

    def center_window(self, width, height):
        """Centers the dashboard window perfectly on your monitor screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        """Creates a stable button-based layout to completely bypass macOS menu crashes."""
        # Main Title Header
        title_lbl = tk.Label(
            self.master,
            text="VOTING SYSTEM DASHBOARD",
            fg="white",
            bg="black",
            font=("Tahoma", 28, "bold"),
        )
        title_lbl.pack(pady=40)

        # Container Frame for Grid Buttons
        btn_frame = tk.Frame(self.master, bg="black")
        btn_frame.pack(expand=True, fill="both", padx=50, pady=10)

        # Configure Grid Weights for Uniform Sizing
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        # Style attributes for professional buttons
        btn_style = {
            "font": ("Tahoma", 16, "bold"),
            "fg": "white",
            "bg": "#004a99",
            "activebackground": "#003366",
            "activeforeground": "white",
            "height": 2,
            "width": 18,
            "bd": 4,
            "relief": "raised",
        }

        # Row 1: Administrative Controls
        btn_add_voter = tk.Button(
            btn_frame, text="Add Voters", command=self.loadaddv, **btn_style
        )
        btn_add_voter.grid(row=0, column=0, padx=20, pady=15)

        btn_add_candidate = tk.Button(
            btn_frame,
            text="Add Candidates",
            command=self.loadcandidate,
            **btn_style,
        )
        btn_add_candidate.grid(row=0, column=1, padx=20, pady=15)

        # Row 2: Voting & Actions
        btn_cast_vote = tk.Button(
            btn_frame, text="Cast Vote", command=self.loadcv, **btn_style
        )
        btn_cast_vote.grid(row=1, column=0, padx=20, pady=15)

        btn_view_voters = tk.Button(
            btn_frame,
            text="View Voter Details",
            command=self.loadvvd,
            **btn_style,
        )
        btn_view_voters.grid(row=1, column=1, padx=20, pady=15)

        # Row 3: Bottom System Management Row
        btn_view_candidates = tk.Button(
            btn_frame,
            text="View Election Results",
            command=self.loadvcd,
            **btn_style,
        )
        btn_view_candidates.grid(row=2, column=0, padx=20, pady=15)

        btn_logout = tk.Button(
            btn_frame,
            text="Log Out",
            command=self.loadlogin,
            font=("Tahoma", 16, "bold"),
            fg="white",
            bg="#b30000",
            activebackground="#800000",
            activeforeground="white",
            height=2,
            width=18,
            bd=4,
            relief="raised",
        )
        btn_logout.grid(row=2, column=1, padx=20, pady=15)

    def loadlogin(self):
        self.master.destroy()
        import frmLogin
        root = tk.Tk()
        frmLogin.Login(root)
        root.mainloop()

    def loadcandidate(self):
        self.master.destroy()
        import CandidateDetails
        root = tk.Tk()
        CandidateDetails.CandidateDetails(root)
        root.mainloop()

    def loadaddv(self):
        self.master.destroy()
        import VoterDetails
        root = tk.Tk()
        VoterDetails.Student(root)
        root.mainloop()

    def loadcv(self):
        self.master.destroy()
        import castVote
        root = tk.Tk()
        castVote.Vote(root)
        root.mainloop()

    def loadvvd(self):
        self.master.destroy()
        import ViewVoterDetails
        root = tk.Tk()
        ViewVoterDetails.ViewVoters(root)
        root.mainloop()

    def loadvcd(self):
        self.master.destroy()
        import frmResults
        root = tk.Tk()
        frmResults.ElectionResults(root)
        root.mainloop()


# System execution gateway
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
