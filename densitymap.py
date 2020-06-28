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

# using density estimator function to creat the density map
ax = sns.kdeplot(df['x'], df['y'], cmap="Reds", shade=True, shade_lowest=False)

#adapt picture dimensions to floorplan dimension (25x25m) to trajectory points match with floorplan
ax.imshow(img, extent=[0, 25.00, 0, 25.00])

# plot your KDE from x and y limits
ax.set_frame_on(False)
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.axis('off')
plt.show()