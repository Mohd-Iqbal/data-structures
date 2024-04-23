class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
           return
       
        if data < self.data:
            if self.left:
               self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
               self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self,val):
        if self.data == val:
            return True 
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False                
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def pre_order_transversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_transversal()

        if self.right:
            elements += self.right.pre_order_transversal()

        return elements
    
    def post_order_transversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_transversal()

        if self.right:
            elements += self.right.post_order_transversal()

        elements.append(self.data)

        return elements
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def min_value(self):
        min = self.data
        if self.left:
           min = self.left.min_value()

        return min
    
    def min_value(self):
        min = self.data
        if self.left:
           min = self.left.min_value()

        return min
    
    def max_value(self):
        max = self.data
        if self.right:
           max = self.right.max_value()

        return max

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

numbers = build_tree([3, 7, 2, 8, 10, 5, 1])
# print(numbers.search(44))
print(numbers.in_order_traversal())
# print(numbers.pre_order_transversal())
# print(numbers.post_order_transversal())
# print(numbers.calculate_sum())
# print(numbers.min_value())
# print(numbers.max_value())