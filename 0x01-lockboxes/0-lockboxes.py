#!/usr/bin/python3
'''contain a method that determines if all the boxes can be opened.'''


def canUnlockAll(boxes):
    '''Return True if all boxes can be opened, else return False'''
    n = len(boxes)
    for i in range(0, n - 1):
        opened = False
        j = 0
        for s in boxes:
            if (i + 1) in s and (i + 1) != j:
                opened = True
                break
            j += 1
        if not :
            return False
    return True
