from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    str = ''
    while not stack.is_empty():
        str += stack.pop()
    return str

def is_balanced(s):
    dict = {
        "}":"{",
        ")":"(",
        "]":"[",
    }

    stack = Stack()
    
    for ch in s:
        if ch == '{' or ch == '(' or ch == "[":
            stack.push(ch)        
        if ch == '}' or ch == ')' or ch == "]":
            if dict[ch] == stack.peek():
                stack.pop()
    
    if stack.is_empty():
        return True
    else:
        return False

def next_greater(arr):
    stack = Stack()
    new_array = list()
    for idx,i in enumerate(arr):
        present = False
        if stack.is_empty():
            stack.push(i)
            for i in range(idx + 1,len(arr)):
                if arr[i] > stack.peek():
                    stack.pop()
                    new_array.append(arr[i])
                    present = True
                    break
            if not present:
                new_array.append(-1)
                stack.pop()        
    return new_array



    
# array = next_greater([1, 3, 2, 4])
# print(array)
# stack = Stack()
# stack.push("We will conquere COVID-19")
# reverse = reverse_string("We will conquere COVID-19")
# print(reverse)

