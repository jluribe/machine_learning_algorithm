from sklearn.tree import DecisionTreeClassifier
def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer

    clf = DecisionTreeClassifier(random_state=0)
    clf = clf.fit(features_train, labels_train)
    return clf