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
# 新闻分类数据，大数据集
from sklearn.datasets import fetch_20newsgroups


from sklearn.datasets import load_boston

#分类测试

# 随机梯度下降分类器
def SGDClassifierTest():
    from sklearn.linear_model import SGDClassifier
    ss = StandardScaler()
    digits = load_digits()

    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
    X_train = ss.fit_transform(X_train)
    X_test = ss.fit_transform(X_test)

    sgdc = SGDClassifier()
    sgdc.fit(X_train, Y_train)
    sgdc_y_predict =sgdc.predict(X_test)
    print  'The Accuracy of SGD is ', sgdc.score(X_test, Y_test)
    print  classification_report(Y_test, sgdc_y_predict, target_names=digits.target_names.astype(str))



# 线性回归
def logisticRegressionTest():
    from sklearn.linear_model import LogisticRegression
    ss = StandardScaler()
    digits = load_digits()
    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
    lr = LogisticRegression()
    lr.fit(X_train, Y_train)
    lr_y_predict = lr.predict(X_test)
    print  'The Accuracy of logistic is ', lr.score(X_test, Y_test)
    print  classification_report(Y_test, lr_y_predict, target_names=digits.target_names.astype(str))


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


# 朴素贝叶斯，主要用于文本分析
def nultinomialNBTest():
    news = fetch_20newsgroups(subset= 'all')
    X_train, X_test, Y_train, Y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)

    #文本特征抽取
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer()
    X_train = vec.fit_transform(X_train)
    X_test = vec.transform(X_test)

    from sklearn.naive_bayes import MultinomialNB
    mnb = MultinomialNB()
    mnb.fit(X_train, Y_train)
    y_predict = mnb.predict(X_test)

    print  'The Accuracy of Linear MNB is ', mnb.score(X_test, Y_test)
    print  classification_report(Y_test, y_predict, target_names=news.target_names)

#K邻近分类器
def KNeighborsClassifiertest():
    from sklearn.neighbors import KNeighborsClassifier
    ss = StandardScaler()
    digits = load_digits()
    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
    # 数据标准化
    X_train = ss.fit_transform(X_train)
    X_test = ss.fit_transform(X_test)

    knc = KNeighborsClassifier()
    knc.fit(X_train, Y_train)
    y_predict = knc.predict(X_test)

    print  'The Accuracy of Linear KNC is ', knc.score(X_test, Y_test)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))

#决策树分类器  0.848888888889
def DecisionTreeClassifierTest():
    from sklearn.tree import DecisionTreeClassifier
    ss = StandardScaler()
    digits = load_digits()
    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
    # 数据标准化
    # X_train = ss.fit_transform(X_train)
    # X_test = ss.fit_transform(X_test)

    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, Y_train)
    y_predict = dtc.predict(X_test)

    print  'The Accuracy of Linear DTC is ', dtc.score(X_test, Y_test)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))


def treeTest():
    from sklearn.ensemble import RandomForestClassifier #随机森林  0.928888888889
    from sklearn.ensemble import GradientBoostingClassifier #梯度提升决策树 0.951111111111

    digits = load_digits()
    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)

    rtc = RandomForestClassifier()
    rtc.fit(X_train, Y_train)
    y_predict = rtc.predict(X_test)

    print  'The Accuracy of Linear RTC is ', rtc.score(X_test, Y_test)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))

    gbc = GradientBoostingClassifier()
    gbc.fit(X_train, Y_train)
    y_predict = gbc.predict(X_test)

    print  'The Accuracy of Linear GBC is ', gbc.score(X_test, Y_test)
    print  classification_report(Y_test, y_predict, target_names=digits.target_names.astype(str))





treeTest()