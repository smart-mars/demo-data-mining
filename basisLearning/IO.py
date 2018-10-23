# -*- coding: utf-8 -*-

import os

print '''改工作目录'''
os.chdir("Q:\\test")
print os.getcwd()

print '''读出文件'''
data = []
fr = open('data.txt', mode='r')
for line in fr.readlines():
    line = line.strip()
    data_line = line.split("\t")
    data.append(data_line)
print data[0]
fr.close()

print '''写文件'''
fw = open('output.txt', mode='w+')
data = [['1', '2'], ['3', '4'], ['5', '6']]
line1 = ','.join(data[0])
fw.write(line1 + '\n')
line2 = ','.join(data[1])
fw.write(line2 + '\n')
# 使用 print >> fw
data = [[11, 12], [13, 14]]
for line in data:
    print >> fw, str(line[0]) + ',' + str(line[1]) + '\n'
fw.close()
