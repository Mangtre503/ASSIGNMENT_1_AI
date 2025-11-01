import matplotlib.pyplot as plt

# Data
runtimesB = [
    0.0020, 0.0089, 0.0315, 0.0030, 0.0376,
    0.2735, 0.0180, 0.1093, 0.0126, 0.0495,
    0.0350, 0.2183, 0.0400, 0.2913, 0.0235,
    0.0867, 0.0431, 0.3537, 0.0370, 0.3155,
]

runtimesH = [
    0.0021, 0.0110, 0.0400, 0.0050, 0.0550,
    0.3801, 0.0315, 0.1799, 0.0170, 0.0699,
    0.0440, 0.3364, 0.0538, 0.4555, 0.0320,
    0.1265, 0.0566, 0.5251, 0.0546, 0.4516,
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


