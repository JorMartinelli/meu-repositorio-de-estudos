contacts_list = []

def save_contact(contacts_list, name, phone_number, email):
    contact = {"name": name, "phone number": phone_number, "email": email, "favorite": False}
    contacts_list.append(contact)
    print("Contact saved successfully!")

def print_contacts(contacts_list):
    print("\nContact List:")
    for index, contact in enumerate(contacts_list, start=1):
        favorite = "★" if contact["favorite"] else " "
        name_contact = contact["name"]
        print(f"{index}. [{favorite}] {name_contact}")

def edit_contact(contacts_list, contact_index, name, phone_number, email):
    index = int(contact_index) - 1
    if index >= 0 and index < len(contacts_list):
        contacts_list[index] = {"name": name, "phone number": phone_number, "email": email, "favorite": False}
        print("Contact edited successfully!")
    else:
        print("Invalid contact index.")

def mark_favorite(contacts_list, contact_index):
    index = int(contact_index) - 1
    if index >= 0 and index < len(contacts_list):
        contacts_list[index]["favorite"] = True
        print("Contact marked as favorite.")
    else:
        print("Invalid contact index.")

def delete_contact(contacts_list, contact_index):
    index = int(contact_index) - 1
    if index >= 0 and index < len(contacts_list):
        contacts_list.pop(index)
        print("Contact deleted successfully!.")
    else:
        print("Invalid contact index.")

while True:

    print("\nContact List Menu:")
    print("1. Save Contact")
    print("2. Edit Contact")
    print("3. Mark a Contact as a Favorite")
    print("4. Delete Contact")
    print("5. View Contact List")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name of the contact: ")
        phone_number = input("Enter the contact number: ")
        email = input("Enter the contact email: ")
        save_contact(contacts_list, name, phone_number, email)
    
    elif choice == "2":
        print_contacts(contacts_list)
        contact_index = input("Enter the contact index to edit: ")
        name = input("Enter the new contact name: ")
        phone_number = input("Enter the new contact number: ")
        email = input("Enter the new contact email: ")
        edit_contact(contacts_list, contact_index, name, phone_number, email)

    elif choice == "3":
        print_contacts(contacts_list)
        contact_index = input("Enter the contact index to favorite: ")
        mark_favorite(contacts_list, contact_index)

    elif choice == "4":
        print_contacts(contacts_list)
        contact_index = input("Enter the contact index to delete: ")
        delete_contact(contacts_list, contact_index)
    
    elif choice == "5":
        print_contacts(contacts_list)

    else:
        print("Invalid choice.")

# TODO: add error handling and input validation 





















