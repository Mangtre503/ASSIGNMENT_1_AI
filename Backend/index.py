from .BlindSearch.index import bfs
from .Heuristic.index import astar
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



    print(solution('heuristic', 'mini_cosmos_1.txt'))
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


#     runtimesB = [
#     0.0061,
#     0.0346,
#     0.1534,
#     0.0088,
#     0.1521,
#     1.0613,
#     0.0789,
#     0.3881,
#     0.0395,
#     0.1736,
#     0.1169,
#     0.8327,
#     0.1565,
#     1.0691,
#     0.0948,
#     0.3130,
#     0.1451,
#     1.3116,
#     0.1485,
#     1.1293
# ]


# runtimesH = [
#     0.0018, 0.0015, 0.0014, 0.0015, 0.0014,
#     0.0016, 0.0015, 0.0015, 0.0013, 0.0013,
#     0.0015, 0.0015, 0.0015, 0.0018, 0.0014,
#     0.0012, 0.0015, 0.0020, 0.0018, 0.0017
# ]

# peak_memory_usage = [
#     83.45, 478.14, 1888.48, 92.10, 2161.00,
#     14411.98, 950.85, 6745.23, 523.88, 2535.11,
#     1879.47, 11197.77, 2105.74, 14960.06, 1587.27,
#     4134.33, 2115.47, 16734.55, 2179.90, 15171.20
# ]


# peak_memory_usageH = [
#     83.45, 83.52, 83.51, 92.17, 92.15,
#     92.14, 92.14, 92.13, 83.45, 83.45,
#     92.09, 92.08, 100.50, 100.49, 83.40,
#     83.39, 101.22, 101.21, 92.04, 92.03
# ]
