import threading
import time
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()    

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

# q = Queue()
# def place_order():
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     for order in orders:
#         print("Placing order for:",order)
#         q.enqueue(order)
#         time.sleep(0.5)
    

# def serve_order():
#     time.sleep(1)
#     while not q.is_empty():
#         time.sleep(2)
#         food = q.dequeue()
#         print(food)

# place = threading.Thread(target=place_order)
# serve = threading.Thread(target=serve_order)
# place.start()
# serve.start()

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()    

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

def binary_change(n):
    q = Queue()
    q.enqueue("1")

    for i in range(n):
        front = q.front() 
        print(front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")

        q.dequeue()

binary_change(10)
