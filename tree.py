# class TreeNode:
#     def __init__(self,name,designation):
#         self.data = [name,designation]
#         self.children = []
#         self.parent = None

#     def addChild(self,child):
#         child.parent = self
#         self.children.append(child)

#     def get_level(self):
#         p = self.parent
#         level = 0
#         while p:
#             level += 1
#             p = p.parent

#         return level  

#     def print_tree(self,print_value):
#         spaces = " " * self.get_level() * 2
#         prefix = spaces + "!___" if self.parent != None else ""  
#         if print_value == "name":
#             print(prefix + self.data[0])
#         elif print_value == "designation":
#             print(prefix + self.data[1])
#         else:
#             print(prefix + f'''{self.data[0]} ({self.data[1]})''')
#         for child in self.children:
#             child.print_tree(print_value)

# root = TreeNode("Nilpul","CEO")

# cto = TreeNode("Chinmay","CTO")
# infra_head = TreeNode("Vishwa","Infrastructure Head")
# infra_head.addChild(TreeNode("Dhaval","Cloud Manager"))
# infra_head.addChild(TreeNode("Abhijit","App Manager"))
# cto.addChild(infra_head)
# cto.addChild(TreeNode("Amir","Application Head"))
# hr_head = TreeNode("Gels","HR Head")
# hr_head.addChild(TreeNode("Peter","Recruitment Manager"))
# hr_head.addChild(TreeNode("Waqas","Policy Manager"))

# root.addChild(cto)
# root.addChild(hr_head)

# root.print_tree("designation")


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent

        return level  

    def print_tree(self,level):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "!___" if self.parent != None else ""  
        print(prefix + self.data)
        for child in self.children:
            if self.get_level() < level:
                child.print_tree(level)


root = TreeNode("Global")

#India
india = TreeNode("India")
gujrat = TreeNode("Gujrat")
karnataka = TreeNode("Karnataka")
gujrat.addChild(TreeNode("Ahmedabad"))
gujrat.addChild(TreeNode("Baroda"))
karnataka.addChild(TreeNode("Bangluru"))
karnataka.addChild(TreeNode("Mysore"))
india.addChild(gujrat)
india.addChild(karnataka)

#USA
usa = TreeNode("USA")
new_jersey = TreeNode("New Jersey")
california = TreeNode("California")
new_jersey.addChild(TreeNode("Princeton"))
new_jersey.addChild(TreeNode("Trenton"))
california.addChild(TreeNode("San Francisco"))
california.addChild(TreeNode("Mountain View"))
california.addChild(TreeNode("Palo Alto"))
usa.addChild(new_jersey)
usa.addChild(california)

root.addChild(india)
root.addChild(usa)

root.print_tree(2)