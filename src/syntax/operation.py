# 运算符

a, b, c, d = 1, 2, 3, 4

print('t1', a + b)
print('t2', a - b)
print('t3', a * b)
print('t4', a / b)
print('t5', c % 2)
# 以下两种运算符优先级较高
print('t6', c ** b)  # 幂运算
print('t7', c // b)  # 取整，结果舍弃小数位

# 赋值运算符
e = 5
e **= b
print('e', e)

# 比较运算符
print(a == b)
print('hello' > 'world')  # 字符串依次比较字符编码
print(ord('好'))  # 获取字符编码值

# 逻辑运算符
print(a and b)
print(a or b)
print(not a)

print('' and 'hi')
print('' or 'hi')

# 位运算符
print(int('101', 2) and int('101', 2))
