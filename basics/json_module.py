import json

people_string = '''
{
    "people": [
        {
            "name": "Jon Smith",
            "phone": "123",
            "emails": ["jon@gmail.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "123",
            "emails": ["jane@gmail.com"],
            "has_license": false
        }
    ]
}
'''

data = json.loads(people_string)

# print(type(data['people']))

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

print(dir(json))
