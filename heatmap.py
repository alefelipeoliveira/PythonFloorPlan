# import the required packages
from scipy import stats, integrate
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Reading floor plan to use as Background image
imgloc = "images\\layout.png"
img = plt.imread(imgloc)

#Creating dataframe from trajectory data
df = pd.read_csv("data\\history.csv")

# call the kernel density estimator function
ax = sns.kdeplot(df['x'], df['y'], cmap="Reds", shade=True, shade_lowest=False)
# the function has additional parameters you can play around with to fine-tune your heatmap, e.g.:
#ax = sns.kdeplot(x, y, kernel="gau", bw = 25, cmap="Reds", n_levels = 50, shade=True, shade_lowest=False, gridsize=100)

#adapt picture dimensions to floorplan dimension (25x25m) to trajectory points match with floorplan
ax.imshow(img, extent=[0, 25.00, 0, 25.00])

# plot your KDE
ax.set_frame_on(False)
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.axis('off')
plt.show()
 
# save your KDE to disk
fig = ax.get_figure()
fig.savefig('kde.png', transparent=True, bbox_inches='tight', pad_inches=0)