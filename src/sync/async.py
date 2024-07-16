# 协程
import asyncio
import time

async def fun1():
    print('Hello world!')
    await asyncio.sleep(3)
    print('Hello world!')

async def fun2():
    print('Hello C!')
    await asyncio.sleep(2)
    print('Hello C!')

async def fun3():
    print('Hello python!')
    await asyncio.sleep(4)
    print('Hello python!')

if __name__ == '__main__':
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()

    tasks = [f1, f2, f3]

    t1 = time.time()
    # 一次性启动多个任务（协程）
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()

    print(t2-t1)
