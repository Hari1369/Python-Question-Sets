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

