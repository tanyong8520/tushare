#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 手写体数据源
from sklearn.datasets import load_digits
# 数据分割
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA

from sklearn.svm import LinearSVC
# 统计模型结果
from sklearn.metrics import classification_report

#降维测试

def PCATest():
    digits = load_digits()

    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)

    svc = LinearSVC()
    svc.fit(X_train, Y_train)
    y_predict = svc.predict(X_test)


    pca_svc = LinearSVC()
    estimator = PCA(n_components = 20)
    X_train_pca = estimator.fit_transform(X_train)
    X_test_pca = estimator.transform(X_test)
    pca_svc.fit(X_train_pca, Y_train)
    y_predict_pca = pca_svc.predict(X_test_pca)

    print  'The Accuracy of Linear SVC is ', svc.score(X_test,Y_test)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))

    print  'The Accuracy of Linear SVC before PCA is ', svc.score(X_test,y_predict_pca)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))


PCATest()