
entered_num = int(input("Enter number to check if prime:    "))

def is_prime(num):
    if num <= 1:
        return print("Not a prime number")
    for n in range(2, num):
        if num % n == 0:
            return print("Not a prime number")
    return print("Prime number!")

is_prime(entered_num)
