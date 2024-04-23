# class HashTable:  
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]
        
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
    
#     def __getitem__(self, index):
#         h = self.get_hash(index)
#         return self.arr[h]
    
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val    
        
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         self.arr[h] = None    


# hash_table = HashTable()
# hash_table["march 6"] = 430
# # print(hash_table["march 6"])

# # problem create the dictionary with keys as this poem word and value as the number of times key present
# # this sorting this extra layer
# poem  = f"""Two roads diverged in a yellow wood,
# And sorry I could not travel both
# And be one traveler, long I stood
# And looked down one as far as I could
# To where it bent in the undergrowth;

# Then took the other, as just as fair,
# And having perhaps the better claim,
# Because it was grassy and wanted wear;
# Though as for that the passing there
# Had worn them really about the same,

# And both that morning equally lay
# In leaves no step had trodden black.
# Oh, I kept the first for another day!
# Yet knowing how way leads on to way,
# I doubted if I should ever come back.

# I shall be telling this with a sigh
# Somewhere ages and ages hence:
# Two roads diverged in a wood, and I—
# I took the one less traveled by,
# And that has made all the difference."""

# array_string = [word.rstrip('.') for word in poem.split()]
# dictionary = {}
# for i in array_string:
#     if i in dictionary:
#         dictionary[i] += 1
#     else: 
#         dictionary[i] = 1
# sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
# keys = list(sorted_dict.keys())
# # top three most repeated words in the list top_three
# top_three = [keys[0],keys[1],keys[2]]
# # print(top_three)


# linear probing 
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        for i in self.arr:
            if i is not None:
                if i[0] == key:
                    return i
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h] = (key,val)
        elif self.arr[h][0] and self.arr[h][0] == key:
            self.arr[h] = (key,val)
        else:
            found = False
            for i in range(h,len(self.arr)):
                if self.arr[i] == None:
                    self.arr[i] = (key,val)
                    found = True
                    break
            if not found:
                for i in range(0,len(self.arr)):
                    if self.arr[i] == None:
                        self.arr[i] = (key,val)
                        found = True
                        break

    def __delitem__(self, key):
        for idx,i in enumerate(self.arr):
            if i is not None:
                if i[0] == key:
                    del self.arr[idx]



hash_map = HashTable()
hash_map["march 6"] = 40
hash_map["march 17"] = 50
hash_map["march 7"] = 60
print(hash_map["march 7"])
del hash_map["march 17"]
print(hash_map.arr)    

# this is more suitable solution to handle linear probing
class HashTable:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)

# note: we use numerate for getting index as well from the Iterable
# note: range(0,7) this function creates a range of numbers starting from 0 to 6, 7 is exclusive and if we use *range(0,7) then this will turn the range object (defaul return value) to list 
