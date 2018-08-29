import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.pyplot as plt


#Plot (1)


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