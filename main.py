import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10)) ]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters +password_num
    shuffle(password_list)

    pwd = "".join((password_list))
    password_entry.insert(0, pwd)
    pyperclip.copy(pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = username_entry.get()
    pass_word = password_entry.get()

    new_data = {
        website: {
            "email" : email,
            "pass_word" : pass_word
        }
    }
    if website == "" or pass_word =="":
        messagebox.showinfo(title="Oops", message=f"Please don't leave any fields empty!" )
    else:
        try:
            with open("save.json","r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("save.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except JSONDecodeError:
            with open("save.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating odl data with new data
            data.update(new_data)
            with open("save.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- SEARCH pASSWORD  ------------------------------- #
def search_password():
    website = web_entry.get()
    # new_data = {
    #     website: {
    #         "email": email,
    #         "pass_word": pass_word
    #     }
    # }
    try:
        with open("save.json") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message="No File data")

    else:
        if website in data:
            email=data[website]["email"]
            password = data[website]["pass_word"]
            messagebox.showinfo(title=website,message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title= "Error", message=f'No such {website} details found')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 100, pady= 100, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(102, 102,image=pass_img)
canvas.grid(column=1,row=0)

web_label = Label(text="Website:",font=("Ariel", 10), bg= "white")
web_label.grid(column=0, row=1)

web_entry = Entry(width=32)
web_entry.grid(column=1, row= 1)
web_entry.focus()

search_button = Button(text="Search",font=("Ariel", 10), command=search_password, bg= "white",highlightthickness=0)
search_button.grid(column=2, row=1)
search_button.config(width=14)

username_label = Label(text="Email/Username:",font=("Ariel", 10), bg= "white")
username_label.grid(column=0, row=2)

username_entry = Entry(width=52)
username_entry.grid(column=1, row= 2, columnspan= 2)
username_entry.insert(0,"aathiramathew@gmail.com")

password_label = Label(text="Password:",font=("Ariel", 10), bg= "white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row= 3, columnspan=1)

gen_button = Button(text="Generate Password",command= password_generator, font=("Ariel", 10), bg= "white",highlightthickness=0)
gen_button.grid(column=2, row=3,columnspan=1)
gen_button.config(width=14)

add_button = Button(text="Add",font=("Ariel", 10),command=save_password, highlightthickness=0)
add_button.grid(column=1, row=4,columnspan=2)
add_button.config(width=39)





window.mainloop()