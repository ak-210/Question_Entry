import tkinter
from tkinter import filedialog, ttk, messagebox
import csv
import os
import shutil

def saveImg(num):
    user = user_entry.get()

    f = filedialog.askopenfilename()
    filename = os.path.basename(f)
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, 'figures')
    shutil.copy(f, path)
    os.rename(f'figures/{filename}', f'figures/technical_question_{user}_{num}.png')
    return f'technical_question_{user}_{num}.png'

def enter_data():
    num = 1
    with open('info/tech_no.txt', 'r') as t:
        j = t.read()
        if j != '': num = int(j)

    title = title_entry.get()
    question = que_entry.get("1.0", "end")
    constraints = con_entry.get("1.0", "end")
    company = comp_entry.get()
    difficulty = diff_entry.get()
    tags = tag_entry.get()
    topic = topic_entry.get()
    figure = saveImg(num) if fig_avl.get() else ''
    link = link_entry.get()

    if title and question and constraints and company and difficulty and tags and topic:
        with open('data/technical_questions.csv', 'a') as f:
            w = csv.writer(f)

            w.writerow([num, title, question, figure, constraints, link, company, difficulty, tags])
            num += 1

            with open('info/tech_no.txt', 'w') as t:
                t.write(str(num))
    else:
        tkinter.messagebox.showerror("Error", "Please enter all the fields.")

window = tkinter.Tk()

window.title("Technical Questions Entry")

frame = tkinter.Frame(window)
frame.pack()

user_label = tkinter.Label(frame, text="User")
user_entry = tkinter.Entry(frame)
user_label.grid(row=0, column=0)
user_entry.grid(row=0, column=1)

title_label = tkinter.Label(frame, text="Title")
title_entry = tkinter.Entry(frame)
title_label.grid(row=1, column=0)
title_entry.grid(row=1, column=1)

que_label = tkinter.Label(frame, text="Question")
que_entry = tkinter.Text(frame, height=10)
que_label.grid(row=2, column=0)
que_entry.grid(row=2, column=1)

con_label = tkinter.Label(frame, text="Constraints/options")
con_entry = tkinter.Text(frame, height=10)
con_label.grid(row=3, column=0)
con_entry.grid(row=3, column=1)

comp_label = tkinter.Label(frame, text="Company")
comp_entry = tkinter.Entry(frame)
comp_label.grid(row=4, column=0)
comp_entry.grid(row=4, column=1)

tag_label = tkinter.Label(frame, text="Tags")
tag_entry = ttk.Combobox(frame, values=['Programming', 'Aptitude', 'Case Study'])
tag_entry.current(0)
tag_label.grid(row=5, column=0)
tag_entry.grid(row=5, column=1)

fig_label = tkinter.Label(frame, text="Figure")
fig_avl = tkinter.BooleanVar(value=False)
fig_check = tkinter.Checkbutton(frame, text='Yes', variable=fig_avl, onvalue=True, offvalue=False)
fig_label.grid(row=6, column=0)
fig_check.grid(row=6, column=1)

link_label = tkinter.Label(frame, text="Link")
link_entry = tkinter.Entry(frame)
link_label.grid(row=7, column=0)
link_entry.grid(row=7, column=1)

topic_label = tkinter.Label(frame, text="Topic")
topic_entry = tkinter.Entry(frame)
topic_label.grid(row=8, column=0)
topic_entry.grid(row=8, column=1)

diff_label = tkinter.Label(frame, text="Difficulty")
diff_entry = ttk.Combobox(frame, values=["Easy", "Medium", "Hard"])
diff_entry.current(0)
diff_label.grid(row=9, column=0)
diff_entry.grid(row=9, column=1)
 
button = tkinter.Button(frame, text="Submit", command=enter_data)
button.grid(row=11, column=1)

for widget in frame.winfo_children():
    widget.grid_configure(padx=5, pady=10)
    widget.configure(width=50)

window.mainloop()