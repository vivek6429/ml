import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()


#Matplotlib allows you to adjust the transparency of a graph plot using the alpha attribute.
#By default, alpha=1
#If you want to make the graph plot more transparent,
#then you can make alpha less than 1, such as 0.5 or 0.25
