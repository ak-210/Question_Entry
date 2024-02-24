import tkinter
from tkinter import filedialog, ttk, messagebox
import os
import shutil

def saveImg(num):
    f = filedialog.askopenfilename()
    filename = os.path.basename(f)
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, 'figures')
    shutil.copy(f, path)
    os.rename(f'figures/{filename}', f'figures/technical_question_{num}.png')


def enter_data():
    title = title_entry.get()
    question = que_entry.get("1.0", "end")
    constraints = con_entry.get("1.0", "end")
    company = comp_entry.get()
    difficulty = diff_entry.get()
    tags = tag_entry.get()
    topic = topic_entry.get()
    figure = fig_avl.get()
    link = link_avl.get()
    link_value = link_entry.get() if link else ''

    num = 1
    with open('info/tech_no.txt', 'r') as t:
        j = t.read()
        if j != '': num = int(j)

    if figure:
        figure = 'Yes'
        saveImg(num)
    else:
        figure = ''

    if title and question and constraints and company and difficulty and tags and topic:
        with open('data/technical_questions.csv', 'a') as f:
            w = csv.writer(f)

            w.writerow([num, title, question, figure, constraints, link_value, company, difficulty, tags])
            num += 1

            with open('info/tech_no.txt', 'w') as t:
                t.write(str(num))
    else:
        tkinter.messagebox.showerror("Error", "Please enter all the fields.")

window = tkinter.Tk()

window.title("Technical Questions Entry")

frame = tkinter.Frame(window)
frame.pack()

title_label = tkinter.Label(frame, text="Title")
title_entry = tkinter.Entry(frame)
title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)

que_label = tkinter.Label(frame, text="Question")
que_entry = tkinter.Text(frame, height=10)
que_label.grid(row=1, column=0)
que_entry.grid(row=1, column=1)

con_label = tkinter.Label(frame, text="Constraints/options")
con_entry = tkinter.Text(frame, height=10)
con_label.grid(row=2, column=0)
con_entry.grid(row=2, column=1)

comp_label = tkinter.Label(frame, text="Company")
comp_entry = tkinter.Entry(frame)
comp_label.grid(row=3, column=0)
comp_entry.grid(row=3, column=1)

diff_label = tkinter.Label(frame, text="Difficulty")
diff_entry = ttk.Combobox(frame, values=["Easy", "Medium", "Hard"])
diff_entry.current(0)
diff_label.grid(row=4, column=0)
diff_entry.grid(row=4, column=1)

tag_label = tkinter.Label(frame, text="Tags")
tag_entry = ttk.Combobox(frame, values=['Programming', 'Aptitude', 'Case Study'])
tag_entry.current(0)
tag_label.grid(row=5, column=0)
tag_entry.grid(row=5, column=1)

fig_label = tkinter.Label(frame, text="Figure")
fig_avl = tkinter.BooleanVar(value=False)
fig_check = tkinter.Checkbutton(frame, text='Yes', variable=fig_avl, onvalue=True, offvalue=False)
fig_button = tkinter.Button(frame, text="Browse", command=lambda: browse_file(fig_avl, 'figures/'))
fig_label.grid(row=6, column=0)
fig_check.grid(row=6, column=1)

link_label = tkinter.Label(frame, text="Link")
link_avl = tkinter.BooleanVar(value=False)
link_check = tkinter.Checkbutton(frame, text='Yes', variable=link_avl, onvalue=True, offvalue=False)
link_entry = tkinter.Entry(frame)
link_label.grid(row=9, column=0)
link_check.grid(row=9, column=1)
link_entry.grid(row=10, column=1)

topic_label = tkinter.Label(frame, text="Topic")
topic_entry = tkinter.Entry(frame)
topic_label.grid(row=8, column=0)
topic_entry.grid(row=8, column=1)

button = tkinter.Button(frame, text="Submit", command=enter_data)
button.grid(row=11, column=1)

for widget in frame.winfo_children():
    widget.grid_configure(padx=5, pady=10)
    widget.configure(width=50)

window.mainloop()