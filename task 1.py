import time
import random
import threading

def write_random_number(file):
    random_number = random.randint(1, 100)
    time.sleep(1)
    with open(file, 'w') as file:
        file.write(str(random_number))

file = 'random_number.txt'
write_random_number(file)
