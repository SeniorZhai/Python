#!/usr/bin/env python
# -*-coding: utf-8 -*-

# 第一行注释为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行是为了告诉Python解释器，按照UTF-8编码读取源码，否在源码中文输出科恩能够会乱码

# 字母和数值的切换
ord('A')
chr(65)

#对Unicode的支持，以u'...'表示
print u'中文'
u'中文'

#把u'...'转换成UTF-8编码的'XXX'用encode('utf-8')方法
u'ABC'.encode('utf-8')
u'中文'.encode('utf-8')

#len()函数可以返回字符串的长度：
len(u'ABC')
len('ABC')
len(u'中文')
len('\xe4\xb8\xad\xe6\x96\x87')
#把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法
'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#在Python 3.x版本中，把'xxx'和u'xxx'统一成Unicode编码，即写不写前缀u都是一样的，而以字节形式表示的字符串则必须加上b前缀：b'xxx'。