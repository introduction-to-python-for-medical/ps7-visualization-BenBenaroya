# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='diabetes', version=1, as_frame=True)
df = data.frame
features = list(df.columns)
selected_features = [features[3], features[2], features[7], features[5], features[8]]

#creating a histogram
fig, axs  = plt.subplots(1, len(selected_features), figsize = (18,3))
for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

# Creating a scatter plot for the selected pair
x = df[selected_features[0]]  # The reference feature
y = df[selected_features[3]]  # A feature to compare to
plt.scatter(x, y)
plt.xlabel(selected_features[0])
plt.ylabel(selected_features[3])

# Saving the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()
