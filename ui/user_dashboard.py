import customtkinter as ctk
from ui import add_book_page
from ui  import view_book
from ui import login_page

def logout_fun():
    root.destroy()
    login_page.main()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

def main(user_email=None):
    global root
    root = ctk.CTk()
    root.title("User Dashboard")

    ctk.CTkLabel(root, text=f"Welcome, {user_email or 'User'}", font=("Arial", 24, "bold")).pack(pady=20)

    ctk.CTkButton(root, text="➕ Add Book", width=200, height=40, command=add_book_page.main).pack(pady=10)
    ctk.CTkButton(root, text="📚 View My Books", width=200, height=40, command=view_book.main).pack(pady=10)
    ctk.CTkButton(root, text="🚪 Logout", width=200, height=40, command=logout_fun).pack(pady=20)

    center_window(root, 600, 400)
    root.mainloop()


if __name__ == '__main__':
    main()