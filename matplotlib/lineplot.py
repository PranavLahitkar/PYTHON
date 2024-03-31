import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()