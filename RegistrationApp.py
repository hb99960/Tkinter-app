from tkinter import *
from tkinter import messagebox


user_dictionary = {}

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # validations
    if username and password and confirm_password:
        if username in user_dictionary:
            messagebox.showerror("Error", "User already exists!!!")
            return
        else:
            if password != confirm_password:
                messagebox.showerror("Error", "Both passwords should be same")
                return
            else:
                user_dictionary[username] = password
                messagebox.showinfo("Success", "Registration successfull!!!")
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                confirm_password_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "All fields are required!!!")
        return


def user_list():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
    global list_screen
    list_screen = Toplevel(home_page)
    list_screen.title("Registered Users")
    list_screen.configure(bg="white")
    list_screen.geometry("400x800")

    Label(list_screen, text="Registered Users : ", bg="white", fg="black").pack(pady=5)

    for i, user in enumerate(user_dictionary, start=1):
            text_var = f"{i}. {user}"
            Label(list_screen, text=text_var, bg="white", fg="black").pack(pady=5)

    Button(list_screen, text="Back", command=quit_list, bg="black", fg="black").pack(pady=5)

def quit_app():
    home_page.quit()

def quit_list():
    list_screen.destroy()



home_page = Tk()
home_page.title("Registration App")
home_page.geometry("800x400")
home_page.configure(bg="white")

Label(home_page, text="Enter Username : ", bg="white", fg="black" ).grid(row=0, column=0)
username_entry = Entry(home_page,bg="lightgray", fg="black")
username_entry.grid(row=0, column=1)

Label(home_page, text="Enter Password : ", bg="white", fg="black").grid(row=1, column=0)
password_entry = Entry(home_page, show="*", bg="lightgray", fg="black")
password_entry.grid(row=1, column=1)

Label(home_page, text="Confirm Password : ", bg="white", fg="black").grid(row=2, column=0)
confirm_password_entry = Entry(home_page, show="*", bg="lightgray", fg="black")
confirm_password_entry.grid(row=2, column=1)

Button(home_page, text="Register", command=register_user, bg="blue", fg="black").grid(row=3, column=1)
Button(home_page, text="Registered Users", command=user_list, bg="black", fg="black").grid(row=4, column=1)
Button(home_page, text="Quit", command=quit_app, bg="black", fg="black").grid(row=5, column=1)

# Button(home_page, text="Register", command=register_user, bg="blue", fg="white").pack(pady=5)
# Button(home_page, text="Registered Users", command=user_list, bg="black", fg="white").pack(pady=5)
# Button(home_page, text="Quit", command=quit_app, bg="black", fg="white").pack(pady=5)

home_page.mainloop()