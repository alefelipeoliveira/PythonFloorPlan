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


ax.imshow(img, extent=[0, 25.00, 0, 25.00])
plt.grid('off')

#ax.set(xlabel='position x [m]', ylabel='position y [m]', title='Office Plan')
ax.grid()

plt.show()

imgplot = plt.imshow(img)