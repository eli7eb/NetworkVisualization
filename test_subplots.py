import numpy as np
import matplotlib.pyplot as plt

# Create some sample data
data = np.arange(20)

# Create a matplotlib figure
fig, ax = plt.subplots()

# Create multiple plots
for i in range(7):
    ax.plot(data, i * data, label=f'y={i}x')

# Set title and labels
ax.set_title('Example plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Add a legend
ax.legend()

# Visualize the final plot
plt.show()