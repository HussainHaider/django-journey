import re


class Error(Exception):
    """Base class for other exceptions"""
    pass


class UniqueUserNameError(Error):
    pass


class NegativeAgeError(Error):
    pass


class AgeLimitError(Error):
    pass


class InvalidEmailError(Error):
    pass


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def main():
    dict = {}
    user_data = [
        ('Hussain', 'hussainhaider@gmail.com', 26),
        ('Hussain', 'hussain490@gmail.com', 20),
        ('Hassan', 'hassangmail.com', 26),
        ('Haider', 'haider@gmail.com', -20),
        ('Ahmed', 'ahmed@gmail.com', 14),
        ('Jawwad', 'jawwad@gmail.com', 28)
    ]

    for user in user_data:
        try:
            if user[2] < 0:
                raise NegativeAgeError()
            elif user[2] < 16:
                raise AgeLimitError()
            elif not(re.fullmatch(regex, user[1])):
                raise InvalidEmailError()
            elif user[0] in dict:
                raise UniqueUserNameError()
            else:
                dict[user[0]] = user
        except NegativeAgeError:
            print('The age is not a positive integer')
        except AgeLimitError:
            print('The user is under 16')
        except InvalidEmailError:
            print('The email address is not valid')
        except UniqueUserNameError:
            print('Given User Name is not unique')

    print(dict)


main()
