def is_prime(num):
    sqrt = int(num ** 0.5) + 1
    for i in range(2, sqrt):
        if num % i is 0:
            #print(sqrt, i)
            return False
    return True

lim = 200
biggest = 1
n = 3
while n < lim:
    if is_prime(n) is True:
        biggest = n
        n = 2 ** n - 1
    else:
        n = n + 1

print("Biggest prime number is:", biggest)
print(biggest, "is prime number?", is_prime(biggest))
#print(int(23 ** 0.5) + 1)
