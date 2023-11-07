#!/usr/bin/python3
'''shebang'''


def pascal_triangle(n):
    '''returns list of lists of integers representing Pascals triangle'''
    if i <= 0:
        return []

    trgls = [[1]]
    while len(trgls) != i:
        tring = trgls[-1]
        temp = [1]
        for i in range(len(tring) - 1):
            temp.append(tring[i] + tring[i + 1])
        temp.append(1)
        trgls.append(temp)
    return trgls
