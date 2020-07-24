from sklearn import tree
clf = tree.DecisionTreeClassifier()
# height , hair-length, voice pitch
x = [[180, 15, 0],
     [167, 42, 1],
     [136, 35, 1],
     [174, 15, 0],
     [141, 28, 1]]
y=['man','woman','woman','man','woman']
clf=clf.fit(x,y)
