# Contacts Management System

This program is a simple command-line interface that allows users to manage their contacts. The program stores the contacts in a JSON file called contacts.json.

## Functions

- `load_contacts()`: loads the contacts from the JSON file
- `save_contacts(contacts)`: saves the contacts to the JSON file
- `input_validation(func)`: a decorator function that validates user input
- `input_formatter(str)`: a function that formats user input
- `command_handler(command)`: a function that handles user commands
- `unknown_command(*args)`: a function that is called when an unknown command is entered
- `hello()`: a function that greets the user
- `add_contact(*args)`: a function that adds a contact to the list
- `change(*args)`: a function that changes a contact's phone number
- `phone(*args)`: a function that retrieves a contact's phone number
- `remove_contact(*args)`: a function that removes a contact from the list
- `show_all(*args)`: a function that displays all contacts

## Classes

- `Field`: a class that represents a field of a contact (e.g. name, phone)
- `Name`: a subclass of `Field` that represents the name field of a contact
- `Phone`: a subclass of `Field` that represents the phone field of a contact
- `Record`: a class that represents a single contact (i.e. name and phone)
- `AddressBook`: a class that stores multiple contacts and provides methods for adding, removing, and finding contacts.

## Commands

The following commands are available:

- `hi`, `hello`, `hey`: greets the user
- `add`: adds a contact to the list
- `change`: changes a contact's phone number
- `phone`: retrieves a contact's phone number
- `show`: displays all contacts
- `remove`, `delete`: removes a contact from the list

## Usage

To run the program, simply execute the `main()` function. The program will display a greeting and prompt the user for input. Enter a command followed by any necessary arguments. To exit the program, enter one of the following: `close`, `.`, `bye`, or `exit`.
