def print_prime_number(limit):
    for num in range(0, limit + 1):
        prime = True
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    prime = False
                    break
            if prime:
                print(num)


limit = input("Enter your limit: ")

print_prime_number(int(limit))
