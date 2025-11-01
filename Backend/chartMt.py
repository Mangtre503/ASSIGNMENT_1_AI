import matplotlib.pyplot as plt

# Data
peak_memory_usageB = [
    125.51, 479.11, 1886.94, 130.98, 2158.66,
    14410.02, 955.95, 6741.60, 523.86, 2533.06,
    1876.42, 11189.74, 2110.11, 14952.47, 1586.12,
    4130.62, 2111.03, 16726.96, 2171.42, 15163.10,
]

peak_memory_usageH = [
    124.72, 359.63, 1701.42, 130.98, 1991.65,
    14949.70, 982.05, 4982.98, 470.96, 2296.51,
    1687.51, 10568.58, 2184.03, 15621.86, 1091.72,
    4242.74, 1963.54, 17500.48, 2005.07, 15864.96,
]

# Test case indices
test_cases = list(range(1, 21))

# Plot
plt.figure(figsize=(10, 10))
plt.plot(test_cases, peak_memory_usageB, marker='o', color='blue', label='Blind Search')
plt.plot(test_cases, peak_memory_usageH, marker='o', color='red', label='Heuristic')

# Labels, title, and grid
plt.title('Comparison of Peak Memory Usage between Blind Search and Heuristic', fontsize=13)
plt.xlabel('Test Case', fontsize=12)
plt.ylabel('Peak Memory Usage (KB)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(range(0, 22, 2))  # from 0 → 20, step 2
plt.yticks(range(0, 17500, 1000))  # from 0 → 20, step 2

# Save as high-resolution image
plt.savefig('memory_comparison.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
