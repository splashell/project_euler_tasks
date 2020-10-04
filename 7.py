'''What is the nth prime number?'''

nth_prime = 10001
prime = 0
lower = 1
upper = 10000000
count = 0
'''The first loop is the number in a given range, second loop calculates modulus between the range 2
and the given number-1 to determine if it is not a prime number.'''

for num in range(lower,upper+1):
    if num>1 and count < nth_prime:
        for j in range(2,num):
            if (num % j) == 0:
                break
        else:
            print(num, count+1)
            count += 1
            prime = num

print(f"The {nth_prime}. prime number is {prime}.")
