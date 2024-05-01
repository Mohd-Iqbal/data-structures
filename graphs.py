# class Graph:
#     def __init__(self,edges):
#         self.edges = edges
#         self.graph_dict = {}
#         for start,end in self.edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end]
#         print(self.graph_dict)
        
#     def get_paths(self,start,end,path=[]):
#         path = path + [start]

#         if start == end:
#             return [path]
        
#         if start not in self.graph_dict:
#             return []

#         paths = []

#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_paths = self.get_paths(node, end, path)
#                 for p in new_paths:
#                     paths.append(p)

#         return paths
    
#     def shortest_path(self,start,end,path = []):
#         path = path + [start]

#         if start == end:
#             return path

#         if start not in self.graph_dict:
#             return None
        
#         shortest_path = None
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 sp = self.get_paths(node, end, path)
#                 if sp:
#                     if shortest_path is None or len(sp) < len(shortest_path):
#                         shortest_path = sp

#         return shortest_path


        

# routes = [
#     ("Mumbai","Paris"),
#     ("Mumbai","Dubai"),
#     ("Paris","Dubai"),
#     ("Paris","New York"),
#     ("Dubai","New York"),
#     ("New York","Toronto")
# ]

# route_graph = Graph(routes)
# # route_graph.get_paths("Mumbai","New York")
# print(route_graph.get_paths("Mumbai","New York"))
# print(route_graph.shortest_path("Mumbai","New York"))


class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)
        
    def get_paths(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    def traverse_graph(self,start,nodes=[]):
        nodes += [start]

        for neighbor in self.graph_dict[start]:
            if neighbor not in nodes:
                self.traverse_graph(neighbor,nodes)

        return nodes
routes = [
    ("A","B"),
    ("A","C"),
    ("B","A"),
    ("B","D"),
    ("B","E"),
    ("C","A"),
    ("C","F"),
    ("D","B"),
    ("E","B"),
    ("E","F"),
    ("F","C"),
    ("F","E")
]

route_graph = Graph(routes)
print(route_graph.traverse_graph("D"))
