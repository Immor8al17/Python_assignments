import csv
import os
import sys

CSV_FILE = "address_book.csv"


def initialize_csv():
    if not os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Mobile", "Email"])


def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    mobile = input("Enter Mobile: ").strip()
    email = input("Enter Email: ").strip()

    if not name or not mobile or not email:
        print("Error: All fields are required!")
        return

    contact_list = [name, mobile, email]

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(contact_list)

    print("Contact added successfully!")


def view_contacts():
    print("\n--- Saved Contacts ---")
    if not os.path.isfile(CSV_FILE):
        print("No contacts found. The address book is empty.")
        return

    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        count = 0
        for row in reader:
            if len(row) == 3:
                print(f"Name: {row[0]} | Mobile: {row[1]} | Email: {row[2]}")
                count += 1

        if count == 0:
            print("No contacts found.")


def main():
    initialize_csv()

    while True:
        print("\n===== ADDRESS BOOK MENU =====")
        print("1. Add contact details")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
