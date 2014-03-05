#!/usr/bin/env python
# -*-coding: utf-8 -*-

#元组，一种有序列表，一旦初始化就不能修改
colors = ('black','blue','red')
print colors;
t = (1,2)
print t
#空的元组
t = ()
print t
#定义只有一个元素的元组，不能直接用t=(1)
t = (1,)
#元素不可变，指定是地址
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t