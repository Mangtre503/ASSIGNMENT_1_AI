import matplotlib.pyplot as plt

# Data
peak_memory_usageB = [
    83.45, 478.14, 1888.48, 92.10, 2161.00,
    14411.98, 950.85, 6745.23, 523.88, 2535.11,
    1879.47, 11197.77, 2105.74, 14960.06, 1587.27,
    4134.33, 2115.47, 16734.55, 2179.90, 15171.20
]

peak_memory_usageH = [
    83.45, 83.52, 83.51, 92.17, 92.15,
    92.14, 92.14, 92.13, 83.45, 83.45,
    92.09, 92.08, 100.50, 100.49, 83.40,
    83.39, 101.22, 101.21, 92.04, 92.03
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
