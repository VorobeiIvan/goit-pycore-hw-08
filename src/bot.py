from src.commands import exit_bot, start_bot, add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from src.parser import parse_input
from src.decorator.colorize_message import colorize_message
from src.decorator.input_error import input_error
from src.constants import messages_error, messages
from src.addressbook_storage import load_data, save_data
from src.classes import AddressBook

@colorize_message
@input_error
def bot():
    """Основний цикл бота."""
    contacts = load_data()  
    print(messages["start_bot"])
    
    while True:
        user_input = input(messages["user_input"])
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(contacts)  
            print(exit_bot())
            break
        elif command == "hello":
            print(start_bot()) 
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        else:
            print(messages_error["invalid"])
