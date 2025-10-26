from .BlindSearch.index import bfs
from .Heuristic.index import astar
# from Evaluate.index import memory_count, time_count
import time
import tracemalloc


def solution(algorithm, testcase):
    print(f"Solving {testcase} using {algorithm}...")
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
          

# def estimate(algorithm, testcase):
#     '''
#         Final function to evaluate an algorithm in a specific testcase
#         Input:
#             algorithm: "blind_search" or "heuristic"
#             testcase: The testcase file name
#         Output: Tuple (memory_usage, time)
#             memory_usage: Total memory use for computing 
#             time_usage: Calculating time for a specific solution
#     '''
#     memory_usage = memory_count(algorithm, testcase)
#     time_usage = time_count(algorithm, testcase)
#     return (memory_usage, time_usage)


if __name__ == "__main__":
    print(solution('blind_search', 'mini_cosmos_1.txt'))
    # solution('heuristic', 'mini_cosmos_1.txt')
    # solution('blind_search', 'mini_cosmos_2.txt')
    # solution('heuristic', 'mini_cosmos_2.txt')
    # solution('blind_search', 'mini_cosmos_3.txt')
    # solution('heuristic', 'mini_cosmos_3.txt')
    # solution('blind_search', 'mini_cosmos_4.txt')
    # solution('heuristic', 'mini_cosmos_4.txt')