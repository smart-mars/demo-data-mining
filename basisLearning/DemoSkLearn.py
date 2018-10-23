# -*- coding: utf-8 -*-
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
print digits.data
print digits.target
print '*' * 70 + '\n'

print '''训练和预测'''
# 选择模型参数
clf = svm.SVC(gamma=0.0001, C=100)
# 进行训练
clf.fit(digits.data[:-1], digits.target[:-1])
# 进行预测
print digits.data[-1].reshape(1, -1)
print clf.predict(digits.data[-1].reshape(1, -1))
print '*' * 70 + '\n'
