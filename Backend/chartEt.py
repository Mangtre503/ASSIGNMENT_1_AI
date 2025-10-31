import matplotlib.pyplot as plt

# Data
runtimesB = [
    0.0061, 0.0346, 0.1534, 0.0088, 0.1521,
    1.0613, 0.0789, 0.3881, 0.0395, 0.1736,
    0.1169, 0.8327, 0.1565, 1.0691, 0.0948,
    0.3130, 0.1451, 1.3116, 0.1485, 1.1293
]

runtimesH = [
    0.0018, 0.0015, 0.0014, 0.0015, 0.0014,
    0.0016, 0.0015, 0.0015, 0.0013, 0.0013,
    0.0015, 0.0015, 0.0015, 0.0018, 0.0014,
    0.0012, 0.0015, 0.0020, 0.0018, 0.0017
]

# Convert seconds → milliseconds
runtimesB_ms = [t * 1000 for t in runtimesB]
runtimesH_ms = [t * 1000 for t in runtimesH]

# Test case indices
test_cases = list(range(1, 21))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(test_cases, runtimesB_ms, marker='o', color='blue', label='Blind Search')
plt.plot(test_cases, runtimesH_ms, marker='o', color='red', label='Heuristic')

# Labels, title, and grid
plt.title('Comparison of Execution Time between Blind Search and Heuristic', fontsize=13)
plt.xlabel('Test Case', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(range(0, 22, 2))  # from 0 → 20, step 2
# Save as high-resolution image
plt.savefig('runtime_comparison_ms.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()


