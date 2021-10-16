#!/usr/bin/env python
# coding: utf-8

# In[13]:


# JAMEEL KHALID
# 200901082
# BS-CS-01-B

from collections import deque


class Stack:

    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def top(self):
        return self.container[-1]

stack = Stack()
equ = input("Enter Equation: ")
condition = True
x = 0
try:
    for i in equ:
        if i =='[' or i=='(' or i=='{':
            stack.push(i)
        elif i ==']' or i==')' or i=='}':
            stack.pop()
    if stack.size()==0:
        for i in range(0, len(equ)):
            if equ[i] == '"':
                if x % 2 == 0:
                    x += 1
                    if equ[i+1] ==')'or equ[i+1] ==']'or equ[i+1] =='}'or equ[i+1] =='"':
                        condition = False
                    else:
                        condition = True
                else:
                    condition = True
                    x += 1

    if x % 2 == 0:
        condition = True
    else:
        condition = False
    if condition:
        print("True")
    else:
        print("False")
except:
    print("False")





# In[ ]:





# In[ ]:




