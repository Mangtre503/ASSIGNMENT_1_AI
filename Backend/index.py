from .algorithm import bfs
from .algorithm import astar
# from Evaluate.index import memory_count, time_count
import time
import tracemalloc
import os


def solution(algorithm, testcase):
    # print(f"Solving {testcase} using {algorithm}...")
    '''
        Final function to find the solution of sokoban
        Input:
            algorithm: "blind_search" or "heuristic"
            testcase: The testcase file name
        Output:
            solutions: the step by step solutions
    '''
    try:
        i = int(testcase.split("_")[-1].split(".")[0])  # mini_cosmos_1.txt -> 1
    except ValueError:
        raise ValueError(f"Invalid testcase name: {testcase}")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(current_dir, "solutions")
    os.makedirs(solutions_dir, exist_ok=True)

    tracemalloc.start()
    start_time=time.time()
    if algorithm == "blind_search":
        solution = bfs(testcase)
        result_filename = f"BlindSearch_testcase_{i}.txt"
    elif algorithm == "heuristic":
        solution = astar(testcase)
        result_filename = f"Heuristic_testcase_{i}.txt"
    else:
        raise ValueError("Not known algorithm")
    end_time=time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    runtime = end_time - start_time
    memory_usage = peak /1024  # in KB
    
    result_file_path = os.path.join(solutions_dir, result_filename)
    with open(result_file_path, "w", encoding="utf-8") as f:
        f.write(solution) 
    print(f"✅ Algorithm: {algorithm}")
    print(f"📄 Saved to: {result_file_path}")
    print(f"⏱ Runtime: {runtime:.4f} seconds")
    print(f"💾 Peak Memory: {memory_usage:.2f} KB")
    return solution, runtime, memory_usage
          

if __name__ == "__main__":
    print(solution('blind_search', 'mini_cosmos_1.txt'))
    print(solution('blind_search', 'mini_cosmos_2.txt'))
    print(solution('blind_search', 'mini_cosmos_3.txt'))
    print(solution('blind_search', 'mini_cosmos_4.txt'))
    print(solution('blind_search', 'mini_cosmos_5.txt'))
    print(solution('blind_search', 'mini_cosmos_6.txt'))
    print(solution('blind_search', 'mini_cosmos_7.txt'))
    print(solution('blind_search', 'mini_cosmos_8.txt'))
    print(solution('blind_search', 'mini_cosmos_9.txt'))
    print(solution('blind_search', 'mini_cosmos_10.txt'))
    print(solution('blind_search', 'mini_cosmos_11.txt'))
    print(solution('blind_search', 'mini_cosmos_12.txt'))
    print(solution('blind_search', 'mini_cosmos_13.txt'))
    print(solution('blind_search', 'mini_cosmos_14.txt'))
    print(solution('blind_search', 'mini_cosmos_15.txt'))
    print(solution('blind_search', 'mini_cosmos_16.txt'))
    print(solution('blind_search', 'mini_cosmos_17.txt'))
    print(solution('blind_search', 'mini_cosmos_18.txt'))
    print(solution('blind_search', 'mini_cosmos_19.txt'))
    print(solution('blind_search', 'mini_cosmos_20.txt'))
    print(solution('blind_search', 'mini_cosmos_21.txt'))



    # print(solution('heuristic', 'mini_cosmos_1.txt'))
    # print(solution('heuristic', 'mini_cosmos_2.txt'))
    # print(solution('heuristic', 'mini_cosmos_3.txt'))
    # print(solution('heuristic', 'mini_cosmos_4.txt'))
    # print(solution('heuristic', 'mini_cosmos_5.txt'))
    # print(solution('heuristic', 'mini_cosmos_6.txt'))
    # print(solution('heuristic', 'mini_cosmos_7.txt'))
    # print(solution('heuristic', 'mini_cosmos_8.txt'))
    # print(solution('heuristic', 'mini_cosmos_9.txt'))
    # print(solution('heuristic', 'mini_cosmos_10.txt'))
    # print(solution('heuristic', 'mini_cosmos_11.txt'))
    # print(solution('heuristic', 'mini_cosmos_12.txt'))
    # print(solution('heuristic', 'mini_cosmos_13.txt'))
    # print(solution('heuristic', 'mini_cosmos_14.txt'))
    # print(solution('heuristic', 'mini_cosmos_15.txt'))
    # print(solution('heuristic', 'mini_cosmos_16.txt'))
    # print(solution('heuristic', 'mini_cosmos_17.txt'))
    # print(solution('heuristic', 'mini_cosmos_18.txt'))
    # print(solution('heuristic', 'mini_cosmos_19.txt'))
    # print(solution('heuristic', 'mini_cosmos_20.txt'))
    # solution('heuristic', 'mini_cosmos_1.txt')
    # solution('blind_search', 'mini_cosmos_2.txt')
    # solution('heuristic', 'mini_cosmos_2.txt')
    # solution('blind_search', 'mini_cosmos_3.txt')
    # solution('heuristic', 'mini_cosmos_3.txt')
    # solution('blind_search', 'mini_cosmos_4.txt')
    # solution('heuristic', 'mini_cosmos_4.txt')

