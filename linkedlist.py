# class Node:

#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next

# class LinkedList:

#     def __init__(self):
#        self.head = None

#     def insert_at_begining(self,data):
#         node = Node(data, self.head)
#         self.head = node

#     def print(self):
#         if self.head is None:
#             print("linkedlist is empty")
#             return
        
#         itr = self.head
#         while itr:
#             print(itr.data)
#             itr = itr.next

#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head
#         while itr.next:
#             itr = itr.next            

#         itr.next = Node(data,None)        
    
#     def insert_values(self,data_list):
#         self.head = None

#         for i in data_list:
#            self.insert_at_end(i)

#     def get_length(self):

#         itr = self.head
#         counter = 0
#         while itr:
#             counter += 1
#             itr = itr.next

#         return counter
    
#     def remove_at(self,index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index == 0:
#             self.head = self.head.next
#             return
                
#         counter = 0
#         itr = self.head
#         while itr:
#             if counter == index - 1:
#                 itr.next = itr.next.next
#                 break
#             counter += 1
#             itr = itr.next

#     def insert_at(self,index,data):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index == 0:
#             self.insert_at_begining(data)
#             return
                
#         counter = 0
#         itr = self.head
#         while itr:
#             if counter == index - 1:
#                 new_node = Node(data,itr.next)
#                 itr.next = new_node
#                 break
#             counter += 1
#             itr = itr.next
     
#     def insert_after_value(self, data_after, data_to_insert):
#         if self.head is None:
#             return

#         if self.head.data == data_after:
#             self.head.next = Node(data_to_insert,self.head.next) 
#             return
        
#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 itr.next = Node(data_to_insert, itr.next)
#                 break
#             itr = itr.next

#     def remove_by_value(self, data):
#         if self.head is None:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return

#         itr = self.head
#         while itr:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next



# linkedlist = LinkedList()
# linkedlist.insert_at_end(5)
# linkedlist.insert_at_end(6)
# linkedlist.insert_at_end(7)
# linkedlist.print()
# # # linkedlist.insert_values(["banana","mango","grapes","orange"])
# # # linkedlist.print()
# # # linkedlist.insert_after_value("mango","apple")
# # # linkedlist.print()
# # # linkedlist.remove_by_value("orange")
# # # linkedlist.print()

# # doubly linked list 
# class Node:
#     def __init__(self, val, next=None, prev=None):
#        self.val = val
#        self.next = next
#        self.prev = prev


# class MyLinkedList:

#     def __init__(self):
#        self.head = None

#     def get_length(self) -> int:
#       count = 0
#       itr = self.head
#       while itr:
#         count += 1
#         itr = itr.next
#       return count
  
#     def get(self, index: int) -> int:
#       if index < 0 or index >= self.get_length():
#         raise IndexError("Index out of range")
  
#       count = 0
#       itr = self.head
#       while itr:
#         if index == count:
#           return itr.val
#         count += 1
#         itr = itr.next
  
#     def addAtHead(self, val: int) -> None:
#       if self.head is None:
#         self.head = Node(val, None, None)
#       else:
#         node = Node(val, self.head, None)
#         self.head.prev = node
#         self.head = node
  
#     def addAtTail(self, val: int) -> None:
#       if self.head is None:
#         self.head = Node(val, None, None)
#         return
  
#       itr = self.head
#       while itr.next:
#         itr = itr.next
  
#       itr.next = Node(val, None, itr)
  
#     def addAtIndex(self, index: int, val: int) -> None:
#       if index < 0 or index > self.get_length():
#         raise IndexError("Index out of range")
  
#       if index == 0:
#         self.addAtHead(val)
#         return
  
#       count = 0
#       itr = self.head
#       while itr:
#         if count == index - 1:
#           node = Node(val, itr.next, itr)
#           if itr.next:
#             itr.next.prev = node
#           itr.next = node
#           break
#         count += 1
#         itr = itr.next
  
#     def deleteAtIndex(self, index: int) -> None:
#       if index < 0 or index >= self.get_length():
#         raise IndexError("Index out of range")
  
#       if index == 0:
#         self.head = self.head.next
#         if self.head:
#           self.head.prev = None
#         return
  
#       count = 0
#       itr = self.head
#       while itr:
#         if count == index:
#           itr.prev.next = itr.next
#           if itr.next:
#             itr.next.prev = itr.prev
#           break
#         count += 1
#         itr = itr.next

#     def insert_values(self, data_list):
#         self.head = None
#         for i in data_list:
#             self.addAtTail(i)

#     def print_forward(self):
#         if self.head is None:
#             print("linkedlist is empty")
#             return
        
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.val) + ' --> '
#             itr = itr.next
#         print(llstr)        

#     def print_backward(self):
#         if self.head is None:
#             print("linkedlist is empty")
#             return

#         last_node = self.get_last_node()
#         llstr = ''
#         while last_node:
#             llstr += str(last_node.val) + ' --> '
#             last_node = last_node.prev
#         print(llstr)        

        
#     def get_last_node(self):
#         itr = self.head
#         while itr.next:
#             itr = itr.next

#         return itr

# Your MyLinkedList object will be instantiated and called as such:
# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(1)
# myLinkedList.addAtTail(3)
# myLinkedList.addAtIndex(1, 2)
# myLinkedList.deleteAtIndex(1)
# data = myLinkedList.get(1)
# myLinkedList.print_forward()
# myLinkedList.print_backward()

# this is more efficient and has been tested
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class MyLinkedList:

#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
    
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current.val

#     def addAtHead(self, val: int) -> None:
#         new_node = Node(val, self.head)
#         self.head = new_node
#         self.size += 1
        

#     def addAtTail(self, val: int) -> None:
#         if self.head is None:
#             self.head = Node(val,None)
#             self.size += 1
#             return
            
#         itr = self.head
#         while itr.next:
#             itr = itr.next
            
#         itr.next = Node(val,None)
#         self.size += 1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return
            
#         if index == 0:
#             self.addAtHead(val)
#             self.size += 1
#             return
                
#         current = self.head
#         for _ in range(index - 1):
#             current = current.next
#         node = Node(val,current.next)
#         current.next = node
#         self.size += 1

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
            
#         if index == 0:
#             self.head = self.head.next
#             self.size -= 1
#             return
                
#         current = self.head
#         for _ in range(index - 1):
#             current = current.next    
#         current.next = current.next.next
#         self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(60)
# obj.addAtTail(30)
# param_1 = obj.get(1)
# print(param_1)
# obj.addAtIndex(1,50)
# obj.deleteAtIndex(1)

# palindrome: this is palindrome 1 --> 2 --> 3 --> 4 --> 3 --> 2 --> 1 --> 
class Node:
    def __init__(self, val=0, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Linkedlist:
    
    def __init__(self):
       self.head = None

    def add_at_begining(self,val):
       self.head = Node(val,self.head,None)

    def add_at_end(self,val):
        if self.head is None:
           self.head = Node(val,self.head,None)
           return
       
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(val,None,current)

    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count
    
    def last_node(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.val) + ' --> '
            itr = itr.next
        print(llstr)        


    def palindrome(self):
        nodes = self.size()
        halve_nodes = nodes // 2
        correct = list()
        forward = self.head
        backward = self.last_node()
        for _ in range(halve_nodes):
            if forward.val == backward.val:
                correct.append(forward.val)
                forward = forward.next
                backward = backward.prev
        if correct and len(correct) == halve_nodes:
            return True
        else:
            return False
            

linkedlist = Linkedlist()
linkedlist.add_at_begining(6)
linkedlist.add_at_begining(5)
linkedlist.add_at_begining(4)
linkedlist.add_at_begining(3)
linkedlist.add_at_begining(2)
linkedlist.add_at_begining(1)
linkedlist.add_at_end(5)
linkedlist.add_at_end(4)
linkedlist.add_at_end(3)
linkedlist.add_at_end(2)
linkedlist.add_at_end(1)
linkedlist.print()
print(linkedlist.palindrome())