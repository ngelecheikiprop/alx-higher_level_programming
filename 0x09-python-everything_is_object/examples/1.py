#!/usr/bin/python3
numbers = [1, 2, 3, 4, 5, 6]

# for index in range(len(numbers)):
#     numbers[index] = numbers[index] ** 2

# print(numbers)

for index, value in enumerate(numbers):
    numbers[index] = value ** 2
