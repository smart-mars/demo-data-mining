# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.linear_model import LogisticRegression, RandomizedLogisticRegression
from sklearn.model_selection import train_test_split

# 导入数据观察
data = pd.read_csv('data/7/LogisticRegression.csv', encoding='utf-8')
print data.head(5)

# 将类别变量进行独热编码（one-hot encoding）
data_dum = pd.get_dummies(data, prefix='rank', columns=['rank'], drop_first=True)
print data_dum.tail(5)

# 切分训练数据集和测试集
X_train, X_test, y_train, y_test = train_test_split(data_dum.ix[:, 1:], data_dum.ix[:, 0],
                                                    test_size=.1, random_state=520)

# 建立LR模型
lr = LogisticRegression()
# 用处理好的数据集训练模型
lr.fit(X_train, y_train)
print '逻辑回归的准确率为：{0:.2f}%'.format(lr.score(X_test, y_test) * 100)
