from multiprocessing import Process

def square(x):
    print(x**2)


def sum(a,b):
    print(a+b)

if __name__ =='__main__':
    t1 = Process(target=square,args = (5,))
    t1.start()

    t2 = Process(target=sum , args = (5,6))
    t2.start()