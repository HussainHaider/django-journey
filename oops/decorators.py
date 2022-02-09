class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.pay = pay
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('Corey', 'Schdafer')
emp_2 = Employee('Test', 'User')

emp_1.first = 'Jim'

emp_1.fullname = 'Hussain Haider'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname