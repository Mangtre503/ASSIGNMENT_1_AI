from BlindSearch.index import bfs
from Heuristic.index import heuristic_solution
from Evaluate.index import memory_count, time_count


def solution(algorithm, testcase):
    '''
        Final function to find the solution of sokoban
        Input:
            algorithm: "blind_search" or "heuristic"
            testcase: The testcase file name
        Output:
            solutions: the step by step solutions
    '''
    if algorithm == "blind_search":
        return bfs(testcase)
    elif algorithm == "heuristic":
        return heuristic_solution(testcase)
    else:
        raise ValueError("Not known algorithm")

def estimate(algorithm, testcase):
    '''
        Final function to evaluate an algorithm in a specific testcase
        Input:
            algorithm: "blind_search" or "heuristic"
            testcase: The testcase file name
        Output: Tuple (memory_usage, time)
            memory_usage: Total memory use for computing 
            time_usage: Calculating time for a specific solution
    '''
    memory_usage = memory_count(algorithm, testcase)
    time_usage = time_count(algorithm, testcase)
    return (memory_usage, time_usage)


if __name__ == "__main__":
    print(solution('blind_search', 'mini_cosmos_1.txt'))