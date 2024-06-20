try:
    prlnt()
except Exception as e:
    print('error:', e)
    pass
else:
    print('fun success')
finally:
    print('finally')

try:
    print('do')
except Exception as e:
    pass
else:
    print('print success')
finally:
    print('finally')

raise Exception('抛出异常')
