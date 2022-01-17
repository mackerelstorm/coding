def add_sum(*args):
    sum_ = 0
    for i in args:
        sum_ += i 
    return sum_

sum_ = add_sum(5, 4, 3, 7)
print(sum_)