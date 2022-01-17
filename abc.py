# This is an ABC formula solver for ax^2+bx+c
import math
def func_input():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    return a,b,c


def convert(a,b,c):
    b_minus = b - (2*b)
    root = (pow (b, 2) - (4 * a * c))
    return b_minus, root


def complex_result(a,b_minus,root):
    root = math.sqrt(abs(root)) * complex(0, 1)
    complexplus_result = ((b_minus + root) / (2*a))
    complexminus_result = ((b_minus - root) / (2*a))
    print(complexplus_result, complexminus_result)
    exit()


def real_result(a,b_minus,root):
    plus_result = ((b_minus + math.sqrt(root)) / (2*a))
    minus_result = ((b_minus - math.sqrt(root)) / (2*a))

    if plus_result >=0:
        plus_factorconvert = f"(x-{plus_result})"
    else:
        plus_print = plus_result - 2*plus_result
        plus_factorconvert = f"(x+{plus_print:.2f})"
    if minus_result >=0:
        minus_factorconvert = f"(x-{minus_result})"
    else:
        minus_print = minus_result - 2*minus_result
        minus_factorconvert = f"(x+{minus_print:.2f})"
    
    print ((f"{plus_result:.2f}"), (f"{plus_factorconvert}"))
    print ((f"{minus_result:.2f}"), (f"{minus_factorconvert}"))


def main():
    inputs=func_input()
    a,b,c = inputs[0],inputs[1],inputs[2]
    converted_values=convert(a,b,c)
    b_minus,root=converted_values[0],converted_values[1]
    if root < 0:
        complex_result(a,b_minus,root)
    else:
        real_result(a,b_minus,root)
    
    
main()

