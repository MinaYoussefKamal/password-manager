import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    messagebox.showinfo(title="Copied!",message="Password copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_and_clear():
    website = website_entry.get()
    user_or_email = email_or_user_entry.get()
    passw = password_entry.get()
    new_data = {
        website: {
            "email": user_or_email,
            "password": passw
        }
    }

    if len(website)==0 or len(passw)==0 or len(user_or_email)==0:
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n"
                                                      f"Email/Username: {user_or_email}\nPassword: {passw}\n\n"
                                                      f"Is it ok to save?")


        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
                    if website in data:
                        overwrite = messagebox.askyesno("Overwrite",message="There is an account registered saved to this website, do you want to overwrite it?")
                        if overwrite:
                            data.update(new_data)
                        else:
                            return
                    else:
                        data.update(new_data)



            except (FileNotFoundError,json.decoder.JSONDecodeError):
                with open("data.json","w") as f:
                    json.dump(new_data, f,indent=4)

            else:
                with open("data.json","w") as f:
                    json.dump(data, f,indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- SEARCH ------------------------------- #
def find_password():
    try:
        with open("data.json","r") as f :
                data = json.load(f)
                website = website_entry.get()
                if website in data:
                    messagebox.showinfo(title=website,message=f"Email: {data[website]['email']}\n"
                                                                  f"Password: {data[website]['password']}")
                else:
                    messagebox.showerror(title="Error",message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")


window.iconbitmap("icon.ico")
window.config(padx=50, pady=50,bg="grey15")

canvas= Canvas(width=200, height=190,bg="grey15",highlightthickness=0)
lock_image = PhotoImage(file="logo.png")

canvas.create_image(100,95,image=lock_image)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text=" Website:",bg="grey15",fg="white")
website_label.grid(column=0, row=1)

email_or_username_label = Label(text="Email/Username:",bg="grey15",fg="white")
email_or_username_label.grid(column=0, row=2)
password_label = Label(text="Password:",bg="grey15",fg="white")
password_label.grid(column=0, row=3)

# Entries

website_entry= Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

email_or_user_entry= Entry(width=52)
email_or_user_entry.insert(0, "example@gmail.com")
email_or_user_entry.grid(column=1, row=2, columnspan=2)

password_entry= Entry(width=33)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons

gen_password = Button(text="Generate Password", command=generate_password,bg="blue4",fg="white",activebackground="gray15",activeforeground="white")
gen_password.grid(column=2, row=3)

search = Button(text="Search", width=15, command=find_password,bg="blue4",fg="white",activebackground="gray15",activeforeground="white")
search.grid(column=2, row=1)

add = Button(text="Add",width=45,command= save_and_clear,bg="blue4",fg="white",activebackground="gray15",activeforeground="white")
add.grid(column=1, row=4, columnspan=2)





window.mainloop()