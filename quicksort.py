# def swap(elements,a,b):
#     if a != b:
#         elements[a], elements[b] = elements[b], elements[a]

# def partition(elements,start,end):
#     element_index = start
#     element = elements[element_index]

#     while start < end:
#         while start < len(elements) and elements[start] <= element:
#             start += 1
        
#         while elements[end] > element:
#             end -= 1
        
#         if start < end:
#             swap(elements,start,end)

#     swap(elements,element_index,end)

#     return end

# def quicksort(elements,start,end):
#     if start < end:
#         pi = partition(elements,start,end)
#         print(pi)
#         quicksort(elements,start,pi-1)
#         quicksort(elements,pi+1,end)


# items = [5,9,2,1,67,34,88,34]
# quicksort(items,0,len(items) - 1)
# print(items)

def partition(elements,start,end):
    element_index = end
    element = elements[element_index]
    index = end

    while start < end:  
        if elements[start] >= element:
            j = start + 1
            while j <= end:
                if elements[j] <= element:
                    tmp = elements[start] 
                    elements[start] = elements[j]
                    elements[j] = tmp
                    index = start
                    break
                j += 1
        start += 1

    return index
  

def quicksort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quicksort(elements,start,pi-1)        
        quicksort(elements,pi+1,end)        

# items = [72, 25, 49, 13, 81, 2, 1, 37, 64, 56, 98]
items = [11,9,7,2,29,15,28]
quicksort(items,0,len(items)-1)
print(items)

# items = [5,9,2,1,67,34,88,34]
        
