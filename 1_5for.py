#!/usr/bin/env python
# -*-coding: utf-8 -*-

#for...in循环，吧list或tuple中的元素迭代出来
print '---for...in---'
names = ['Li','Zoe','Jack']
for name in names:
	print name
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
#range(n)用于生成从0到不大于n的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print sum
#while循环，只要条件满足，就不断循环，条件不满足时退出循环
print '---while---'
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum