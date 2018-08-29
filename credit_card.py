import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets


#데이타 요약 bar plot
credit_data = pd.read_csv("C:\creditcard.csv")
mean_data = credit_data.describe().loc["mean"]
mean_data = mean_data.drop(["Time", "Amount", "Class"])
plt.xticks(rotation=90)
plt.ylabel("Mean")
plt.xlabel("Item")
plt.title("Credit card")
plt.bar(mean_data.index, mean_data)


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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

credit_data = pd.read_csv("C:\creditcard.csv")

#-----------------------------------------------------
#boxplot 
for column in credit_data:

    if column != "Time" and column != "Class":
    #if (column == "V1" or column=="V2"):
        sns.boxplot(x="Class", y=column, data=credit_data)
        sns.stripplot(x="Class", y=column, data=credit_data, jitter=True, edgecolor="gray")
        plt.show()
        
#-----------------------------------------------------
#facetGrid 
first_col = np.array(credit_data.columns)
second_col = np.array(credit_data.columns)

index = [0]
first_col = np.delete(first_col, index)
second_col = np.delete(second_col, index)

#print(type(first_col))
print(first_col)
print(second_col)
s_index = 0
for f_col in first_col:
    for value in range(s_index, len(second_col)):
        sns.FacetGrid(credit_data, hue="Class", size=5)\
        .map(plt.scatter, f_col, second_col[value]) \
        .add_legend()
        print(second_col[value])
    s_index += 1
    
    
        

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
