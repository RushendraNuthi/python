from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from csv import writer

root = Tk()
root.title('Student Feedback')
root.geometry('500x300')
frame_header = ttk.Frame(root)
frame_header.pack()
headerlabel = ttk.Label(frame_header, text='Student Feedback', foreground='Black',
                        font=('Century SchoolBook', 24, "bold", "underline"))
headerlabel.grid(row=0, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()

namevar = StringVar()
rollvar = StringVar()

namelabel = ttk.Label(frame_content, text='Name', font=('Constantia',10))
namelabel.grid(row=0, column=0, padx=12, sticky='sw')
entry_name = ttk.Entry(frame_content, width=24, font=('Arial', 10), textvariable=namevar)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(frame_content, text='Roll No:', font=('Constantia', 10,))
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(frame_content, width=20, font=('Arial', 10), textvariable=rollvar)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(frame_content, text='Please provide you Feedback below:', font=('Constantia', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)


textcomment.config(wrap ='word')

def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    path = 'Response.csv'
    new_list = [namevar.get(), rollvar.get(), textcomment.get(1.0, END)]
    with open( path, 'a') as f:
        csv_writer = writer(f)
        csv_writer.writerow(new_list)
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback ..!')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=5, column=0, pady=5, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=5, column=1, padx=6, sticky='w')

mainloop()
