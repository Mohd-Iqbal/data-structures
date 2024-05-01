# 1) Write a Python program to calculate the sum of a list of numbers using recursion.
# def sum(arr,n):
#     if n == 0:
#         return arr[n]
#     return arr[n] + sum(arr,n-1)

# list = [1,2,3,4,5,6,7,8,9]
# print(sum(list,len(list)-1))

# 2) Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3,4], [5,6]]
# def sum(arr,n):
#     if n < 0:
#         return 0 

#     total = 0
#     if isinstance(arr[n], int):
#         total = arr[n]
        
#     if isinstance(arr[n], list):
#        total = sum(arr[n],len(arr[n])-1)
            
#     return total + sum(arr,n-1)
    

# array = [1, 2, [3,4], [5,6]]
# print(sum(array,len(array)-1))

# 3) Write a Python program to get the factorial of a non-negative integer using recursion.
# def factorial(n):
#     if n == 1:
#         return n 
#     return n * factorial(n-1)
    

# print(factorial(6))

# 4 )Write a Python program to get the sum of a non-negative integer using recursion.
# def sum(n):
#     if n == 0:
#         return 0 
#     return n % 10 + sum(int(n / 10))
    
# print(sum(667))


# 5) Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion
# def sum(n):
#     if n == 0 or n == 1:
#         return n 
#     return n + sum(n-2)
    
# print(sum(11))

# 6) Write a  Python program to calculate the sum of harmonic series upto n terms.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# def sum(n):
#     if n == 1:
#         return n 
#     return 1/n + sum(n-1)
    
# print(sum(7))


# 6) Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
# def multiply(n,times):
#     if times == 1:
#         return n
#     return n * multiply(n,times-1)
    
# print(multiply(3,10))

# 7) Write a  Python program to find the greatest common divisor (GCD) of two integers using recursion.
def divisor(a,b, times):
    if times == 0:
        return 

    if a % times == 0 and b % times == 0:
        return times
    else:
        return divisor(a,b,times-1)
    
print(divisor(12,14,12))
