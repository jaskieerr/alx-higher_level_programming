#!/usr/bin/python3
def complex_delete(my_dict, value):
    del_idx = []
    for key in my_dict:
        if my_dict[key] == value:
            del_idx.append(key)
    for key in del_idx:
        del my_dict[key]
    return my_dict
