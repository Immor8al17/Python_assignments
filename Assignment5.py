# Open the file in write mode ('w')
# If the file does not exist, Python will create it automatically
file = open("today_session_topics.txt", "w")

# Write each topic on a new line
file.write("File Handling Basics\n")

# Always close the file after writing
file.close()

print("Text file 'today_session_topics.txt' created successfully!")


#2. Address Book CSV Program
# Step 1: Create the CSV file and add headings if it doesn't exist yet
# Opening with 'a' creates the file if it's missing, but doesn't erase anything if it exists
file = open("address_book.csv", "a")
# If the file is completely empty, we can write the headers
# (For a beginner project, writing headers initially or just running the program is perfect)
file.close()


# Step 2: Main Program Loop
while True:
    print("\n--- ADDRESS BOOK MENU ---")
    print("1. Add contact details (Name, Mobile, Email)")
    print("2. View Contacts")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        # Take input from the user
        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email ID: ")
        
        # Create a list from this data
        contact_list = [name, mobile, email]
        
        # Convert the list items into a single comma-separated row string
        # We add a newline character (\n) at the end so the next contact starts on a new line
        row_data = contact_list[0] + "," + contact_list[1] + "," + contact_list[2] + "\n"
        
        # Open file in append mode ('a') to add data to the end without deleting old data
        file = open("address_book.csv", "a")
        file.write(row_data)
        file.close()
        
        print("Contact added successfully!")
        
    elif choice == "2":
        print("\n--- Saved Contacts ---")
        
        # Open file in read mode ('r')
        file = open("address_book.csv", "r")
        
        # Read and print each line from the file
        for line in file:
            # strip() removes the extra hidden newline spacing at the end of the line
            print(line.strip())
            
        file.close()
        print("----------------------")
        
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break  # Stops the while loop
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
