#!/usr/bin/env python
# -*-coding: utf-8 -*-

#set是一组key的集合，不储存value
#这里的[1,2,3]不是一个list
s = set([1,2,3])
print s
#重复的元素会被过滤掉
s = set([1,1,1,1,1,2,3,4,2])
print s
#添加元素
s.add(0)
print s
s.add(1)
print s
#删除元素
s.remove(1)
print s
#交集与并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2
print '------------'
