# -*- coding: utf-8 -*-

print '''列表用作堆栈'''
stack = [7, 8, 9]
stack.append(10)
stack.append(11)
print stack
num = stack.pop()
print '取出值：%s' % num
print stack
