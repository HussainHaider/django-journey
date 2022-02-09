import json

scientist_birthday = '''
{
    "Rudolf Clausius": "2/1/1822",
    "Isaac Newton": "4/1/1643",
    "Stephen Hawking": "8/1/1942",
    "Edward Teller": "15/1/1904",
    "Albert Einstein": "14/3/1879"
}
'''

data = json.loads(scientist_birthday)


def main():
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    [print(name) for name in data.keys()]
    name = input("Who's birthday do you want to look up?\n")
    try:
        print(f"{name}'s birthday is {data[name]}")
    except KeyError:
        print("No you're not a scientist man!!")


main()
