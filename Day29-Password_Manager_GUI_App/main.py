from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,"end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for letter in range(randint(8, 10))]
    symbol_list = [choice(symbols) for symbol in range(randint(2, 4))]
    number_list = [choice(numbers) for number in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if website_text == "" or password_text == "":
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text,message=f"These are the details entered: \nEmail: {email_text} "
                                                                  f"\nPassword: {password_text} \nIs it okay to save?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_text = f"{website_text} | {email_text} | {password_text}\n"
                data_file.write(data_text)
                website_entry.delete(0,"end")
                password_entry.delete(0,"end")
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
# canvas.pack()

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry = Entry(width=35,justify="center")
website_entry.grid(row=1,column=1,columnspan=2,sticky="w")
website_entry.focus()

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2,column=0)

email_entry = Entry(width=35,justify="center")
email_entry.grid(row=2,column=1,columnspan=2,sticky="w")
email_entry.insert(0,"chickenteriyaki@gmail.com")

# Note: chickenteriyaki@gmail.com is a dummy Gmail account. I just wrote that because I was
#       craving for some chicken teriyaki. 😅

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry = Entry(width=35,justify="center")
password_entry.grid(row=3,column=1,sticky="w")

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2,sticky="w")

add_button = Button(width=29,text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="w")










window.mainloop()