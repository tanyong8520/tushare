#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt
import pandas as pd

# 手写体数据源
from sklearn.datasets import load_digits
# 数据分割
from sklearn.model_selection import train_test_split
#轮廓系数
from sklearn.metrics import silhouette_score

#聚类测试

def kmeansTest():
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=10)
    digits = load_digits()

    X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)

    kmeans.fit(X_train)
    y_pred = kmeans.predict(X_test)

    from sklearn import metrics
    print metrics.adjusted_rand_score(Y_test, y_pred)

def pltTest():
    plt.subplot(3,2,1)#这里的意思是这六个子图是呈3行2列排序的。
    x1 = np.array([1,2,3,1,5,6,4,4,6,7,8,9,7,9])
    x2 = np.array([1,3,2,2,8,6,7,6,7,1,2,1,1,3])
    X = np.array(zip(x1, x2)).reshape(len(x1), 2)#zip(x1, x2)的意思就是拼接起来变成一个坐标。
    # X就是点的坐标的集合
    # reshape的作用就是让列表的元素也是列表，如果没有reshape这个函数，那么列表的元素是元组
    # 所以reshape对输出功能没有影响，只是让输出的形式发生了改变。

    plt.xlim([0,10])
    plt.ylim([0,10])
    plt.title('Instances')
    plt.scatter(x1,x2)

    colors = ['b','g','r','c','m','y','k','b']
    markers = ['o','s','D','v','^','p','*','+']

    clusters = [2,3,4,5,8]
    subplot_counter = 1

    sc_scores = []

    for t in clusters:
        subplot_counter +=1
        plt.subplot(3, 2, subplot_counter)#subplot表示画在同一张图中的子图
        from sklearn.cluster import KMeans
        kmeans_model = KMeans(n_clusters=t).fit(X)
        for i ,l in enumerate(kmeans_model.labels_):
            plt.plot(x1[i],x2[i], color = colors[l], marker = markers[l], ls ='None')
        plt.xlim([0,10])
        plt.ylim([0,10])
        sc_score = silhouette_score(X, kmeans_model.labels_, metric= 'euclidean')#这个讲的是轮廓系数
        sc_scores.append(sc_score)
        plt.title('K=%s, silhouette coefficient=%0.03f'%(t, sc_score))
    plt.figure()
    plt.plot(clusters, sc_scores, '*-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette coefficient Score')

    plt.show()

def kmeanstest2():
    from sklearn.cluster import KMeans
    from scipy.spatial.distance import cdist
    import matplotlib.pyplot as plt

    cluster1 = np.random.uniform(0.5, 1.5, (2,10))
    cluster2 = np.random.uniform(5.5, 6.5, (2, 10))
    cluster3 = np.random.uniform(3.0, 4.0, (2, 10))
    X = np.hstack((cluster1,cluster2,cluster3)).T
    plt.scatter(X[:,0], X[:,1])
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()

    K = range(1,10)
    meandistortions = []
    for k in K:
        kmeans = KMeans(n_clusters = k)
        kmeans.fit(X)
        meandistortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1))/X.shape[0])

    plt.plot(K, meandistortions,'bx-')
    plt.xlabel('k')
    plt.ylabel('average dispersion')
    plt.title('selecting k with the elbow method')
    plt.show()


def lins3D():


    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = Axes3D(fig)

    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)  # 设置z值
    r = z ** 2 + 1
    x = r * np.sin(theta)  # 设置x值
    y = r * np.cos(theta)  # 设置y值

    ax.plot(x, y, z)

    plt.show()

def scatter3D():
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = Axes3D(fig)

    xs = 1
    ys = 1
    zs = 1

    ax.scatter(xs, ys, zs)

    plt.show()

def wireframe():
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax = Axes3D(fig)

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    surf = ax.plot_surface(X, Y, Z)


pltTest()