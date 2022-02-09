def fibonacci(length):
    if length == 0 or length == 1:
        return 1
    return fibonacci(length-1) + fibonacci(length-2)


def main():
    while(True):
        val = input("Enter your value: ")
        list = [fibonacci(n) for n in range(int(val))]
        print(list)


main()
