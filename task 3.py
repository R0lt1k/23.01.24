import time
import random
import threading

def write_random_number(filename):
    random_number = random.randint(1, 100)
    time.sleep(1)
    with open(filename, 'w') as f:
        f.write(str(random_number))

def main():
    start_time = time.time()
    threads = []

    for i in range(1, 1001):
        filename = f"random_number_{i}.txt"
        t = threading.Thread(target=write_random_number, args=(filename,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")
    
main()
