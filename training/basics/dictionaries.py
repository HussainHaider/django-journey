students = {"name": 'John', "age": 25, 'courses': ['math', 'compsci'], 1: 'test'}
print(students['name'], students[1])

students['phone'] = '555-5555'
students['name'] = 'Jane'

print(students.get('name'), students.get('phone', 'Not Found'))

students.update({'name': 'Jane 2', 'phone': '555-12345'})

print(students)

del students['age']
print(students)
print(students.keys())
print(students.values())
print(students.items())

for key, value in students.items():
    print(key, value)
