#!/usr/bin/python3
'''shebang'''


class Student:
    '''creatin student class'''
    def __init__(self, first_name, last_name, age):
        '''initin it'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''rtfmmm'''
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
 
    def reload_from_json(self, json):
        '''replacees student attrs'''
        for k, v in json.items():
            setattr(self, k, v)
