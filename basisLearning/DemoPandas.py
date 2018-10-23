# -*- coding: utf-8 -*-
import pandas as pd

print '''DataFrame(数据框)'''
data = {
    'id': ['Jack', 'Sarah', 'Mike'],
    'age': [18, 35, 20],
    'cash': [10.53, 500.7, 13.6]
}
df = pd.DataFrame(data)
print df
print '*' * 70 + '\n'
print '''DataFrame(数据框)声明列与索引'''
df1 = pd.DataFrame(data, index=['one', 'two', 'three'], columns=['id', 'age', 'cash'])
print df1
print '*' * 70 + '\n'
print '''DataFrame(数据框)只取ID列'''
print df1['id']
print '*' * 70 + '\n'

print '''Series(系列)'''
s = pd.Series({'a': 4, 'b': 9, 'c': 6}, name='number')
print s
print s[0]
print s['a']
print s[:2]
