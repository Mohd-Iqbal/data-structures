# expenses = [
#     {"January": 2200},
#     {"February": 2350},
#     {"March": 2600},    
#     {"April": 2130}, 
#     {"May": 2190},
# ]

# # 1. In Feb, how many dollars you spent extra compare to January?
# extra = expenses[1]["February"] - expenses[0]["January"] 
# print(extra)

# # 2. Find out your total expense in first quarter (first three months) of the year.
# total = 0
# for i in range(0,3):
#     expense = list(expenses[i].values())
#     total += expense[0]
# print(total)

# # 3. Find out if you spent exactly 2000 dollars in any month
# for i in expenses:
#     expense = list(i.values())
#     if expense == 2000:
#         print("yes")

# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# new_month = {"June":1980}
# expenses.append(new_month)
# print(expenses)

# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this
# expenses[3]["April"] -= 200
# print(expenses)



# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# heros=['spider man','thor','hulk','iron man','captain america']

# # 1. Length of the list
# print(len(heros))

# # 2. Add 'black panther' at the end of this list
# heros.append('black panther')

# # 3. You realize that you need to add 'black panther' after 'hulk',
# # so remove it from the list first and then add it after 'hulk'
# heros.remove('black panther')
# heros.insert(4,'black panther')
# print(heros)

# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.
# heros[1:3] = ["doctor strange"]
# print(heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
# max = int(input("Enter number "))
# odd_numbers = list()
# for num in range(1,max):
#     if num % 2 != 0:
#         odd_numbers.append(num)

# print(odd_numbers)