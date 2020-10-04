multiples = []
num_range = int(input("Give a number range of whose 3 or 5 divisible sum you want to find.\n>"))
'''Find the numbers of 3 or 5 divisible numbers under user inputted range and sum their total.'''
for i in range(num_range):
    if i%3==0 or i%5==0:
        #print(i)
        multiples.append(i)
        #print(i)
sum = 0
for i in multiples:
    sum += i
print(f"The sum of 3 and 5 multiples below {num_range} is {sum}.")
