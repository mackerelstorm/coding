import time

for hour in range(24):
    for minutt in range(60):
        for sekund in range(60):
            print(f"{hour}:{minutt}:{sekund}")
            time.sleep(1)