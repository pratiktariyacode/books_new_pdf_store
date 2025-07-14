import customtkinter as ctk
from tkinter import messagebox
import sqlite3
from ui import signup_page 
from ui import user_dashboard  
from ui import admin_panel

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

def open_signup():
    root.destroy()
    signup_page.main()

def login_user(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def main():
    global root
    root = ctk.CTk()
    root.title("Book Store - Login")

    ctk.CTkLabel(root, text="Login", font=("Arial", 35, "bold")).pack(pady=40)

    email_entry = ctk.CTkEntry(root, placeholder_text="Email", width=250, height=40)
    email_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(root, placeholder_text="Password", show="*", width=250, height=40)
    password_entry.pack(pady=10)

    def handle_login():
        email = email_entry.get()
        password = password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Please enter all fields")
            return

        user = login_user(email, password)

        if user:
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()  
            user_dashboard.main(user_email=email)  
        elif email == "admin" and password == "admin":
            email_entry.delete(0,'end')
            password_entry.delete(0,'end')
            admin_panel.main()
        else:
            messagebox.showerror("Error", "Invalid email or password")

    login_button = ctk.CTkButton(root, text="Login", width=200, height=35, command=handle_login)
    login_button.pack(pady=20)

    signup_button = ctk.CTkButton(root, text="Create New Account", command=open_signup, width=200, height=35)
    signup_button.pack()

    center_window(root, 900, 600)
    root.mainloop()
