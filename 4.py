'''Largest palindromic number made up of 2 3-digit numbers.'''

lower = 100
upper = 999
largest = 0
mul1 = 0
mul2 = 0
'''Two loops, multiply values and check if their product is the same as original and reversed.'''
for i in range(lower,upper+1):

    for j in range(lower,upper+1):
        multiply = i*j
        string = str(multiply)
        reverse = string[::-1]
        if reverse == string and multiply > largest:
            largest = multiply
            mul1 = i
            mul2 = j
print(f"The largest palindrome number between {lower} and {upper} is {largest} from the factors {mul1} and {mul2}.")
