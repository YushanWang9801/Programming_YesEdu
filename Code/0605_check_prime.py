n = int(input("Please enter a positive integer: "))

if n == 2:
    print("This is a prime number")
else:
    is_prime = True
    for i in range(2, n):
        print(i)
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")
    