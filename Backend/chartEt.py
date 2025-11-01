import matplotlib.pyplot as plt

# Data
runtimesB = [
  0.0066,
  0.0335,
  0.1214,
  0.0088,
  0.1506,
  1.0454,
  0.0776,
  0.3855,
  0.0401,
  0.1809,
  0.1178,
  0.8352,
  0.1442,
  1.1399,
  0.1006,
  0.3379,
  0.1535,
  1.3739,
  0.1556,
  1.1807
]
runtimesH = [
    0.0167,
    0.1295,
    0.7395,
    0.1680,
    1.4926,
    10.0857,
    0.2254,
    1.9221,
    0.4226,
    1.1720,
    0.4038,
    5.8828,
    0.6494,
    7.1271,
    0.7254,
    2.1143,
    4.6445,
    46.0357,
    1.0859,
    21.9143
]


# Convert seconds → milliseconds
runtimesB_ms = [t * 1000 for t in runtimesB]
runtimesH_ms = [t * 1000 for t in runtimesH]

# Test case indices
test_cases = list(range(1, 21))

# Plot
plt.figure(figsize=(10, 10))
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


