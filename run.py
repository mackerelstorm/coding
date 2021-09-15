import os
import time

count = 0


while 1>0:
    if count > 0:
        time.sleep(1.5)
    print("What script do you want to run? \n 1: ax²+bx+c solver \n 2: Yield Calculator \n 3: Fibonacci Finder \n 4: Password Generator")
    print("Type q to quit")
    type_check = input(": ")
    if type_check == "q" or type_check == "quit":
        exit()

    try:
        run_script = int(type_check)
    except ValueError:
        print("You typed in something invalid ")
        time.sleep(0.8)
        continue

    while run_script > 4 or run_script < 1 :
        print(f"{run_script} is not a script")
        run_script = int(input(": "))


    if run_script == 1:
        script_name = 'abc.py'
    elif run_script == 2:
        script_name = "avkastning.py"
    elif run_script == 3:
        script_name = "fibonacci.py"
    elif run_script == 4:
        script_name = "password_generator.py"

    os.system("python " + script_name)
    count += 1