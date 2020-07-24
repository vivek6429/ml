import pandas as pd
from sklearn import LogisticRegression
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data= {'mid1': [20,20,19,18,17,17,16,15,15,14,14,13,13,12,12,11,11,10,10,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0,0,0],
       'mid2': [20,19,20,19,18,16,17,16,17,15,16,13,14,11,13,11,12,11,9,10,11,9,8,8,9,8,6,6,7,5,4,2,3,2,1,0,4,5,2,1,0],
       'final': ['9.8','9.7','9.7','9.5','9.3','9','9','8.8','8.7','8.2','8.4','7.8','8','7.2','7.5','6.9','7.1','6.8','6.7','6.7','6.8','6.5','6','5.7','5.9','5.6','5.2','5','5.2','4.8','4.6','4','3.7','3.3','2.8','2','2','2.3','1.5','1','0']
                }


df=pd.DataFrame(data,columns=['mid1','mid2','final'])

X =df[['mid1','mid2']]
Y = df['final']

reger=LogisticRegression()
reger.fit(X,Y)

aa=[[(varr.get()),(varr1.get())]]
ma=reger.predict(aa)
print(ma)


