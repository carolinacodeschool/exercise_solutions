# Electronic Phone Book
# == == == == == == == == == == =
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

# What do you want to do(1-5)?

phonebook = {
    "clark": "555-426-7877",
    "bruce": "555-426-2866"
}
running = True

while running == True:
    print("Choose one of the following options:")
    print("-------------------")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

    option = input("What do you want to do? Select from option 1-5. ")

    if not option:
        print("no number chosen")
        optionInt = 0
        pass
    else:
        optionInt = int(option)

    if optionInt == 1:
        lookup = input("What is the contact's name? ")
        lowercase_name = lookup.lower()
        if lowercase_name in phonebook:
            print(lookup.capitalize() +"'s phone number is: " + phonebook[lowercase_name])
        else:
            print("No entry found for " + lookup.capitalize())
        pause = input("Press any key to continue...")
        print('\033c')
    elif optionInt == 2:
        name = input("Contact name: ")
        number = input("Contact number: ")
        lowercase_name = name.lower()
        phonebook[lowercase_name] = number
        print("Entry stored for " + name + ".")
        pause = input("Press any key to continue...")
        print('\033c')
    elif optionInt == 3:
        contact_to_remove = input("Which contact would you like to delete? ")
        lower_ctr = contact_to_remove.lower()
        if lower_ctr in phonebook:
            del phonebook[lower_ctr]
            print("Deleted contact " + contact_to_remove)
        else:
            print("No entry found for " + contact_to_remove)
        pause = input("Press any key to continue...")
        print('\033c')
    elif optionInt == 4:
        for contact in phonebook:
            print("Found entry for " + contact.capitalize() + ": " + phonebook[contact])
        pause = input("Press any key to continue...")
    elif optionInt == 5:
        print("Goodbye!")
        running = False
    else:
        pause = input("Invalid selection. Press any key to continue...")
        pass
else:
    exit()