import customtkinter as ctk
from tkinter import messagebox, filedialog
import sqlite3
import os
import shutil
import webbrowser

DB_PATH = "users.db"

def fetch_books():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, pdf_path FROM books")
        books = cursor.fetchall()
        conn.close()
        return books
    except Exception as e:
        messagebox.showerror("Database Error", f"Error fetching books:\n{e}")
        return []

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

def main():
    root = ctk.CTk()
    root.title("View Books")

    ctk.CTkLabel(root, text="Available Books", font=("Arial", 25, "bold")).pack(pady=20)

    book_frame = ctk.CTkScrollableFrame(root, width=600, height=400)
    book_frame.pack(pady=10)

    books = fetch_books()

    if not books:
        ctk.CTkLabel(book_frame, text="No books found.", font=("Arial", 18)).pack(pady=20)
    else:
        for book_id, title, pdf_path in books:
            def open_pdf(p=pdf_path):
                if os.path.isfile(p):
                    try:
                        webbrowser.open_new(os.path.abspath(p))
                    except Exception as e:
                        messagebox.showerror("Open Error", f"Could not open PDF:\n{e}")
                else:
                    messagebox.showerror("File Not Found", f"The PDF file was not found:\n{p}")

            def download_pdf(p=pdf_path):
                if os.path.isfile(p):
                    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                    if save_path:
                        try:
                            shutil.copy(p, save_path)
                            messagebox.showinfo("Download Complete", f"File saved to:\n{save_path}")
                        except Exception as e:
                            messagebox.showerror("Download Error", f"Could not save file:\n{e}")
                else:
                    messagebox.showerror("File Not Found", f"The PDF file was not found:\n{p}")

            row = ctk.CTkFrame(book_frame)
            row.pack(fill="x", pady=5, padx=10)

            ctk.CTkLabel(row, text=title, font=("Arial", 16), anchor="w").pack(side="left", padx=10, fill="x", expand=True)
            ctk.CTkButton(row, text="Open PDF", command=open_pdf, width=100).pack(side="right", padx=5)
            ctk.CTkButton(row, text="Download", command=download_pdf, width=100).pack(side="right", padx=5)

    center_window(root, 700, 600)
    root.mainloop()


if __name__ == '__man__':
    main()
