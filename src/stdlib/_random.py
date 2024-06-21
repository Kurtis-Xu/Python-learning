import random

# 随机小数
a = random.random()
print(a)

a = random.randint(1, 10)
print(a)

ls = [1, 2, 3, 4, 5]
print(random.choice(ls))

s = ''
for i in range(4):
    s += str(random.randint(0, 9))
print(f'验证码：{s}')
