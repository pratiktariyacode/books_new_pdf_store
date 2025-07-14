import customtkinter as ctk
import sqlite3
from tkinter import messagebox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

def get_all_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def delete_user(user_id, refresh_callback):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", f"User with ID {user_id} has been deleted.")
    refresh_callback()

def main():
    global root
    root = ctk.CTk()
    root.title("Admin Panel")

    ctk.CTkLabel(root, text="Admin Panel", font=("Arial", 35, "bold")).pack(pady=20)

    frame = ctk.CTkScrollableFrame(root, width=700, height=400)
    frame.pack(pady=10)

    def load_users():
        for widget in frame.winfo_children():
            widget.destroy()

        users = get_all_users()

        if not users:
            ctk.CTkLabel(frame, text="No users found.", font=("Arial", 16)).pack(pady=10)
            return

        for user in users:
            user_id, username, email = user
            user_frame = ctk.CTkFrame(frame)
            user_frame.pack(pady=5, fill='x', padx=10)

            ctk.CTkLabel(user_frame, text=f"ID: {user_id}", width=50).pack(side='left', padx=10)
            ctk.CTkLabel(user_frame, text=f"Username: {username}", width=200).pack(side='left', padx=10)
            ctk.CTkLabel(user_frame, text=f"Email: {email}", width=200).pack(side='left', padx=10)

            del_btn = ctk.CTkButton(user_frame, text="Delete", width=80, fg_color="red",
                                     command=lambda uid=user_id: delete_user(uid, load_users))
            del_btn.pack(side='right', padx=10)

    load_users()

    center_window(root, 900, 600)
    root.mainloop()


if __name__ == '__main__':
    main()