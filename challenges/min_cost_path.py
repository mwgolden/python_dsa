from typing import List, Optional, Dict


def min_cost_path(matrix2d: List[List], i=0, j=0) -> int:
    n = len(matrix2d)  # number of rows
    m = len(matrix2d[0])  # number of columns
    if i == n-1 and j == m-1:
        return matrix2d[i][j]  # this is the bottom right cell of the 2D matrix
    elif i == n-1:
        return matrix2d[i][j] + min_cost_path(matrix2d, i, j+1)  # bottom row, can only move right
    elif j == m-1:
        return matrix2d[i][j] + min_cost_path(matrix2d, i+1, j)  # right-most column, can only move down
    else:
        return matrix2d[i][j] + min(min_cost_path(matrix2d, i+1, j), min_cost_path(matrix2d, i, j+1))


def min_cost_path_with_memoization(matrix2d: List[List], i=0, j=0, lookup: Optional[Dict]=None) -> int:
    lookup = {} if lookup is None else lookup
    n = len(matrix2d)  # number of rows
    m = len(matrix2d[0])  # number of columns
    if (i, j) in lookup:
        return lookup[(i, j)]
    if i == n-1 and j == m-1:
        return matrix2d[i][j]  # this is the bottom right cell of the 2D matrix
    elif i == n-1:
        lookup[(i, j)] = matrix2d[i][j] + min_cost_path_with_memoization(matrix2d, i, j+1, lookup)  # bottom row, can only move right
        return lookup[(i, j)]
    elif j == m-1:
        lookup[(i, j)] = matrix2d[i][j] + min_cost_path_with_memoization(matrix2d, i+1, j, lookup)  # right-most column, can only move down
        return lookup[(i, j)]
    else:
        lookup[(i, j)] = matrix2d[i][j] + min(min_cost_path_with_memoization(matrix2d, i+1, j, lookup), min_cost_path_with_memoization(matrix2d, i, j+1, lookup))
        return lookup[(i, j)]

