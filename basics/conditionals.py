langauage = 'javascript'
if langauage == 'python':
    print('condition was python')
elif langauage == 'javascript':
    print('condition was javascript')
else:
    print('No match!!')


user = 'Admin'
logged_in = False

if user == 'admin' and logged_in:
    print('Admin Page')
elif not logged_in:
    print('plz login')
else:
    print('Bad Creds')


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)
print(a is b)

c = a 
print(id(a))
print(id(c))
print(a == c)
print(a is c)
