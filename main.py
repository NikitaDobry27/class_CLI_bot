
import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name, phones=None):
        self.name = Name(name)
        self.phones = []
        if phones:
            for phone in phones:
                self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)
        
        
    def remove_phone(self, phone):
        self.phones.remove(phone)
        
    def get_phones(self):
        return self.phones
    
    def clear_phones(self):
        self.phones.clear()

    def __str__(self) -> str:
        phones_str = ', '.join([str(phone) for phone in self.phones])
        return f"{self.name}: {phones_str}"
                

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        
    def add_record(self, record):
        self.data[record.name.value] = record
        
        
    def find_records(self, query):
        result = []
        for name, record in self.data.items():
            if str(query).lower() in str(name).lower():
                result.append(record)
        return result


contacts = AddressBook()

def input_validation(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return '\nPlease provide name and phone number\n'
        except KeyError:
            return f'\nThere is no contact with such name\n'
        except ValueError:
            return '\nOnly name is required\n'
    return wrapper


def input_formatter(str):
    words_from_string = re.findall(r'\b\w+\b', str)
    command = words_from_string[0]

    if len(words_from_string) == 1:
        return command, ''
    data = words_from_string[1:]
    return command, data

def command_handler(command):
    for func, word in COMMANDS.items():
        if command in word:
            return func
    return unknown_command


def unknown_command(*args):
    return "\nThis command doesn't exist. Please try again\n"

@input_validation
def hello(*args):
    return '\nHi! How can I help you\n'

@input_validation
def add_contact(*args):
    lst = args[0]
    name = lst[0]
    phone = lst[1]

    if len(lst) < 2:
        raise IndexError
    if len(phone) > 15 or len(phone) < 9:
        return f'\n{phone} is not valid phone number\n'
    name_obj = Name(name)
    record = Record(name_obj)
    record.add_phone(Phone(phone))
    contacts.add_record(record)
   
    return f'\nContact {name.capitalize()} was successfully added\n'


@input_validation
def change(*args):
    lst = args[0]
    name = lst[0]
    phone = lst[1]

    if len(lst) < 2:
        raise IndexError
    if len(phone) > 15 or len(phone) < 9:
        return f'\n{phone} is not valid phone number\n'

    records = contacts.find_records(name)

    if records:
        for record in records:
            record.clear_phones()
            record.add_phone(Phone(phone))

        return f'\nPhone number for contact {name.capitalize()} was successfully changed\n'
    else:
        raise KeyError



@input_validation
def phone(*args):
    lst = args[0]
    if not lst:
        raise IndexError
    if len(lst) > 1:
        raise ValueError
    name = lst[0]

    records = contacts.find_records(name)
    if not records:
        raise KeyError
    
    result = ''
    for record in records:
        phones = record.get_phones()
        result += f'\nPhone number(s) for contact {str(record.name.value).capitalize()}: '
        for phone in phones:
            result += f'{phone}\n'
    return result


@input_validation
def remove_contact(*args):
    lst = args[0]
    
    if not lst:
        return '\nPlease provide "remove" and contact name\n' 

    if len(lst) > 1:
        raise ValueError
    name = lst[0]

    records = contacts.find_records(name)

    if records:
        for record in records:
            contacts.data.pop(record.name.value)
    else:
        raise KeyError
    return f'\nContact {str(name).capitalize()} was successfully removed\n'

def show_all(*args):
    if not contacts:
        return '\nYour contacts list is empty\n'
    result = ''
    for record in contacts.values():
        name = str(record.name.value).capitalize()
        phones = ', '.join(str(phone) for phone in record.get_phones())
        result += f'\n{name}: {phones}\n'
    return result


COMMANDS = {
    hello: ['hi', 'hello', 'hey'],
    add_contact: ['add'],
    change: ['change'],
    phone: ['phone'],
    show_all: ['show'],
    remove_contact: ['remove', 'delete']
}


def main():
    print(hello())
    while True:
        
        user_input = input('Type your query >>> ').lower()
            
        if user_input in ['close', '.', 'bye', 'exit']:
            print('\nSee you!')
            break
        
        try:
            command, data = input_formatter(user_input)
        except IndexError:
            print('\nPlease provide command and data\n')
            continue
            
        call = command_handler(command)

        print(call(data))


if __name__ == "__main__":
    main()