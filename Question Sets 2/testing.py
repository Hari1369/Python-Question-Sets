# 1) Count Odd numbers = [12, 15, 8, 21, 30, 17, 4, 9] output : 4
numbers = [12, 15, 8, 21, 30, 17, 4, 9]
n = len(numbers)
count_number = 0
for i in range(n):
    if numbers[i] % 2 != 0:
        count_number = count_number + 1
print(count_number)

# 2) Find the Largest numbers = [10, 25, 7, 43, 18, 31] output : 43
numbers = [10, 25, 7, 43, 18, 31]
n = len(numbers)
largest_number = numbers[0]
for i in range(n):
    if largest_number < numbers[i]:
        largest_number = numbers[i]
print(largest_number)

# 3) Find the Smallest numbers = [15, 8, 23, 4, 19, 11] output : 4
numbers = [15, 8, 23, 4, 19, 11]
n = len(numbers)
smallest_number = numbers[0]
for i in range(n):
    if smallest_number > numbers[i]:
        smallest_number = numbers[i]
print(smallest_number)

# 4) Calculate Sum Without sum() numbers = [10, 20, 30, 15, 25] output : 100
numbers = [10, 20, 30, 15, 25]
n = len(numbers)
sum_numbers = 0
for i in range(n):
    sum_numbers = sum_numbers + numbers[i]
print(sum_numbers)

# 5) Count Positive, Negative and Zero numbers = [10, -5, 0, 8, -2, 0, 15, -7] 
# Positive: 3
# Negative: 3
# Zero: 2
numbers = [10, -5, 0, 8, -2, 0, 15, -7]
n = len(numbers)
positive_numbers = 0
negative_numbers = 0
zero_numbers = 0
for i in range(n):
    if numbers[i ] > 0:
        positive_numbers = positive_numbers + 1
    elif numbers[i] < 0:
        negative_numbers = negative_numbers + 1
    else:
        zero_numbers = zero_numbers + 1
print(positive_numbers)
print(negative_numbers)
print(zero_numbers)

# 6) Calculate Average numbers = [10, 20, 30, 40, 50] output : 30.0
numbers = [10, 20, 30, 40, 50]
n = len(numbers)
average_number = 0
average = 0
total = 0
for i in range(n):
    average_number = average_number + 1
    total = total + numbers[i]

average = total / average_number
print(average)



# 7) Find the Second Largest numbers = [10, 5, 8, 20, 15] output : 15
numbers = [10, 5, 8, 20, 15]
n = len(numbers)
largest_number = numbers[0]
second_largest_number = 0
for i in range(n):
    if largest_number < numbers[i]:
        second_largest_number = largest_number
        largest_number = numbers[i]
    elif numbers[i] > second_largest_number:
        second_largest_number = numbers[i]
print(second_largest_number)


# 8) Find Duplicate Elements number = [1,2,3,2,4,1,5] output 1 2
numbers = [1,2,3,2,4,1,5]
n1 = len(numbers)
n2 = len(numbers)
for i in range(n1):
    for j in range(i+1, n2):
        if numbers[i] == numbers[j]:
            print("duplicate : ", numbers[j])

 
# 9) Count Frequency of a Given numbers = [10, 20, 10, 30, 10, 40, 20] output : 10 occurs 3 times
numbers = [10, 20, 10, 30, 10, 40, 20]
target = 10
n = len(numbers)
counter = 0
for i in range(n):
    if numbers[i] == target:
        counter = counter + 1
print(target,  "occurs ", counter, "times")


# 10) Separate Even and Odd numbers = [12, 7, 8, 15, 20, 3, 10, 5] output : Even Number = 12 8 20 10 Odd Number = 7 15 3 5 
numbers = [12, 7, 8, 15, 20, 3, 10, 5]
even_number = []
odd_number = []
n = len(numbers)
for i in range(n):
    if numbers[i] % 2 == 0:
        even_number.append(numbers[i])
    else:
        odd_number.append(numbers[i])
print(even_number)
print(odd_number)


# 11) Reverse a List Without numbers = [1, 2, 3, 4, 5, 6] output : [6, 5, 4, 3, 2, 1]
numbers = [1, 2, 3, 4, 5, 6]
reverse_numbers = []
n = len(numbers)
for i in range((n-1), -1, -1):
    reverse_numbers.append(numbers[i])
print(reverse_numbers)


# 12) Find Common Elements list1 = [1, 2, 3, 4, 5] list2 = [3, 5, 7, 9, 1] output : 1 3 5
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9, 1]
n1 = len(list1)
n2 = len(list2)
for i in range(n1):
    for j in range(n2):
        if list1[i] == list2[j]:
            print(list1[i])


# 13) Final Challenge numbers = [10, 5, 20, 5, 30, 10, 40, 20]
numbers = [10, 5, 20, 5, 30, 10, 40, 20]
# Largest number
# Smallest number
# Total
# Number of even numbers
# Number of odd numbers
# Duplicate numbers



largest_number = numbers[0]
n = len(numbers)

duplicate_number = 0
n1 = len(numbers)
for i in range(n):
    for j in range(i+1, n1):
        if numbers[i] == numbers[j]:
            print("Duplicate Numbers are ", numbers[i])


for i in range(n):
    if largest_number < numbers[i]:
        largest_number = numbers[i]
print(largest_number)

smallest_number = numbers[0]
for i in range(n):
    if smallest_number > numbers[i]:
        smallest_number = numbers[i]
print(smallest_number)

total_sum = 0
for i in range(n):
    total_sum = total_sum + numbers[i]
print(total_sum)

count_even = 0
count_odd = 0
for i in range(n):
    if numbers[i] % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
print(count_even)
print(count_odd)

