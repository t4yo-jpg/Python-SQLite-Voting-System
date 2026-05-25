import sqlite3
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("New Horizons Ikorodu - Staff Details")


# db = sqlite3.connect('voter.db')

# cursor = db.cursor()
# for record in data:
#     db.execute("INSERT INTO Voterinfo VALUES (:voterid, :firstname, :othername, :gender, :phonenumber, :dob, :department, :course, :state)",
#                {
#                    'voterid': record[0],
#                    'firstname': record[1],
#                    'othername': record[2],
#                    'gender': record[3],
#                    'phonenumber': record[4],
#                    'dob': record[5],
#                    'department': record[6],
#                    'course': record[7],
#                    'state': record[8],
#
#                }
#                )
# db.commit()
# db.close()

def view():
    db = sqlite3.connect('voter.db')

    cursor = db.cursor()
    cursor.execute("SELECT * FROM CandidateReg")
    records = cursor.fetchall()
    global count
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                           tags=('oddrow',))

        count += 1
    cursor.close()

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
                background="white",
                foreground = "black",
                rowheight = 25,
                fieldbackground = "#fff")
style.map('Treeview',
          background = [('selected', '#004a99')])
tree_frame  =Frame(window)
tree_frame.pack(pady = 10)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
tree_scroll.config(command=my_tree.yview)
my_tree['columns'] = ("Name", "Phone No", "Gender", "Birth Date", "Department", "Year", "Grade", "State")

#Format Our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=CENTER, width=140 )
my_tree.column("Phone No", anchor=CENTER, width=140 )
my_tree.column("Gender", anchor=CENTER, width=140 )
my_tree.column("Birth Date", anchor=CENTER, width=140 )
my_tree.column("Department", anchor=CENTER, width=140 )
my_tree.column("Year", anchor=CENTER, width=140 )
my_tree.column("Grade", anchor=CENTER, width=140 )
my_tree.column("State", anchor=CENTER, width=140 )

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Phone No", text="Phone No", anchor=CENTER)
my_tree.heading("Gender", text="Gender", anchor=CENTER)
my_tree.heading("Birth Date", text="Birth Date", anchor=CENTER)
my_tree.heading("Department", text="Department", anchor=CENTER)
my_tree.heading("Year", text="Year", anchor=CENTER)
my_tree.heading("Grade", text="Grade", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)

# AdD Fake Data
# data = [
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
#     ['tayo', 'jonathan', 'male', '53533', 'uysuyfuy', 'rstfu', 'efgfygife'],
# ]
# my_tree.insert(parent='', index='end', iid=0, text="", values=( "tayo", "tayo", "male", "4535643","tdfgg" ))
# my_tree.insert(parent='', index='end', iid=1, text="", values=( "wxsxo", "tayexqsqo", "msqwale", "4535643","tdfgg" ))
# my_tree.insert(parent='', index='end', iid=2, text="", values=( "tayo", "tgttayo", "male", "4535643","tdfgg" ))
# my_tree.insert(parent='', index='end', iid=3, text="", values=( "trayo", "taryo", "male", "443","tdfgg" ))
# my_tree.insert(parent='', index='end', iid=4, text="", values=( "trayo", "tayo", "male", "4643","tdbbg" ))

#Create Stripped Row Tag
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="white")

#Add our data to the Screen






view()
window.mainloop()