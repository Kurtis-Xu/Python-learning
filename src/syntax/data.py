# 数据结构

# 列表
l1 = []
l2 = list()
l3 = ['1', 2, True]
l4 = list('123')  # list() 的参数必须是一个可遍历的对象
# l = list(1)
print(l4)

# 列表加法与乘法
print('列表加法', l3 + l4)
print('列表乘法', l3 * 3)
print('-' * 30)

l3 += 'abc'
l3.append('def')
l3.extend('ghi')
l3.insert(3, 'ins')  # 插入元素
print(l3)
l3.pop(3)  # 删除元素
print('pop', l3)
l3.remove('def')
print('remove', l3)

print([1, 2, 3] < [3, 2, 1])  # 列表比较的是第一个元素
s = 'abc'
print('in', 'a' in s)  # 是否存在元素 'a'
print(len(s))
print(min(s))
print(max(s))

# 列表遍历
for i in s: print('for list', i)

# 枚举
enum = enumerate(s)
print(enum)
print(type(enum))
for i, v in enum: print('for enum', i, v)  # 枚举

# 元组
# 相当于常量形式列表，元素不可改变
t1 = ()
t2 = tuple()
t3 = (1)
print(type(t3))
t3 = (1,)  # 只有一个元素时需要加一个逗号表示该变量是个元组
print(type(t3))
t4 = ('1', 2, True)

t = tuple('hello')
print(t)
t = tuple([1, 2, 3])
print(t)
print(type(list(t)), list(t))
print(type(str(t)), str(t))

print(t[0])
print(t[0:1])
print(t[::-1])
print(1 in t)  # 是否存在元素 1
print('1' in t)  # False
print(max(t))
print(t + (4, 5, 6))
print(t * 3)
# t[0] = 2  # 报错，元组中的元素不可替换

# 字典
d1 = {}
d2 = dict()
d3 = {
    'name': '小明',
    'age': 18,
    'gender': True,
    1: 'test1',
    True: 'test2',  # 该键值对无效，会覆盖上一个的值
    2: 'test3'
}
print(d3)
# 查询是否有某个 key
print(1 in d3)
print('小明' in d3)

d = d3
del d[1]
print(d)

for k, v in d.items():
    print('dict item', k, v)

for k in d.keys():
    print('dict key', k)

for v in d.values():
    print('dict value', v)

# 集合
# 无序不重复的列表
s1 = set()
s2 = {1, 2, 3}  # 大括号默认是字典，内容不是 k-v 形式的话就是 set
print(type(s2))

print(set('12345123'))
