import csv
import os
import tkinter as tk
from tkinter import messagebox

CSV_FILE = "address_book.csv"


def save_to_csv():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    mobile = entry_mobile.get().strip()

    if not name or not email or not mobile:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    file_exists = os.path.isfile(CSV_FILE)

    try:
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Email", "Mobile"])

            writer.writerow([name, email, mobile])

        messagebox.showinfo("Success", "Contact saved successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_mobile.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")


root = tk.Tk()
root.title("Address Book")
root.geometry("320x180")
root.resizable(False, False)

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(
    row=1, column=0, padx=10, pady=5, sticky="w"
)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Mobile:").grid(
    row=2, column=0, padx=10, pady=5, sticky="w"
)
entry_mobile = tk.Entry(root, width=30)
entry_mobile.grid(row=2, column=1, padx=10, pady=5)

btn_save = tk.Button(
    root, text="Add to Address Book", command=save_to_csv, bg="green", fg="white"
)
btn_save.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()
