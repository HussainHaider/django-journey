my_msg = """Hello's World
too good!!"""
print(my_msg)

msg = 'Hello World'

print(len(msg))
print(msg[0])
print(msg[0:5])
print(msg[6:])
print(msg.upper())
print(msg.count('l'))
print(msg.find('World'))
print(msg.replace('World', 'Hussain'))

greeting = 'Hello'
name = 'Hussain'

# message = greeting + ', ' + name + '. Welcome!!'
# message = '{}, {}. Welcome!!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!!'
print(message)
