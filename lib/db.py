import os
import random
path = "pages/"
abc = "abcdefghijklmnopqrstuvwxyz"

def getString():
    f = random.randrange
    return abc[f(26)] + abc[f(26)] + abc[f(26)] + abc[f(26)] +  abc[f(26)]

class Database():
    ''' 
    This is a database specifically designed to hold pages of 
    data arranged in a specific format.

    For example::

        Title
        Line 001
        Line 002
        ...
    '''
    def __init__(self):
        ''' Set up the initial class'''
        self.cache = {}
        self.keys = os.listdir(path)

    def load(self, key):
        '''Open the file containing the data from key'''
        if key in self.cache:
            result = self.cache[key]
        else:
            file = open(path+key, 'r')
            result = file.readlines()
            file.close()
            self.cache[key] = result
        title = result[0][:-1]
        content = result[1:]
        return title, content

    def save(self, key, title, content):
        data = [title + '\n'] + content
        self.cache[key] = data
        if key not in self.keys:
            self.keys.append(key)
        file = open(path+key)
        file.writelines(data)
        file.close()

    def new(self, title, content):
        key = getString()
        while key in self.keys:
            key = getString()
        self.save(key, title, content)

    def list(self):
        dummy = []
        for item in self.keys:
            if item in self.cache:
                dummy.append((item, self.cache[item][0][:-1]))
            else:
                dummy.append((item, "<Unknown>"))
        return dummy