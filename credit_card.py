import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

#Plot (1)
n_neighbors = 15
x1 = data['V1']
x2 = data['V2']
y = data.Class
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
h =0.02
clf = neighbors.KNeighborsClassifier(n_neighbors, weights = 'uniform')
clf.fit(x,y)
clf
x_min, x_max = x1.min()- 1, x1.max() - 1
y_min, y_max = x2.min()- 1, x2.max() - 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                    np.arange(y_min, y_max, h))
xr = xx.ravel()
yr = yy.ravel()
xy = np.c_[xr,yr]
z = clf.predict(xy)
z= z.reshape(xx.shape)
plt.pcolormesh(xx,yy,z,cmap = cmap_light)
plt.scatter(x1,x2,c=y,cmap = cmap_bold)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())

#Plot (2)



#Plot (3)
data = pd.read_csv('creditcard.csv')
data5=data[['V1', 'V2']]
data00 = data.var()[1:29]
plt.plot(range(1,29),data00)
plt.show()

#Plot(4)
clf=tree.DecisionTreeClassifier()
clf.fit(data5[['V1', 'V2']], data['Class'])
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=['V1', 'V2'])
dot_data.getvalue()
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('creditcard.png')
