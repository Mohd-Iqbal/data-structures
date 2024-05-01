# def binary_search(number_list,number_to_find):
#     left_index = 0
#     right_index = len(number_list) - 1
#     mid_index = 0

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         number = number_list[mid_index]

#         if number == number_to_find:
#             return mid_index 

#         if number < number_to_find:
#             left_index = mid_index + 1
#         else:
#             right_index = mid_index - 1

#     return -1

# def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
#     if right_index < left_index:
#         return -1

#     mid_index = (left_index + right_index) // 2
#     if mid_index >= len(numbers_list) or mid_index < 0:
#         return -1

#     mid_number = numbers_list[mid_index]

#     if mid_number == number_to_find:
#         return mid_index

#     if mid_number < number_to_find:
#         left_index = mid_index + 1
#     else:
#         right_index = mid_index - 1

#     return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


# numbers_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# binary_search(numbers_list,23)
# binary_search_recursive(numbers_list,23,0,len(numbers_list))


# occurrence of a number
def binary_occurence_recursion(number_list,num_to_find,left_index,right_index):
    if right_index < left_index:
        return -1


    indices = []
    mid_index = (left_index + right_index) // 2
    number = number_list[mid_index]

    if number == num_to_find:
        indices.append(mid_index)
        for i in range(mid_index-2,mid_index+3):
            if i != mid_index and number_list[i] and number_list[i] == number:
                indices.append(i)
        return sorted(indices)
    
    if number < num_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_occurence_recursion(number_list,num_to_find,left_index,right_index)

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
print(binary_occurence_recursion(numbers,15,0,len(numbers)))