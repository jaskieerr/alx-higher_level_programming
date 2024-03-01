#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    fiding peak via recursion
    """
    n = len(list_of_integers)
    
    if n == 0:
        return None
    
    if n == 1:
        return list_of_integers[0]
    
    mid = n // 2
    
    if mid - 1 >= 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    elif mid + 1 < n and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return list_of_integers[mid]

