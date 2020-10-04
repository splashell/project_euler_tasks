print("Find the sum of fibonacci members below 4 000 000.")

fib = [1, 2]
num_range = 88888
for i in range(num_range):
    if i < len(fib):
        continue
    first = fib[i-2]
    second = fib[i-1]
    fib_num = first + second
    fib.append(fib_num)
fib_sum = 0
for i in fib:
    print(i)
    if fib_sum + i > 4000000:
        break
    fib_sum += i
print(f"The sum of the fibonacci members below 4000000 is {fib_sum}.")
