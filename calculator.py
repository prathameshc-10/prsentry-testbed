import os
import sys
import json

def calc(a,b,op):
    if op=="add":
        return a+b
    elif op=="sub":
        return a-b
    elif op=="mul":
        return a*b
    elif op=="div":
        if b==0:
            return None
        return a/b

class calculator:
    def __init__(self):
        self.history=[]
    def do_calc(self,x,y,operation):
        result = calc(x,y,operation)
        self.history.append(result)
        return result
    def GetHistory(self):
        return self.history

def main():
    c = calculator()
    print(c.do_calc(5,3,"add"))
    print(c.do_calc(10,0,"div"))
    unused_var = "this does nothing"
    x = 1;y = 2;z = 3
    print(x,y,z)

if __name__=="__main__":
    main()