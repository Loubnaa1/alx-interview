#!/usr/bin/python3
''' pascal triangle'''


def pascal_triangle(n):
    '''pascal's triangle'''
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        R = [1]
        for j in range(1, i):
            R.append(pascal[i-1][j-1] + pascal[i-1][j])
        R.append(1)
        pascal.append(R)

    return pascal
