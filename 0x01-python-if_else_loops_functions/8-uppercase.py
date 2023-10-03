#!/usr/bin/python3

def uppercase(str):
    final_res = ""
    for c in str:
        if 'a' <= c <= 'z':
            final_res += chr(ord(c) - 32)
        else:
            final_res += c
    print(final_res)
