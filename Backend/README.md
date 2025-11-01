### How to run

    ../ASSIGNMENT_1_AI> python -m Backend.index
    python3 -m Backend.chartMt to get png Memory Comparision
    python3 -m Backend.chartEt to get png Execution Time Comparision

### Result returned

    input:
        solution('blind_search', 'mini_cosmos_1.txt') (for bfs)
        solution('heuristic', 'mini_cosmos_1.txt') (for astar)
    output:
        'UULUURLDDRRURRUULLDDULLDDRRLDDRRUULUR', 0.001999378204345703, 125.0625 (list of steps, time (second), memory (KB))

### Draw chart

    python3 -m venv venv

    source venv/bin/activate

    pip3 install matplotlib

    python3 -m Backend.chartEt

    deactivate
