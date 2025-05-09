import re

class Contact:
    def __init__(self, name, phone, email, store_name, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.store_name = store_name
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self):
        print("\nAdd New Contact")
        name = input("Enter name: ").strip()
        
        # Validate phone number
        while True:
            phone = input("Enter phone number: ").strip()
            if self.validate_phone(phone):
                break
            print("Invalid phone number. Please enter a 10-digit number.")
        
        # Validate email
        while True:
            email = input("Enter email: ").strip()
            if self.validate_email(email):
                break
            print("Invalid email format. Please enter a valid email.")
        
        store_name = input("Enter store name: ").strip()
        address = input("Enter address: ").strip()
        
        new_contact = Contact(name, phone, email, store_name, address)
        self.contacts.append(new_contact)
        print(f"\nContact '{name}' added successfully!")
    
    def validate_phone(self, phone):
        return re.match(r'^\d{10}$', phone) is not None
    
    def validate_email(self, email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None
    
    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
            return
        
        print("\nContact List:")
        print("-" * 50)
        print(f"{'No.':<5}{'Name':<20}{'Phone':<15}{'Store':<20}")
        print("-" * 50)
        
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i:<5}{contact.name:<20}{contact.phone:<15}{contact.store_name:<20}")
    
    def search_contact(self):
        if not self.contacts:
            print("\nNo contacts to search.")
            return
        
        search_term = input("\nEnter name or phone number to search: ").strip().lower()
        found = False
        
        print("\nSearch Results:")
        print("-" * 80)
        print(f"{'Name':<20}{'Phone':<15}{'Email':<25}{'Store':<20}")
        print("-" * 80)
        
        for contact in self.contacts:
            if (search_term in contact.name.lower()) or (search_term in contact.phone):
                print(f"{contact.name:<20}{contact.phone:<15}{contact.email:<25}{contact.store_name:<20}")
                found = True
        
        if not found:
            print("No matching contacts found.")
    
    def update_contact(self):
        if not self.contacts:
            print("\nNo contacts to update.")
            return
        
        self.view_contacts()
        try:
            contact_num = int(input("\nEnter the number of the contact to update: ")) - 1
            if 0 <= contact_num < len(self.contacts):
                contact = self.contacts[contact_num]
                print("\nCurrent Contact Details:")
                self.display_full_contact(contact)
                
                print("\nEnter new details (leave blank to keep current value):")
                name = input(f"Name [{contact.name}]: ").strip() or contact.name
                
                while True:
                    phone = input(f"Phone [{contact.phone}]: ").strip()
                    if not phone:
                        phone = contact.phone
                        break
                    if self.validate_phone(phone):
                        break
                    print("Invalid phone number. Please enter a 10-digit number.")
                
                while True:
                    email = input(f"Email [{contact.email}]: ").strip()
                    if not email:
                        email = contact.email
                        break
                    if self.validate_email(email):
                        break
                    print("Invalid email format. Please enter a valid email.")
                
                store_name = input(f"Store Name [{contact.store_name}]: ").strip() or contact.store_name
                address = input(f"Address [{contact.address}]: ").strip() or contact.address
                
                # Update the contact
                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.store_name = store_name
                contact.address = address
                
                print("\nContact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def delete_contact(self):
        if not self.contacts:
            print("\nNo contacts to delete.")
            return
        
        self.view_contacts()
        try:
            contact_num = int(input("\nEnter the number of the contact to delete: ")) - 1
            if 0 <= contact_num < len(self.contacts):
                deleted_name = self.contacts[contact_num].name
                del self.contacts[contact_num]
                print(f"\nContact '{deleted_name}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def display_full_contact(self, contact):
        print("\nContact Details:")
        print("-" * 40)
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Store Name: {contact.store_name}")
        print(f"Address: {contact.address}")
        print("-" * 40)

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
            if manager.contacts:
                view_details = input("\nEnter a contact number to view details (or press Enter to continue): ").strip()
                if view_details:
                    try:
                        contact_num = int(view_details) - 1
                        if 0 <= contact_num < len(manager.contacts):
                            manager.display_full_contact(manager.contacts[contact_num])
                        else:
                            print("Invalid contact number.")
                    except ValueError:
                        print("Please enter a valid number.")
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("\nExiting Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()