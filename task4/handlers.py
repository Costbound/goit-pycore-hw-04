def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f'Contact "{name}" alredy exist!'
    contacts[name] = phone
    return f'Contact "{name}" added.'

def change_contact(args, contacts):
    name, phone = args
    if not(name in contacts):
        return f'Contact "{name}" does not exist!'
    contacts[name] = phone
    return f'Contact "{name}" modified.'

def get_phone(args, contacts):
    name = args[0]
    if not(name in contacts):
        return f'Contact "{name}" does not exist!'
    return f'{name}: {contacts[name]}'

def get_all_contacts(contacts):
    contact_strings = []
    for key, value in contacts.items():
        contact_strings.append(f'{key}: {value}')
    return '\n'.join(contact_strings)