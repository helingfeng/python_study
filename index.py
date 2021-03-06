#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello %s !' % 'helingfeng')

print('''line1
line2
line3
''')

s = 1.2345

print('s = %.2f' % s)

print(f's = {s:.3f}')

print('中文'.encode('gb2312'))
print('中文'.encode('utf8'))

# birth = input('birth: ')
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

student = {'username': 'h', 'class': '2020'}

print(student.get('username'))
print(student.get('class'))

print(student.get('age', -1))

s = set([4, 3])
print(s)

s.remove(4)
print(s)

s.add('abc')
print(s)

test = {'array': (1, [2, 3])}
print(test['array'][1])

# >>> int('123')
# 123
# >>> int(12.34)
# 12
# >>> float('12.34')
# 12.34
# >>> str(1.23)
# '1.23'
# >>> str(100)
# '100'
# >>> bool(1)
# True
# >>> bool('')
# False

def my_max(x, y):
    if x > y:
        return x
    else:
        return y

print(my_max(12, 9))
print(my_max(8, 16))