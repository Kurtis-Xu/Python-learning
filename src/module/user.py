# 第一种导入方法
# import lib
#
# lib.fun('do sth')

# 第二种导入方法
# from lib import *  # 全部导入
from lib import fun

fun('do sth')

from lib import fun as f

f('do f')
