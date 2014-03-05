#!/usr/bin/env python
# -*-coding: utf-8 -*-

#求绝对值
print abs(-1)
#比较
print cmp(1,2)
#数据类型转换
print int(123.45)
print float('123.12')
print str(1.2)
print unicode(122)
print bool(1)
print bool('')

#自定义函数
def my_fun(x,y):
	return x+y
#调用函数
print my_fun(102,2)

#空函数
def nop():
	pass

#pass为占位符
#有时候缺少代码又没用pass代码会出错
age = 20
if age >= 18:
	pass

#参数个数不符时，Python会自动抛出TypeError
#自定义函数对数据类型检查isinstance函数
def fun(x):
	if isinstance(x,(int,float)):
		if x < 0:
			return -x
	else:
		raise TypeError('bad')
fun(-1)
#默认参数
def power(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print power(2)
print power(2,4)
#默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()
print add_end()
#可变参数,允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def sum(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

print sum(0,2)
nums = [1,2,3,4]
print sum(*nums)

#关键字参数,允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**other):
	print 'name:',name,'age:',age,'other:',other

person('jack',30,city='shanghai')

#参数组合,在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **other):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'other =', other
func(1, 2, 3, 'a', 'b', x=99)
#递归
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
print fact(9)
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
# fact(1000)

#尾递归优,指在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact_iter(product,count,max):
	if count > max:
		return product
	return fact_iter(product * count,count + 1,max)

def fact(n):
	return fact_iter(1,1,n);

print fact(100)