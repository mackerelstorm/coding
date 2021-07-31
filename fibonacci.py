#This is a calculator that displays Fibonacci numbers up to a specified amount

top = int(input("What is the upper limit you want to calculate to?: "))
value = [0]
first, second = 0, 1

while top > value[-1]:
    if value == [0]:
        value.append(1)
    else:
        addition = value[first] + value[second]
        value.append(addition)
        first += 1
        second += 1
if top >= value[-1]:
    print (value)
else:
    print (value[:-1])
