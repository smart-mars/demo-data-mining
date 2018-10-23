# -*- coding: utf-8 -*-
# 使用 ID3 算法进行分类
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC, export_graphviz

data = pd.read_csv('data/7/titanic_data.csv', encoding='UTF-8')

# 舍弃 ID 列，不适合作为特征
data.drop(['PassengerId'], axis=1, inplace=True)

# 数据是类别标签，将其转换为数，用1表示男，0表示女
data.loc[data['Sex'] == 'male', 'Sex'] = 1
data.loc[data['Sex'] == 'female', 'Sex'] = 0
data.fillna(int(data.Age.mean()), inplace=True)
# 查看数据
data.head(5)

X = data.iloc[:, 1:3]  # 为了方便展示，未考虑年龄（最后一列）
y = data.iloc[:, 0]

dtc = DTC(criterion='entropy')  # 初始化决策树对象，基于信息熵
dtc.fit(X, y)
print '输出准确率：', dtc.score(X, y)

# 可视化决策树，导出结果是一个 dot 文件，需要安装 Graphviz 才能转换为 .pdf 或 .png 格式
with open('tmp/tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=X.columns, out_file=f)
