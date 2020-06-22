import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#Reading floor plan to use as Background image
imgloc = "images\\layout.png"
img = plt.imread(imgloc)

#Creating dataframe from trajectory data
df = pd.read_csv("data\\history.csv")

fig, ax = plt.subplots()

#scatter points from trajectory data
ax.scatter(list(df['x']), list(df['y']))

#adapt picture dimensions to floorplan dimension (25x25m) to trajectory points match with floorplan
ax.imshow(img, extent=[0, 25.00, 0, 25.00])

#turn off grid and ticks
plt.grid('off')
plt.axis('off')
ax.grid()

#show plot
plt.show()