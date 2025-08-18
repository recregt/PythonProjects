contact_book = []

while True:
    print("Contact Book Options:\n1. Add a new contact\n2. View all contacts\n3. Search for a contact\n4. Remove a contact\n5. Exit\n")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        new_contact = {'name': name, 'phone': phone}
        contact_book.append(new_contact)
        print(f"\nContact '{name}' has been added.\n")
                           
    elif choice == '2':
        if not contact_book:
            print("\nThe contact book is empty.\n")
        else:
            print("\n--- Contact Book ---")
            for index, contact in enumerate(contact_book):
                print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}\n")        
        
    elif choice == '3':
        search_name = input("Enter the name to search: ")
        found = False
        for contact in contact_book:
            if contact['name'].lower() == search_name.lower():
                print(f"\n--- Contact Found ---\nName: {contact['name']}\nPhone: {contact['phone']}\n")
                found = True
                break
        if not found:
            print(f"\nContact '{search_name}' not found.\n")
                
    elif choice == '4':
        if not contact_book:
            print("\nThe contact book is empty. Nothing to remove.\n")
        else:
            print("\n--- Current Contacts ---")
            for index, contact in enumerate(contact_book):
                print(f"{index + 1}. Name: {contact['name']}")
            
            try:
                contact_number = int(input("\nEnter the number of the contact to remove: "))
                if 1 <= contact_number <= len(contact_book):
                    removed_contact = contact_book.pop(contact_number - 1)
                    print(f"\nContact '{removed_contact['name']}' has been removed.\n")
                else:
                    print("Invalid contact number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
    elif choice == '5':
        print("\nExiting the application.")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.\n")