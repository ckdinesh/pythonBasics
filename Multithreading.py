
import time
import threading

numbers = [ 1,2 ,3,4, 5]

def cal_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Square :", str(n*n))

def cal_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Cube :", str(n*n*n))

t = time.time()
t1 = threading.Thread(target=cal_square, args=(numbers,))
t2 = threading.Thread(target=cal_cube, args=(numbers,))
t1.start()
t2.start()

# t1.join()
# t2.join()

# print(cal_square(numbers))
# print(cal_cube(numbers))
print("Time taken for execution : ", ((time.time() - t) * 1000))
