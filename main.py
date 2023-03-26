
import re
from collections import UserDict

class AddressBook(UserDict):
    pass

class Record:
    pass

class Field:
    pass

class Name:
    pass

class Phone:
    pass

contacts = {}

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
        return f'\n{phone} is not valid\n'
    contacts[name] = phone
   
    return f'\nContact {name.capitalize()} was successfully added\n'


@input_validation
def change(*args):
    lst = args[0]
    name = lst[0]
    phone = lst[1]

    if name in contacts.keys():
        contacts[name] = phone
   
        return f'\nPhone number for contact {name.capitalize()} was successfully changed\n'
    else:
        raise KeyError


@input_validation
def phone(*args):
    lst = args[0]
    if not lst:
        return '\nPlease provide "phone" and contact name\n' 
    if len(lst) > 1:
        raise ValueError
    name = lst[0]

    if name in contacts.keys():
        return f'\nPhone number for contact {name.capitalize()} is {contacts[name]}\n'

    raise KeyError

@input_validation
def remove_contact(*args):
    lst = args[0]
    
    if not lst:
        return '\nPlease provide "remove" and contact name\n' 

    if len(lst) > 1:
        raise ValueError
    name = lst[0]

    if name in contacts.keys():
        contacts.pop(name)
        
        return f'\n{name.capitalize()} was successfully removed from your contacts\n'

    raise KeyError

def show_all(*args):
    if not contacts:
        return '\nYour contacts list is empty\n'
    result = ''
    for k, v in contacts.items():
        result += f'\n{k.capitalize()}: {v}\n'
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
            print('See you!')
            break

        command, data = input_formatter(user_input)

        call = command_handler(command)

        print(call(data))


if __name__ == "__main__":
    main()