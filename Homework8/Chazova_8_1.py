import re

def email_parse(address):
    try:
        dict = {}
        user = re.search(r'[A-Za-z1-9]*', address)
        domain = re.search(r'[A-Za-z1-9]*\.ru', address)
        dict['username'] = user.group()
        dict['domain'] = domain.group()
    except AttributeError:
        msg = f'wrong email {address}'
        raise AttributeError(msg)

    return dict

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))

