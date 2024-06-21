import os

f = open('read.txt', encoding='utf-8')
# ctx = f.read()
# print(ctx)
i = 1
while True:
    s = f.readline()
    if not s: break
    print(i, s, end='')
    i += 1
f.close()
