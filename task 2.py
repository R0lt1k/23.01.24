import time
import random
import threading

def write_random_number(file):
    random_number = random.randint(1, 100)
    time.sleep(1)
    with open(file, 'w') as file:
        file.write(str(random_number))

start = time.time()
for i in range(1,1000):
    file = f'random_number{i}.txt'
    write_random_number(file)
end = time.time()
print("Время :", end - start)
