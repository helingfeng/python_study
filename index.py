#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
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


def quadratic(a, b, c):
    n1 = -b + math.sqrt(b*b - 4*a*c)
    n2 = -b - math.sqrt(b*b - 4*a*c)
    m = 2*a
    return n1/m, n2/m


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


def add_test(L=1):
    L = L + 1
    return L


print(add_test())
print(add_test())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2, 3))

num = [1, 2, 3]
print(calc(*num))

def calc_test(t, numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n + t
    return sum

print(calc_test(1, [1, 2, 3]))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

def person_test(name, age, kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
person_test('Jack', 24, extra)

def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, 3, city='Beijing', job='Engineer')