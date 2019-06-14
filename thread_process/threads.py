import threading
import os

def square(x):
    print(x**2)

    print("ID of current running task1:{}".format(os.getpid()))

def sum(a,b):
    print(a+b)
    print("ID of current running task2:{}".format(os.getpid()))

if __name__ =='__main__':
    t1 = threading.Thread(target=square,args = (5,))
    t1.start()

    t2 = threading.Thread(target=sum , args = (5,6))
    t2.start()