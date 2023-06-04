import math
prime_list = [2]
for n in range(3, 100000):
    is_prime = True
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_list.append(n)

print(prime_list)