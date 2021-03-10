#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hello_module
from functools import reduce
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
    n1 = -b + math.sqrt(b * b - 4 * a * c)
    n2 = -b - math.sqrt(b * b - 4 * a * c)
    m = 2 * a
    return n1 / m, n2 / m


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


def findMinAndMax(L):
    if len(L) <= 0:
        return (None, None)
    min = max = L[0]
    if len(L) == 1:
        return (min, max)
    for num in L[1:]:
        if num > max:
            max = num
        if num < min:
            min = num
    return (min, max)


findMinAndMax([7, 1, 3, 9, 5])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if isinstance(word, str)]
print(L2)


def triangles():
    L = [1]
    yield L

    n = 2
    while True:
        size = len(L)
        L1 = []
        for i, num in enumerate(L):
            if i == 0:
                L1.append(1)
            else:
                L1.append(L[i] + L[i - 1])
            if i == (size - 1):
                L1.append(1)
        L = L1
        yield L


gle = triangles()
print(next(gle))
print(next(gle))
print(next(gle))
print(next(gle))
print(next(gle))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def createCounter():
    index = 0

    def counter():
        nonlocal index
        index = index + 1
        return index

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5

hello_module.test()
print(hello_module.__doc__)


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


class Student(object):
    count = 0

    def __init__(self, name):
        Student.count = Student.count + 1
        self.name = name


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

try:
    # foo()
    pass
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

import json

s_obj = dict(name='小明', age=20, hobbies=list(['football', 'basketball']))
sj = json.dumps(s_obj, ensure_ascii=False)

print('json => ' + sj)

r_obj = json.loads(sj)
print('obj => ', r_obj)

