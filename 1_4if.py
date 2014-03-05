#!/usr/bin/env python
# -*-coding: utf-8 -*-

print'-----if-----'
age = 20
if age >= 18:
    print u'你成年了'
else:
    print u'你未成年'
print'-----elif-----'
age = 12
if age >= 18:
    print u'你成年了'
elif age >=12:
	print u'你还小'
else:
    print u'你未成年'
#只要是非零数值、非空字符串、非空list等就判断为True,否则为False
print'-----x-----'
x = 1
if x:
	print 'true'