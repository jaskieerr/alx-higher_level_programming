#!/usr/bin/python3
'''shbang'''


class MyInt(int):
    '''rebel rebell by david bowie'''
    def __new__(cls, *args, **kwargs):
        '''creating instance'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''reverse op'''
        return int(self) != other

    def __ne__(self, other):
        '''anotherone'''
        return int(self) == other
