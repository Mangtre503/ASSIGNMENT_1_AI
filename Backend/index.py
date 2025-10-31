from .algorithm import bfs
from .algorithm import build_solutions
from .algorithm import astar
# from Evaluate.index import memory_count, time_count
import time
import tracemalloc


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
    tracemalloc.start()
    start_time=time.time()
    if algorithm == "blind_search":
        solution = bfs(testcase)
    elif algorithm == "heuristic":
        solution = astar(testcase)
    else:
        raise ValueError("Not known algorithm")
    end_time=time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    runtime = end_time - start_time
    memory_usage = peak /1024  # in KB
    
    print(f"Algorithm: {algorithm}")
    print(f'Runtime: {runtime:.4f} seconds')
    print(f'Peak Memory Usage: {memory_usage:.2f} KB')
    return solution, runtime, memory_usage
          

if __name__ == "__main__":
    build_solutions()
    # print(solution('blind_search', 'mini_cosmos_1.txt'))
    # print(solution('blind_search', 'mini_cosmos_2.txt'))
    # print(solution('blind_search', 'mini_cosmos_3.txt'))
    # print(solution('blind_search', 'mini_cosmos_4.txt'))
    # print(solution('blind_search', 'mini_cosmos_5.txt'))
    # print(solution('blind_search', 'mini_cosmos_6.txt'))
    # print(solution('blind_search', 'mini_cosmos_7.txt'))
    # print(solution('blind_search', 'mini_cosmos_8.txt'))
    # print(solution('blind_search', 'mini_cosmos_9.txt'))
    # print(solution('blind_search', 'mini_cosmos_10.txt'))
    # print(solution('blind_search', 'mini_cosmos_11.txt'))
    # print(solution('blind_search', 'mini_cosmos_12.txt'))
    # print(solution('blind_search', 'mini_cosmos_13.txt'))
    # print(solution('blind_search', 'mini_cosmos_14.txt'))
    # print(solution('blind_search', 'mini_cosmos_15.txt'))
    # print(solution('blind_search', 'mini_cosmos_16.txt'))
    # print(solution('blind_search', 'mini_cosmos_17.txt'))
    # print(solution('blind_search', 'mini_cosmos_18.txt'))
    # print(solution('blind_search', 'mini_cosmos_19.txt'))
    # print(solution('blind_search', 'mini_cosmos_20.txt'))
    # print(solution('blind_search', 'mini_cosmos_21.txt'))



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

