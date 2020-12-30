# !python3
import pickle

name_number = {}
while True:
    options = str(input('Contact Commands \n (1 - Create Contact, 2 - Check All Contact, 3 - Search for Contact, 4 - Delete Contac, 5 - Exit)\n'))

    if options == '1':
        name = str(input('Enter this Contact Name:\n'))
        phoneNumber = str(input('Enter the Phone Number:\n'))
        name_number[name] = phoneNumber
        pickle.dump(name_number, open('contacts.txt', 'wb'))

    elif options == '2':
        name_number = pickle.load(open("contacts.txt", 'rb'))
        for contact in name_number.items():
            print(contact)
            
    elif options == '3':
        name_number = pickle.load(open("contacts.txt",'rb'))
        print('Enter the name that you wana look for:')
        nameSearch = input('... ')
        if nameSearch in name_number:
            print(name_number[nameSearch])
        else:
            print("I don't have that contact, or maybe, you can check your spelling")

    elif options == '4':
        name_number = pickle.load(open("contacts.txt",'rb'))
        toBeRemoved = input('Enter a Contact that you want to Remove.\n')
        if toBeRemoved in name_number:
            del name_number[toBeRemoved]
            pickle.dump(name_number, open('contacts.txt', 'wb'))
        else:
            print("I can't find that.")

    elif options == '':
        break
    elif options == '5':
        break
