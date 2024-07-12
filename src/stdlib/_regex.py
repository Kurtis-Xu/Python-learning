# Regular Expression
import re

# .       匹配换行符外的任意字符
# \w      匹配字母、数字、下划线
# \s      匹配任意空白字符
# \d      匹配数字
# \n      匹配换行符
# \t      匹配制表符
#
# ^       匹配字符串开头
# $       匹配字符串结尾
#
# \W      匹配非字母、数字、下划线
# \D      匹配非数字
# \S      匹配非空白字符
# a|b     匹配字符a或字符b
# ()      匹配括号中的表达式，或表示一个组
# [...]   匹配字符组中的字符
# [^...]  匹配除字符组中字符外的所有字符

# 量词：控制元字符重复匹配次数
# *       重复零次或多次
# +       重复一次或多次
# ?       重复零次或一次
# {n}     重复n次
# {n,}    重复n次或更多次
# {n,m}   重复n次到m次

# .*  贪婪匹配
# .*? 惰性匹配

print(re.match('hello', 'hello world'))

print(re.match('\\d+', '12345'))
print(re.match(r'\d+', '12345'))

s = '客服一：10086，客服二：10000'

print('findAll', re.findall(r'\d+', s))
print('finditr', re.finditer(r'\d+', s))  # 迭代器效率比列表高
for v in re.finditer(r'\d+', s): print('iter', v.group())
print('search', re.search(r'\d+', s).group())
print('match', re.match(r'\d+', '123 一二三').group())  # match 默认从头匹配（等于自动在正则前面加上了 ^）

reg = re.compile(r'\d+')
print('preload', reg)  # 预加载

s = '''
<div class="jay"><span id="1">周杰伦</span></div>
<div class="jj"><span id="2">宋轶</span></div>
<div class="jolin"><span id="3">大聪明</span></div>
<div class="sylar"><span id="4">范思哲</span></div>
<div class="tory"><span id="5">阿巴阿巴</span></div>
'''

reg = re.compile(r'<div class="(?P<en>.*?)"><span id="(?P<id>\d+)">(?P<name>.*?)</span></div>', re.S)  # re.S 让 . 能匹配换行符
# (?P<分组名称>表达式)

for v in reg.finditer(s): print(v.group('id'), v.group('en', 'name'))  # 通过分组获取内容
