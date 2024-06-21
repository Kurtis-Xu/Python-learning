# 类型转换

a, b, c = 1, True, 'abc'

print(bool(a))
print(str(a))
print(int(b))
print(int(False))  # True = 1, False = 0
print(str(b))
# print(int(c))
# print(int('abc123'))
print(int('123'))  # 只有纯数字字符串可以转为 int
print(bool(c))

print(float('123.456'))
print(float(True))  # 1.0
print(float(False))  # 0.0

print('b1', bool(1))  # True
print('b2', bool(0))  # False
print('b3', bool(' '))  # True
print('b4', bool(''))  # False
print('b5', bool(str()))  # False
print('b6', bool(1.0))  # True
print('b7', bool(0.0))  # False

print(int('10000', 2))
print(int('20', 8))
print(int('16', 10))
print(int('10', 16))
