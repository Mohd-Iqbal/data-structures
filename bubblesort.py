# def bubble_sort(elements):
#     size = len(elements)

#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             if elements[j] > elements[j+1]:
#                 tmp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = tmp
#                 swapped = True
#         if not swapped:
#             break


# elements = [4,8,21,5,7,12,6,9]
# bubble_sort(elements)
# print(elements)


# exercise 
# def bubble_sort(elements,key=None):
#     size = len(elements)

#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             if elements[j][key] > elements[j+1][key]:
#                 tmp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = tmp
#                 swapped = True
#         if not swapped:
#             break

# elements = [
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]

# bubble_sort(elements, key='name')
# print(elements)
