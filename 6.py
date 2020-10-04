'''The difference of the sum of the squares and square of the sums of the
first 100 natural numbers.'''

lower = 1
upper = 100
square_of_sums = 0
sum_of_squares = 0
for i in range(lower, upper+1):
    square_of_sums += i
    sum_of_squares += i**2
square_of_sums = square_of_sums**2
difference = square_of_sums - sum_of_squares

print(f"The difference between the square of sums and sums of square for the first {upper} natural numbers is {difference}.")
