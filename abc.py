# This is an ABC formula solver for ax^2+bx+c
import math
a = input("A: ")
b = input("B: ")
c = input("C: ")
b_minus = int(b) - (2*int(b))
plus_result = (b_minus + math.sqrt(pow(int(b), 2) - (4 * int(a) * int(c)))) / (2 * int(a))
minus_result = (b_minus - math.sqrt(pow(int(b), 2) - (4 * int(a) * int(c)))) / (2 * int(a))

if plus_result >=0:
    plus_factorconvert = "(x-{})".format(int(plus_result))
else:
    plus_print = plus_result - 2*plus_result
    plus_factorconvert = "(x+{})".format(int(plus_print))
if minus_result >=0:
    minus_factorconvert = "(x-{})".format(int(minus_result))
else:
    minus_print = minus_result - 2*minus_result
    minus_factorconvert = "(x+{})".format(int(minus_print))


print (int(plus_result), (plus_factorconvert))
print (int(minus_result), (minus_factorconvert))
