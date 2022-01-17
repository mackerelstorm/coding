import time
upper_limit = int(input("Hvor mange primtall skal du regne "))
num=1
odd_list=[]
count = 2
start_time = time.time()
while count < upper_limit:
    if num == 1:
        print(num)
        num+=1
        print(num)
        num+=1
    else:
        num+=2
    for i in odd_list:
        if num % i == 0:
            break
    else:
        print(num)
        count+=1
    
    odd_list.append(num)

print(f"Took {time.time()-start_time} seconds")