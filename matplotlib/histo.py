import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Histogram
data = np.random.randn(1000)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()