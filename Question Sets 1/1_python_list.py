#=========================================================================================================#
#=========================================== QUESTIONS ON LIST ============================================#
#=========================================================================================================#

# 1) Create a list of numbers from 1 to 10 and print it.
number = [1,2,3,4,5,6,7,8,9,10]
print(number)
del number
print("=============================================================>\n")

# 2) Access the 3rd element of a list containing random values.
number = [1,2,3,4,5,6,7,8,9,10]
print(number[3])
del number
print("=============================================================>\n")

# 3) Reverse a list without using the built-in reverse function.
number = [1,2,3,4,5,6,7,8,9,10]
rev_numbers = []
print(number)  # ========> [1,2,3,4,5,6,7,8,9,10]
start = -1
stop = len(number) - 1
step = -1
for i in range(start, stop, step):
	print(number[i])
	rev_numbers.append(number[i])
print(rev_numbers)  # ========> [10,9,8,7,6,5,4,3,2,1]

del number
del rev_numbers
del start
del stop
del step
print("=============================================================>\n")

# 4) Find the maximum and minimum elements in a list.
number = [1,2,3,4,5,6,7,8,9,10]
max_number = max(number)
min_number = min(number)
print("MAX NUMBER : " + str(max_number))  # ========> MAX NUMBER : 10
print("MIN NUMBER : " + str(min_number))  # ========> MIN NUMBER : 1

del number
del max_number
del	min_number
print("=============================================================>\n")

# 5) Remove all duplicate values from a list while maintaining the order.
number = [0,1,2,1,2,3,4,5,6,7,8,9,10,10,11]
filter_number = []
start = 0
stop = len(number)
step = 1
for i in range(start, stop, step):
	if number[i] not in filter_number:
		filter_number.append(number[i])
	# else:
	# 	print(number[i])
print("FILTER LIST : " + str(filter_number))  # ========> OUTPUT: FILTER LIST : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

del number
del filter_number
del start
del stop
del step
print("=============================================================>\n")

# 6) Sort a list of strings alphabetically.
fruits = ["Mango","Banana","Apple","Orange","Kiwi","Cherry"]
start = 0
stop = len(fruits)
step = 1
for i in range(start, stop, step):
    for j in range(start, stop - i - 1, step):
        if fruits[j] > fruits[j + 1]:
            fruits[j], fruits[j + 1] = fruits[j + 1], fruits[j]
print(fruits)  # ========> OUTPUT: ["Apple","Banana","Cherry","Kiwi","Orange"]

del fruits
del start
del stop
del step
print("=============================================================>\n")

# 7) Find the index of the first occurrence of an element in a list.
fruits = ["apple","banana","banana","mango","apple"]
elements = "banana"
start = 0
stop = len(fruits)
step = 1
for i in range(start, stop, step):
	if fruits[i] == elements:
		print("INDEX :", i)  #========> OUTPUT: INDEX : 1
		break 
      
del fruits
del start
del stop
del step
print("=============================================================>\n")

# 8) Count the frequency of each element in a list.
fruits = ["apple","banana","banana","kiwi","apple"]
elements = {}
start = 0
stop = len(fruits)
step = 1
for i in range(start, stop, step):
    if fruits[i] in elements:
        elements[fruits[i]] += 1
    else:
        elements[fruits[i]] = 1
print(elements)  #========> OUTPUT: {"apple":2, "banana":2,"kiwi":1}

del fruits
del elements
del start
del stop
del step
print("=============================================================>\n")
			 
# 9) Join all list elements into a single string.
mine = ["This", "is", "Hari"]
result = ""
start = 0 
stop = len(mine)
step = 1

for i in range(start, stop, step):
    result += mine[i]
    if i != stop - 1:
        result += " "
print("RESULT: " + str(result))  # ========> RESULT: This is Hari

del mine
del start
del stop
del step
del result
print("=============================================================>\n")

# 10) Split a list into two sublists: one containing even numbers and the other containing odd numbers.
number = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
start = 0
stop = len(number)
step = 1
for i in range(start, stop, step):
      if number[i] % 2 == 0:
            even.append(number[i])
      else:
            odd.append(number[i])

print("EVEN NUMBER : " + str(even))  # ========> EVEN NUMBER : [2, 4, 6, 8, 10]
print("ODD NUMBER  : " + str(odd))  # ========> ODD NUMBER  : [1, 3, 5, 7, 9]

del number
del even
del odd
del start
del stop
del step
print("=============================================================>\n")

# Example: [[1,2],[3,4,5],[6]]  -> [1,2,3,4,5,6]
nested = [[1,2],[3,4,5],[6]]
# 11) Write code to flatten it into a single list.

start_1 = 0
stop_1 = len(nested)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    start_2 = 0
    stop_2 = len(nested[i])
    step_2 = 1
    for j in range(start_2, stop_2, step_2):
        print("DATA : ", nested[i][j])
print("=============================================================>\n")

# 12) Remove duplicates and sort the list in descending order
number = [4, 5, 2, 2, 9, 1, 4, 5]
duplicate = []
reverse = []

start_1 = 0
stop_1 = len(number)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if number[i] in duplicate:
        pass
    else:
        duplicate.append(number[i])

start_2 = 0
stop_2 = len(duplicate)
step_2 = 1

start_3 = 0
stop_3 = len(duplicate) - 1
step_3 = 1

for k in range(start_2, stop_2, step_3):
    for j in range(start_3, stop_3, step_3):
        if duplicate[j] < duplicate[j + 1]:
            duplicate[j], duplicate[j+1] = duplicate[j+1], duplicate[j]

print(duplicate)

del start_1
del stop_1
del step_1

del start_2
del stop_2
del step_2

del start_3
del stop_3
del step_3

del duplicate
del reverse

del number
print("=============================================================>\n")

# 13) Return all indices where "apple" appears
fruits = ["apple","banana","mango","apple","banana","apple"]
element = "apple"
fruits_array = []
# Expected Output: [0, 3, 5]

start_1 = 0
stop_1 = len(fruits)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if fruits[i] == element:
        fruits_array.append(i)

print(fruits_array)


del start_1
del stop_1
del step_1

del fruits
del fruits_array
del element
print("=============================================================>\n")

# 14) Check if the list reads the same forwards and backwards
number = [1, 2, 3, 2, 1]

start_1 = 0
stop_1 = len(number)
step_1 = 1

left = 0
right = len(number) - 1

for i in range(start_1, stop_1, step_1):
    if number[left] != number[right]:
        print("IT IS NOT A PALINDROME")
        break

    left = left + 1
    right = right -1

else:
    print("IT IS PALINDROME")

del start_1
del stop_1
del step_1

del left
del right

del number
print("=============================================================>\n")

# 15) Merge them into one list without duplicate values
# Expected Output: [1, 2, 3, 4, 5, 6]
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = []

start_1 = 0
stop_1 = len(list1)
step_1 = 1

start_2 = 0
stop_2 = len(list2)
step_2 = 1

for i in range(start_1, stop_1, step_1):
    if list1[i] in list3:
        break
    else:
        list3.append(list1[i])


for j in range(start_2, stop_2, step_2):
    if list2[j] in list3:
        pass
    else:
        list3.append(list2[j])

print(list3) # Output: [1, 2, 3, 4, 5, 6]

del list1
del list2
del list3

del start_1
del stop_1
del step_1

del start_2
del stop_2
del step_2
print("=============================================================>\n")

# 16) Find the second largest unique number
number = [4, 7, 1, 9, 0, 9, 5]
duplicate = []

start_1 = 0
stop_1 = len(number)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if number[i] not in duplicate:
            duplicate.append(number[i])

start_2 = 0
stop_2 = len(duplicate)
step_2 = 1

start_3 = 0
stop_3 = len(duplicate) - 1
step_3 = 1

for j in range(start_2, stop_2, step_2):
    for k in range(start_3, stop_3, step_3):
        if duplicate[k] < duplicate[k + 1]:
            duplicate[k], duplicate[k + 1] = duplicate[k + 1], duplicate[k]
start_4 = 0
stop_4 = len(duplicate) -1
step_4 = 1
max_value = duplicate[0]

for i in range(start_4, stop_4, step_4):
    if duplicate[i] < duplicate[0]:
        max_value = duplicate[i]
        break
    
print("SECOND LARGEST VALUE : ", max_value)
print("=============================================================>\n")

# 17) Print all pairs (a,b) where a+b == target_sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10

start_1 = 0
stop_1 = len(numbers)
step_1 = 1

start_2 = 0
stop_2 = len(numbers)
step_2 = 1

for i in range(start_1, stop_1, step_1):
    for j in range(i, stop_2, step_2):
        if (numbers[i] + numbers[j]) == target_sum:
            print(f"({numbers[i]}, {numbers[j]})")
print("=============================================================>\n")
            
# 18) Find the element that occurs most frequently
# Expected Output: 1
number = [1,2,3,1,2,1,4,5,1]
start_1 = 0 
stop_1 = len(number) 
step_1 = 1

start_2 = 0 
stop_2 = len(number) 
step_2 = 1

max_count = 0
most_frequent = None
for i in range(start_1, stop_1, step_1):
    counter = 0
    for j in range(start_2, stop_2, step_2):
        if number[i] == number[j]:
            counter = counter + 1
    if counter > max_count:
        max_count = counter
        most_frequent = number[i]

print("FREQUENT COUNT : ", most_frequent)

del start_1
del stop_1
del step_1

del start_2
del stop_2
del step_2

del counter
del max_count
del most_frequent

del number
print("=============================================================>\n")


# 19) Create a list of squares of even numbers from 1 to 20 using list comprehension
# Expected Output: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = []
square_number = []

start_1 = 0
stop_1 = len(number)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if number[i] % 2 == 0:
        even_numbers.append(number[i])

start_2 = 0
stop_2 = len(even_numbers)
step_2 = 1

for j in range(start_2, stop_2, step_2):
    value = even_numbers[j] * even_numbers[j]
    square_number.append(value)

print("SQUARE VALUE : ", square_number)

del start_1
del stop_1
del step_1

del start_2
del stop_2
del step_2

del number
del even_numbers
del square_number
print("=============================================================>\n")


# 20) Rotate the list to the right by k positions
# Expected Output: [5,6,7,1,2,3,4]
number = [1,2,3,4,5,6,7]
k = 3

start_1 = 0
stop_1 = k
step_1 = 1

for i in range(start_1, stop_1, step_1):
    start_2 = len(number) -1
    stop_2 = 0
    step_2 = -1
    for j in range(start_2, stop_2, step_2):
        number[j], number[j-1] = number[j-1], number[j]
    
print(number)
