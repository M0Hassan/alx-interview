#!/usr/bin/python3

"""Pascal Triangle"""

def pascal_triangle(n):
    """returns a list of lists of integers
    representiing the Pascal's triangle ofn:
    if n <= 0 Returns an empty list"""

    if n <= 0:
        return []

    output = [[1]]

    for i in range(n - 1):
        temp = [0] + output[-1] + [0]
        row = []
        for j in range(len(output[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        output.append(row)

    return output

