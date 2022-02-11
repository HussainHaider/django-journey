import json

file_name = 'data.json'


def main():
    with open(file_name, 'r') as file:
        data = json.load(file)
        print('Welcome to the birthday dictionary. We know the birthdays of:')
        [print(name) for name in data.keys()]
        name = input("Proivde us the scientist name?\n")
        date = input(f"Proivde us the birthday of {name}?\n")
        try:
            data.update({name: date})
            with open(file_name, 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except KeyError:
            print("Something went wrong!!")


main()
