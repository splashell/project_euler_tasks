number = 600851475143
lower = 0
upper = 7000
primes = []

'''Seek prime numbers within lower-upper range.'''
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
    if num > 1:
       for i in range(2, num):

           if (num % i) == 0:
               break
       else:
           if num not in primes:
               print(num)
               primes.append(num)
divided = []
factors = []

'''Seek the prime factors of a given number. Divide the number with the prime until modulus is zero, move
onto the next prime and gather the prime factors of the number. Print the prime factors.'''
for i in primes:
    if len(divided) < 1:
        if number % i==0:
            left = int(number/i)
            divided.append(left)
            factors.append(i)
        else:
            continue
    else:
        for u in divided:
            if u%i==0:
                left = int(u/i)
                divided.append(left)
                factors.append(i)
            else:
                break
print(factors)
