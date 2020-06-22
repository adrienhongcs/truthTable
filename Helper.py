#!/usr/bin/python
'''
@author: adrienhong
Module contains helper functions
'''

def notGate(value):
    '''
    returns the logic NOT of value
    '''
    if (value==1): return 0
    elif (value==0): return 1
    else: return -1

def isOp(op):
    '''
    returns true if op is an operator false otherwise
    note that ! is not considered an operator by this function
    '''
    if (op=='&' or op == '|'or op=='^' or op=='>' or op=='=' ): return True
    else: return False

def precedence(op):
    '''
    returns a number indicating the precedence of an operator and !
    the higher number, the higher the priority
    '''
    if (op=='='):   return 1
    elif (op=='>'): return 2
    elif (op=='|'): return 3
    elif (op=='^'): return 4
    elif (op=='&'): return 5
    elif (op=='!'): return 6
    else: return -1

def evaluate(x,op,y):
    '''
    returns the result of the boolan expression x op y 
    '''
    if (op=='&'): return (x & y)
    elif (op=='|'): return (x | y)
    elif (op=='^'): return (x ^ y)
    elif (op=='|'): return (x | y)
    elif (op=='>'): return (notGate(x) | y)
    elif (op=='='): return  ((x&y) | (notGate(x)&notGate(y)))
    else: return -1

def error(string):
    '''
    prints the error and returns false
    '''
    print(string)
    return False

def peek(stack):
    '''
    returns the current object on top of the stack without removing it
    '''
    if (not stack.empty()):
        top = stack.get()
        stack.put(top)
        return top
    else: return None
