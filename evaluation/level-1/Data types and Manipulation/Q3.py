import json
import datetime


file_name = 'data.json'
months = {}


def main():
    with open(file_name, 'r') as file:
        data = json.load(file)
        for value in data:
            date = data[value].split('/')
            month_value = datetime.date(int(date[2]), int(date[1]), int(date[0])).strftime('%B')
            try:
                months[month_value] = months[month_value] + 1
            except KeyError:
                months[month_value] = 1
        print(months)


main()
