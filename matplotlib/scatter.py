import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
