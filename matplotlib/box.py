import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(data=data)
plt.title('Box Plot')
plt.grid(True)
plt.show()
