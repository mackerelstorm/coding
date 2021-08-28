# This is an ABC formula solver for ax^2+bx+c
import math
a = input("A: ")
b = input("B: ")
c = input("C: ")
b_minus = int(b) - (2*int(b))
four_ac = (pow(int(b), 2) - (4 * int(a) * int(c)))
if four_ac < 0:
    four_ac = math.sqrt(abs(four_ac)) * complex(0, 1)
    complexplus_result = ((b_minus + four_ac) / (2*int(a)))
    complexminus_result = ((b_minus - four_ac) / (2*int(a)))
    print(complexplus_result, complexminus_result)
    exit()
plus_result = ((b_minus + math.sqrt(four_ac)) / (2*int(a)))
minus_result = ((b_minus - math.sqrt(four_ac)) / (2*int(a)))

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