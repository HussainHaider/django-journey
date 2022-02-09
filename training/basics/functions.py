def hello_func(greeting, name='You'):
    return f'hello, {name} function! {greeting}'


print(hello_func('Hi', 'Test'))


def students_info(*args, **kwargs):
    print(args)
    print(kwargs)


students_info('Math', 'Art', name='John', age=33)
