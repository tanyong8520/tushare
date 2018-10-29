#!/usr/bin/env python
# -*- coding: utf-8 -*-

#新闻文本数据
from sklearn.datasets import fetch_20newsgroups
# 数据分割
from sklearn.model_selection import train_test_split
#向量机分类器
from sklearn.svm import SVC
#文本特征提取
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.pipeline import Pipeline

import numpy as np

def gridSearchTest():
    news = fetch_20newsgroups(subset='all')
    X_train, X_test, Y_train, Y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)

    clf = Pipeline([('vect', TfidfVectorizer(stop_words='english', analyzer='word')),('svc', SVC())])

    parameters = {'svc_gamma':np.logspace(-2, 1, 4), 'svc_C':np.logspace(-1,1,3)}

    from sklearn.model_selection import GridSearchCV
    gs = GridSearchCV(clf, parameters, verbose=2, refit=True, cv=3)

    #初始化配置并行网格搜索，n_jobs=-1代表使用该计算机全部的CPU
    gs=GridSearchCV(clf,parameters,verbose=2,refit=True,cv=3,n_jobs=-1)

    time_=gs.fit(X_train,Y_train)
    gs.best_params_,gs.best_score_
    #输出最佳模型在测试集上的准确性
    print(gs.score(X_test,Y_test))



