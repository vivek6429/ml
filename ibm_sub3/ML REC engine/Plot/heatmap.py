import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# Create data
x = np.random.randn(4096)
y = np.random.randn(4096)

# Create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Plot heatmap
plt.clf()
plt.title('Python heatmap example')
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(heatmap, extent=extent)
plt.show()


#import numpy as np; np.random.seed(0)
#import seaborn as sns; sns.set()
#uniform_data = np.random.rand(10, 12)
#ax = sns.heatmap(uniform_data)
