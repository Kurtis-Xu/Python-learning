# Python 可以直接赋值变量，不需要定义
a, b, c = 1, 2, 3

print(type(a))
a = '123'
print(type(a))  # Python 没有严格的类型要求，同一个变量可以赋值不同类型的数据

# print(d)  # 未赋值的变量不可以使用，会报错

A = '123'  # Python 没有常量，一般约定大写变量名表示该变量不可修改

s = '%d 年 %02d 月 %02d' % (2024, 6, 18)  # 格式化字符串

# 布尔值只有两种值
t, f = True, False

# 空字符串
s1 = ''
s2 = str()

s = '0123456789ABCDEF'
print(s[0], s[1], s[-1])  # 负数索引表示倒数，-1 表示倒数第一个字符
print(s[0:2])  # 带冒号表示使用区间索引，相当于切片
print(s[:2])
print(s[2:])
print(s[0:9:2])  # 第三个数字表示间隔
# string[起始索引（包含）:结束索引（不包含）:步长]
# 起始索引默认为0，可省略；结束索引默认为字符串长度值，可省略；步长默认为1，可省略，第二个冒号也可省略
print(s[:-1])
print(s[::-1])

# 使用 id(arg) 可以获取变量地址
print(id(a))
print(id(b))
print(id(c))

del s  # 删除变量
# print(s)  # not defined
ls = ['a', 'b', 'c']
del ls[1]
print(ls)

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