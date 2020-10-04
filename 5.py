'''Smallest number evenly divisible by numbers from 1 t0 20.'''
'''It is 232792560.'''
count = 0
lower = 21
upper = 300000000
for i in range(lower,upper):
    count = 0
    for j in range(1,21):
        if i%j != 0:
            break
        elif i%j == 0:
            count +=1

    if count == 20:
        print(f"{i} is the smallest number evenly divisible by numbers from 1 to 20.")
        break
