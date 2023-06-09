# -*- coding: utf-8 -*-
"""kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YxW6KmfC6Ihy1URz-24NROXHwcc2pcnR
"""

from sklearn.cluster import KMeans
import numpy as n

# Commented out IPython magic to ensure Python compatibility.
from sklearn import preprocessing
import sklearn.cluster as cluster
import sklearn.metrics as metrics
import pandas as p
from sklearn.preprocessing import MinMaxScaler
import seaborn as sb
from matplotlib import pyplot as pt
# %matplotlib inline

a = p.read_csv("customers.csv")
a.head()

a.shape

scaler = MinMaxScaler()
scale = scaler.fit_transform(a[['Annual Income (k$)','Spending Score (1-100)']])
a_scale = p.DataFrame(scale, columns = ['Annual Income (k$)','Spending Score (1-100)']);
a_scale.head(5)

k=KMeans(n_clusters=4)
y_predicted = k.fit_predict(a_scale[['Annual Income (k$)','Spending Score (1-100)']])
y_predicted

k.cluster_centers_

a['Clusters'] = k.labels_
sb.scatterplot(x="Spending Score (1-100)", y="Annual Income (k$)",hue = 'Clusters',  data=a,palette='viridis')

P=range(2,12)
ws=[]
for p in P:
  kmeans=cluster.KMeans(n_clusters=p)
  kmeans=kmeans.fit(a_scale)
  ws_iter = kmeans.inertia_
  ws.append(ws_iter)

pt.xlabel('P')
pt.ylabel('Within-Cluster-Sum of Squared Errors (WS)')
pt.plot(P,ws)

km=KMeans(n_clusters=5)
y_predicted = km.fit_predict(a_scale[['Annual Income (k$)','Spending Score (1-100)']])
y_predicted

a['Clusters'] = km.labels_

sb.scatterplot(x="Spending Score (1-100)", y="Annual Income (k$)",hue = 'Clusters',  data=a,palette='viridis')

