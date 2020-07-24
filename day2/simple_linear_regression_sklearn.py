import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([171,151,124,134,156])
y = np.array([80,60,45,50,65])

clf = LinearRegression()
clf.fit(X.reshape(-1,1),y)
a=clf.predict([[133]])
print(a)
