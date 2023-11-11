
PHONE_BOOK = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner


@input_error
def add_handler(command):
    res = command.split(' ')
    name, phone = res[1], res[2]
    PHONE_BOOK[name] = phone
    print(PHONE_BOOK)
    return f'Contact whith name {name} and phone number {phone} added'


@input_error
def change_handler(command):
    res = command.split(' ')
    name, phone = res[1], res[2]
    if name in PHONE_BOOK:
        PHONE_BOOK[name] = phone
        return f'Contact {name} changed phone number {phone}'
    else:
        return f'Contact with {name} not found'


def exit_handler():
    return "Good bye!"


def hello_handler():
    return 'Hello, how I can help you?'


def show_all_handler():
    if PHONE_BOOK:
        phones = f'Contacts:\n'
        for name, phone in PHONE_BOOK.items():
            phones += f'{name}: {phone}\n'
        return phones
    else:
        return 'No contacts'


@input_error  
def phone_handler(command):
    res = command.split(' ')
    name = res[1]
    return PHONE_BOOK.get(name, 'not found')
    

def main():
    while True:
        command = input('Enter your text=>  ').lower()
        if command == 'hello':
            result = hello_handler()   
        elif command.startswith('add'):
            result = add_handler(command)
        elif command == 'show all':
            result = show_all_handler()
        elif command.startswith('phone'):
            result = phone_handler(command)
        elif command.startswith('change'):
            result = change_handler(command)
        elif command in ('good bye', 'close', 'exit'):
            print(exit_handler())
            break
        else:
            result = 'Comand not found, try again'
        print(result)
    

if __name__ == '__main__':
    main()
