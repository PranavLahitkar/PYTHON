import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)


# Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [7, 3, 9, 5]
plt.figure(figsize=(8, 6))
plt.bar(categories, values)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()