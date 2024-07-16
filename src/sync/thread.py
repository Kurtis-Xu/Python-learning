from threading import Thread

def fun():
    for i in range(1000):
        print('子线程', i)

if __name__ == '__main__':
    t = Thread(target=fun)

    # t.run()  # 与 Java 相同，线程有 run 方法和 start 方法，开启新线程使用 start 方法
    t.start()
    for i in range(1000):
        print('主线程', i)
