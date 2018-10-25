#!/usr/bin/env python
# -*- coding: utf-8 -*-

#波士顿房价数据
from sklearn.datasets import load_boston
# 数据分割
from sklearn.model_selection import train_test_split
#数据标准化
from sklearn.preprocessing import StandardScaler

#回归器测试

#线性回归器
def LinearRegressionTest():
    from sklearn.linear_model import LinearRegression
    boston = load_boston()
    X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

    ss_X = StandardScaler()
    ss_Y = StandardScaler()

    X_train = ss_X.fit_transform(X_train)
    X_test = ss_X.transform(X_test)
    Y_train = ss_Y.fit_transform(Y_train.reshape(-1,1))
    Y_test = ss_Y.transform(Y_test.reshape(-1,1))

    lr = LinearRegression()
    lr.fit(X_train, Y_train)
    y_predict = lr.predict(X_test)

    from sklearn.metrics import r2_score,mean_squared_error, mean_absolute_error
    print 'the value of default measurement of LinearRegression is', lr.score(X_test,Y_test)
    # print 'the value of R-squared of LinearRegression is', r2_score(Y_test, y_predict)
    # print 'the value of mean squared error  of LinearRegression is', \
    #     mean_squared_error(ss_Y.inverse_transform(Y_test), ss_Y.inverse_transform(y_predict))
    # print 'the value of mean absolute error  of LinearRegression is', \
    #     mean_absolute_error(ss_Y.inverse_transform(Y_test), ss_Y.inverse_transform(y_predict))

#梯度下降回归
def SGDRegressorTest():
    from sklearn.linear_model import SGDRegressor

    boston = load_boston()
    X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

    ss_X = StandardScaler()
    ss_Y = StandardScaler()

    X_train = ss_X.fit_transform(X_train)
    X_test = ss_X.transform(X_test)
    Y_train = ss_Y.fit_transform(Y_train.reshape(-1, 1))
    Y_test = ss_Y.transform(Y_test.reshape(-1, 1))

    sgdr = SGDRegressor()
    sgdr.fit(X_train, Y_train)
    y_predict = sgdr.predict(X_test)

    from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
    print 'the value of default measurement of SGDRegressor is', sgdr.score(X_test, Y_test)
    # print 'the value of R-squared of SGDRegressor is', r2_score(Y_test, y_predict)
    # print 'the value of mean squared error  of SGDRegressor is', \
    #     mean_squared_error(ss_Y.inverse_transform(Y_test), ss_Y.inverse_transform(y_predict))
    # print 'the value of mean absolute error  of SGDRegressor is', \
    #     mean_absolute_error(ss_Y.inverse_transform(Y_test), ss_Y.inverse_transform(y_predict))

#支持向量机回归
def SVRRegressorTest():
    from sklearn.svm import SVR

    boston = load_boston()
    X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

    ss_X = StandardScaler()
    ss_Y = StandardScaler()

    X_train = ss_X.fit_transform(X_train)
    X_test = ss_X.transform(X_test)
    Y_train = ss_Y.fit_transform(Y_train.reshape(-1, 1))
    Y_test = ss_Y.transform(Y_test.reshape(-1, 1))

    # 线性核函数
    svr = SVR(kernel='poly')
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of SVR is', svr.score(X_test, Y_test)

    #多项式核函数
    svr = SVR(kernel='poly')
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of SVR is', svr.score(X_test, Y_test)

    #使用径向基核函数
    svr = SVR(kernel='rbf')
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of SVR is', svr.score(X_test, Y_test)

#K值邻近
def KNeighborsRegressorTest():
    from sklearn.neighbors import KNeighborsRegressor
    boston = load_boston()
    X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

    ss_X = StandardScaler()
    ss_Y = StandardScaler()

    X_train = ss_X.fit_transform(X_train)
    X_test = ss_X.transform(X_test)
    Y_train = ss_Y.fit_transform(Y_train.reshape(-1, 1))
    Y_test = ss_Y.transform(Y_test.reshape(-1, 1))

    svr = KNeighborsRegressor(weights='uniform')
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of KNeighborsRegressor is', svr.score(X_test, Y_test)

    svr = KNeighborsRegressor(weights='distance')
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of KNeighborsRegressor is', svr.score(X_test, Y_test)

#回归树
def DecisionTreeRegressor():
    from sklearn.tree import DecisionTreeRegressor
    boston = load_boston()
    X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

    # ss_X = StandardScaler()
    # ss_Y = StandardScaler()
    #
    # X_train = ss_X.fit_transform(X_train)
    # X_test = ss_X.transform(X_test)
    # Y_train = ss_Y.fit_transform(Y_train.reshape(-1, 1))
    # Y_test = ss_Y.transform(Y_test.reshape(-1, 1))

    svr = DecisionTreeRegressor()
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of DecisionTreeRegressor is', svr.score(X_test, Y_test)

def TreeRegressor():
    #随机森林
    from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor,GradientBoostingRegressor
    boston = load_boston()

    X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

    # ss_X = StandardScaler()
    # ss_Y = StandardScaler()
    #
    # X_train = ss_X.fit_transform(X_train)
    # X_test = ss_X.transform(X_test)
    # Y_train = ss_Y.fit_transform(Y_train.reshape(-1, 1))
    # Y_test = ss_Y.transform(Y_test.reshape(-1, 1))

    svr = RandomForestRegressor()
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of RandomForestRegressor is', svr.score(X_test, Y_test)

    etr = ExtraTreesRegressor()
    etr.fit(X_train, Y_train)
    y_predict = etr.predict(X_test)
    print 'the value of default measurement of ExtraTreesRegressor is', etr.score(X_test, Y_test)

    svr = GradientBoostingRegressor()
    svr.fit(X_train, Y_train)
    y_predict = svr.predict(X_test)
    print 'the value of default measurement of GradientBoostingRegressor is', svr.score(X_test, Y_test)

    import numpy as np
    print np.sort(zip(etr.feature_importances_, boston.feature_names),axis=0)



TreeRegressor()
