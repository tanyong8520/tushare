#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 统计模型结果
from sklearn.metrics import classification_report
# 数据预处理
from sklearn.preprocessing import StandardScaler
# 数据分割
from sklearn.model_selection import train_test_split
# 手写体数据源
from sklearn.datasets import load_digits

# 线性分类器
def logisticRegressionTest():
    from sklearn.linear_model import LogisticRegression
    from sklearn.linear_model import SGDRegressor

def svmRegressionTest():
    # 线性假设的支持向量机分类器
    from sklearn.svm import LinearSVC
    ss = StandardScaler()
    digits = load_digits()
    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25 , random_state=33)
    # 数据标准化
    X_train = ss.fit_transform(X_train)
    X_test = ss.fit_transform(X_test)

    # 初始化
    lsvc = LinearSVC()
    lsvc.fit(X_train, Y_train)
    y_predict = lsvc.predict(X_test)
    print  'The Accuracy of Linear SVC is ', lsvc.score(X_test,Y_test)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))