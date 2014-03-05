#!/usr/bin/env python
# -*-coding: utf-8 -*-

#list初始化
colors = ['black','blue','red'];
#打印list
print colors;
#测长
print len(colors)
#根据索引查找元素
print colors[0]
print colors[1]
print colors[len(colors) - 1]
print colors[-1]
print colors[-2]
print colors[-len(colors)]
#在末尾添加元素
colors.append('green')
print colors
#在指定位置添加元素
colors.insert(1, 'oranger')
print colors
#删除末尾元素
colors.pop()
print colors
#删除指定元素
colors.pop(1)
print colors
#替换指定位置元素
colors[1] = 'green'
print colors
#list的嵌套
p = ['java','oc','python']
s = ['c','c++',p]
print s

a = ['c','a','b']
#排序
a.sort();
print a
#替换
a.replace('a','A')
print a
