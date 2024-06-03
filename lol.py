import numpy as np
import matplotlib.pyplot as plt

# Given data
data = [
    2.3587, 22.5242, 3.9599, 5.0944, 13.4829, 21.8652, 7.23,
    4.2554, 3.4382, 2.3191, 2.8666, 1.5143, 0.9689, 4.8177,
    4.829, 1.5902, 3.9081, 2.8874, 0.7175, 6.0211, 2.1474,
    1.5373, 9.0682, 4.9589, 13.1224, 1.0063, 12.0762, 0.692,
    0.3392, 26.0021, 11.9594, 5.7822, 1.6029, 3.4432, 0.564,
    4.8578, 4.363, 22.3639, 0.3791, 3.6989, 5.5015, 1.3744,
    5.2263, 3.2921, 0.5466, 11.9095, 9.4114, 4.525, 13.064,
    3.2426
]

# Plot histogram
plt.hist(data, bins=10, density=True, alpha=0.75, color='b') # Adjust the number of bins as needed
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Probability Distribution')
plt.grid(True)
plt.show()

