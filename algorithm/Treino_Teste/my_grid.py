from sklearn import cross_validation
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV

iris = datasets.load_iris()
features = iris.data
labels = iris.target


parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = SVC()
clf = GridSearchCV(svr, parameters)
clf.fit(features, labels)

# print features
print labels
print clf.score(features, labels)
print clf.best_params_