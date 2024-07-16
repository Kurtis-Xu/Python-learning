# 进程
from multiprocessing import Process

def fun():
    for i in range(1000):
        print('子进程', i)

if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    for j in range(1000):
        print('主进程', j)
