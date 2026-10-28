# def add(a,b):
#     return a+b
# a = add(1,2)
# print(a)
from itertools import count
from selectors import SelectSelector
from tkinter import commondialog

# def check_even_odd(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# a = check_even_odd(2,3)

# def factorial(n):
#     if ns == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# b = factorial(4)
# print(b)

# def count_digits(num):
#     count = 0
#     for num in str(num):
#         count += 1
#     return count
# print(count_digits(5867))


# def main():
#     numbers = 5843
#     count = 0
#     for number in str(numbers):
#             count += 1
#     print(count)
# main()


# def count_digits(a):
#     count = 0
#     while a > 0:
#         a = a // 10
#         count += 1
#     return count
# print(count_digits(123))


# def common_elements(list1, list2):
#     common = []
#     for element in list1:
#         if element in list2:
#             if element not in common:
#                 common.append(element)
#
#     return common
# list1 = [2,1,4,5]
# list2 = [6,7,1,4]
# print(common_elements(list1, list2))

# def count_types(list):
#     count_negatives = 0
#     count_positives = 0
#     count_zeros = 0
#     for item in list:
#         if item == 0:
#             count_zeros += 1
#         elif item > 0:
#             count_positives += 1
#         else:
#             count_negatives += 1
#     return count_negatives, count_positives, count_zeros
# print(count_types([1,-3,0,4,-8,0]))


def frequency(list):
     count_ones = 0
     count_twos = 0
     count_threes = 0
     for item in list:
         if item == 1:
             count_ones += 1
             print(f"1 appears {count_ones} times")
         elif item == 2:
             count_twos += 1
             print(f"2 appears {count_twos} times")
         elif item == 3:
             count_threes += 1
             print(f"3 appears {count_threes} times")
     return count_ones, count_twos, count_threes

frequency([1, 2, 3])