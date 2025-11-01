import matplotlib.pyplot as plt

# Data
peak_memory_usageB = [
    83.46,
    478.14,
    1888.48,
    92.10,
    2161.00,
    14411.98,
    950.85,
    6745.23,
    523.88,
    2535.11,
    1879.47,
    11197.77,
    2105.74,
    14960.06,
    1587.27,
    4134.33,
    2115.47,
    16734.55,
    2179.90,
    15171.20
]


peak_memory_usageH = [
    96.84,
    550.56,
    2497.99,
    214.13,
    2919.44,
    21385.96,
    1086.32,
    6304.19,
    731.64,
    2957.34,
    1860.60,
    12968.60,
    2581.61,
    18459.04,
    1532.20,
    5210.37,
    6381.17,
    37070.59,
    2556.10,
    21340.92
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
plt.yticks(range(0, 45000, 2000))  # from 0 → 20, step 2

# Save as high-resolution image
plt.savefig('memory_comparison.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
