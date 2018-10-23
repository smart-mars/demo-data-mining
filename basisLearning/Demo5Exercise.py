# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

os.chdir("Q:\\test")

data = pd.read_csv("data.csv")
# data = pd.DataFrame(pd.read_csv("data.csv"))
# 原始数据
print data
print '*' * 70 + '\n'

# 判断第一列是否有缺失值：如果有，则补全
# def defaultValueOfColoum(x):
#     if (pd.isnull(x)):
#         return 40
#     else:
#         return x
#
#
# vec_defaultValueOfColoum = np.vectorize(defaultValueOfColoum)

data['aaa'] = pd.isnull(data['Id'])
cleanedData = 0

# Id 列赋默认值
for isNa in pd.isnull(data['Id']):
    if (isNa):
        # Id 列设置默认值
        cleanedData = data.fillna({'Id': -1})
        break
print cleanedData
print '*' * 70 + '\n'

# Id列相等的，去掉重复行
for isDup in cleanedData.duplicated('Id'):
    if (isDup):
        cleanedData = cleanedData.drop_duplicates('Id')
        break
print cleanedData
print '*' * 70 + '\n'

# 各科平均分
columnAvg = cleanedData.mean()
dataAvg = 0

# 方式一
# dataAvg = cleanedData.append({
#     'Id': '平均分',
#     'Chinese': columnAvg[1],
#     'Math': columnAvg[2],
#     'English': columnAvg[3],
#     'aaa': False}, ignore_index=True)
# 方式二
dataAvg = cleanedData.append(columnAvg, ignore_index=True)
print dataAvg
print '*' * 70 + '\n'

# 平均分最高记录
print cleanedData.mean(axis=1)

print '*' * 70 + '\n'

print cleanedData[['Chinese', 'Math', 'English']].mean(axis=1).max()
print '*' * 70 + '\n'

print cleanedData[(cleanedData['Chinese'] >= 60) & (cleanedData['Math'] >= 60) & (cleanedData['English'] >= 60)].count()
