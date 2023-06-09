
import tkinter as tk
import re
from tkinter import messagebox
from datetime import date
def validate():
    email = email_entry.get()
    civil_id = civil_id_entry.get()
    gender = gender_var.get()
    name = name_entry.get()
    pattern = r'^[^\s!#$%^&*()\-_=+\[\]{}|\\;:\'",/<>?]+$'

    if re.match(pattern, name) and re.match(pattern, email):
        if '@' not in email or '.' not in email:
            messagebox.showerror("Error", "Invalid email!")
            return
        if len(civil_id) != 12:
            messagebox.showerror("Error", "Civil ID must be 12 digits!")
            return
    else:
        messagebox.showerror("Error", "Name or Email can't have special characters!")
        return
    try:
        year = int(civil_id[1:3])
        month = int(civil_id[3:5])
        day = int(civil_id[5:7])
        year += 2000 if year < 23 else 1900
        birthdate = date(year, month, day)
    except ValueError:
        messagebox.showerror("Error", "Invalid civil ID!")
        return

    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age < 13:
        messagebox.showinfo("Sorry", "Sorry, kid! Maybe next time!")
    elif age > 18:
        messagebox.showinfo("Sorry", "It's for kids only!")
        return
    elif gender == "F":
        messagebox.showinfo("Thank you", "Thank you! 🌸")
    else:
        messagebox.showinfo("Thank you", "Thank you! 🔵")

    reset()
    root.destroy()

def reset():
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    civil_id_entry.delete(0, 'end')

def on_entry_click(entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, 'end')
        entry.configure(fg='black')

def on_entry_focus_out(entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.configure(fg='gray')

def select_male():
    gender_var.set("M")
    male_label.config(relief=tk.SUNKEN)
    female_label.config(relief=tk.RAISED)

def select_female():
    gender_var.set("F")
    female_label.config(relief=tk.SUNKEN)
    male_label.config(relief=tk.RAISED)


root = tk.Tk()
root.title("Kuwait Codes Summer Cohort Registration")
root.bg_image = tk.PhotoImage(file="kuwait.png")
root.geometry("400x300")
bg_label = tk.Label(root, image=root.bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
gender_var = tk.StringVar(value="M")

default_name = "Enter your name"
default_email = "Enter your email"
default_civil_id = "Enter your civil ID"

name_entry = tk.Entry(root)
name_entry.insert(0, default_name)
name_entry.bind('<FocusIn>', lambda event: on_entry_click(name_entry, default_name))
name_entry.bind('<FocusOut>', lambda event: on_entry_focus_out(name_entry, default_name))

email_entry = tk.Entry(root)
email_entry.insert(0, default_email)
email_entry.bind('<FocusIn>', lambda event: on_entry_click(email_entry, default_email))
email_entry.bind('<FocusOut>', lambda event: on_entry_focus_out(email_entry, default_email))

civil_id_entry = tk.Entry(root)
civil_id_entry.insert(0, default_civil_id)
civil_id_entry.bind('<FocusIn>', lambda event: on_entry_click(civil_id_entry, default_civil_id))
civil_id_entry.bind('<FocusOut>', lambda event: on_entry_focus_out(civil_id_entry, default_civil_id))

name_label = tk.Label(root, text="Name", bg='black', fg='gold', font=("Arial", 14))
email_label = tk.Label(root, text="Email", bg='black', fg='gold', font=("Arial", 14))
civil_id_label = tk.Label(root, text="Civil ID", bg='black', fg='gold', font=("Arial", 14))
gender_label = tk.Label(root, text="Gender", bg='black', fg='gold', font=("Arial", 14))

male_image = tk.PhotoImage(file="boy.png")
female_image = tk.PhotoImage(file="girl.png")

male_label = tk.Label(root, image=male_image, cursor="hand2")
male_label.bind("<Button-1>", lambda event: select_male())

female_label = tk.Label(root, image=female_image, cursor="hand2")
female_label.bind("<Button-1>", lambda event: select_female())

submit_button = tk.Button(root, text="Submit", bg='green', command=validate, font=("Arial", 14))
reset_button = tk.Button(root, text="Reset", bg='red', command=reset, font=("Arial", 14))

name_entry.pack(pady=10)
email_entry.pack(pady=10)
civil_id_entry.pack(pady=10)
submit_button.pack(anchor="s", side="right")
reset_button.pack(anchor="s", side="left")
male_label.pack(side=tk.LEFT, padx=30)
female_label.pack(side=tk.RIGHT, padx=30)

root.mainloop()
