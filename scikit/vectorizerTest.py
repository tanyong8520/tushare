#!/usr/bin/env python
# -*- coding: utf-8 -*-
#特征提取
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
#新闻文本数据
from sklearn.datasets import fetch_20newsgroups
# 数据分割
from sklearn.model_selection import train_test_split
# 统计模型结果
from sklearn.metrics import classification_report

import pandas as pd


#特征提取和向量化
def printDictVertorizer():
    measurements = [{'city':'Dubai','temperature':33.},
                    {'city':'London','temperature':12.},
                    {'city':'San Fransisco','temperature':18.},
                    {'city':'xi an','temperature':8.}]

    vec = DictVectorizer()

    print vec.fit_transform(measurements).toarray()

    print vec.get_feature_names()


#未去掉停用词的特征提取
def notStopVectorizer():
    news = fetch_20newsgroups()
    X_train, X_test, Y_train, Y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)

    #文本特征抽取
    countvec = CountVectorizer()
    X_train_count = countvec.fit_transform(X_train)
    X_test_count = countvec.transform(X_test)

    from sklearn.naive_bayes import MultinomialNB
    mnb = MultinomialNB()
    mnb.fit(X_train_count, Y_train)
    y_predict = mnb.predict(X_test_count)

    print  'user CountVectorizer The Accuracy of Linear MNB is ', mnb.score(X_test_count, Y_test)
    print  classification_report(Y_test, y_predict, target_names=news.target_names)

    #文本特征抽取
    tfidvec = TfidfVectorizer()
    X_train_tfid = tfidvec.fit_transform(X_train)
    X_test_tfid = tfidvec.transform(X_test)

    from sklearn.naive_bayes import MultinomialNB
    mnb_tfid = MultinomialNB()
    mnb_tfid.fit(X_train_tfid, Y_train)
    y_predict_tfid = mnb_tfid.predict(X_test_tfid)

    print  'use TfidfVectorizer The Accuracy of Linear MNB is ', mnb_tfid.score(X_test_tfid, Y_test)
    print  classification_report(Y_test, y_predict_tfid, target_names=news.target_names)

def useStopVectorizer():
    news = fetch_20newsgroups()
    X_train, X_test, Y_train, Y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)

    #文本特征抽取
    countvec = CountVectorizer(analyzer='word',stop_words='english')
    X_train_count = countvec.fit_transform(X_train)
    X_test_count = countvec.transform(X_test)

    from sklearn.naive_bayes import MultinomialNB
    mnb = MultinomialNB()
    mnb.fit(X_train_count, Y_train)
    y_predict = mnb.predict(X_test_count)

    print  'user CountVectorizer The Accuracy of Linear MNB is ', mnb.score(X_test_count, Y_test)
    print  classification_report(Y_test, y_predict, target_names=news.target_names)

    #文本特征抽取
    tfidvec = TfidfVectorizer(analyzer='word',stop_words='english')
    X_train_tfid = tfidvec.fit_transform(X_train)
    X_test_tfid = tfidvec.transform(X_test)

    from sklearn.naive_bayes import MultinomialNB
    mnb_tfid = MultinomialNB()
    mnb_tfid.fit(X_train_tfid, Y_train)
    y_predict_tfid = mnb_tfid.predict(X_test_tfid)

    print  'use TfidfVectorizer The Accuracy of Linear MNB is ', mnb_tfid.score(X_test_tfid, Y_test)
    print  classification_report(Y_test, y_predict_tfid, target_names=news.target_names)


def titanicTest():
    titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
    y = titanic['survived']
    X = titanic.drop(['row.names','name','survived'], axis=1)

    X['age'].fillna(X['ange'].mean(), inplace = True)
    X.fillna('UNKNOWN', inplace = True)

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, random_state=33)

    vec = DictVectorizer()

    X_train = vec.fit_transform(X_train.to_dict(orient = 'record'))
    X_test = vec.transform(X_test.to_dict(orient = 'record'))

    print len(vec.feature_names_)

    #用决策树对数据进行预测
    from sklearn.tree import DecisionTreeClassifier
    dt = DecisionTreeClassifier(criterion = 'entropy')
    dt.fit(X_train, Y_train)
    dt.score(X_test, Y_test)

    #特征筛选器
    from sklearn import feature_selection
    fs = feature_selection.SelectPercentile(feature_selection.chi2, percentile=20)
    X_train_fs = fs.fit_transform(X_train, Y_train)
    dt.fit(X_train_fs, Y_train)
    X_test_fs = dt.transform(X_test)
    dt.score(X_test_fs, Y_test)

    #使用交叉验证
    from sklearn.model_selection import cross_val_score
    import numpy as np
    percentiles = range(1, 100, 2)
    results = []
    for i in percentiles:
        fs = feature_selection.SelectPercentile(feature_selection.chi2, percentile=i)
        X_train_fs = fs.fit_transform(X_train, Y_train)
        scores = cross_val_score(dt, X_train_fs, Y_train, cv=5)
        results = np.append(results, scores.mean())

    print results

    opt = np.where(results == results.max())[0]
    print 'Optimal number of features %d'%percentiles[opt]

    #使用最佳筛选后，利用相同的配置对模型在测试集上进行评估
    fs = feature_selection.SelectPercentile(feature_selection.chi2, percentile=opt)
    X_train_fs = fs.fit_transform(X_train, Y_train)
    dt.fit(X_train_fs, Y_train)
    X_test_fs = dt.transform(X_test)
    dt.score(X_test_fs, Y_test)

