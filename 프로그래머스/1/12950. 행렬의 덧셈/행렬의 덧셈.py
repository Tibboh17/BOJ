import numpy as np

def solution(arr1, arr2):
    matrix = np.array(arr1) + np.array(arr2)
    answer = matrix.tolist()
    return answer