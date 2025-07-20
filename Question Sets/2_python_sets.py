#=========================================================================================================#
#=========================================== QUESTIONS ON SETS ============================================#
#=========================================================================================================#

# 1) Create a set from a list of numbers, ensuring no duplicates.
number = {1,2,3,4,5,6,7,8,9,10}
print(number) # =======> outpur: {1,2,3,4,5,6,7,8,9,10}
del number
print("=============================================================>\n")

# 2) Check if a set is a subset of another set.
# ===================================> Method 1:-
number_1 = {1, 2, 3, 4}
number_2 = {1, 2, 3, 4, 5, 6, 7, 8}
new_union = set()

number_1 = list(number_1)
number_2 = list(number_2)

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

start_2 = 0
stop_2 = len(number_2)
step_2 = 1  

for i in range(start_1, stop_1, step_1):
    new_union.add(number_1[i])

for i in range(start_2, stop_2, step_2):
    if number_2[i] not in new_union:
        new_union.add(number_2[i])

print(new_union)  # =======> output: {1, 2, 3, 4, 5, 6, 7, 8}

del number_1
del number_2
del new_union
del start_1, start_2
del step_1, step_2
del stop_1, stop_2

# ===================================> Method 2:-
number_1 = {1,2,3,4}
number_2 = {1,2,3,4,5,6,7,8}
new_union = set()
for i in number_1:
	new_union.add(i)
for i in number_2:
	if i not in new_union:
		new_union.add(i) 

print(new_union) # =======> output: {1, 2, 3, 4, 5, 6, 7, 8}

del number_1
del number_2
del new_union
print("=============================================================>\n")


# 3) Find the intersection of two sets.
# ===================================> Method 1:-
number_1 = list({1, 2, 3, 4, 5, 6, 7})
number_2 = list({4, 5, 9, 7, 2, 8, 9, 10})

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

start_2 = 0
stop_2 = len(number_2)
step_2 = 1  

intersection_set = set()

for i in range(start_1, stop_1, step_1):
    for j in range(start_2, stop_2, step_2):
        if number_1[i] == number_2[j]:
            intersection_set.add(number_1[i])
print(intersection_set)

del number_1
del number_2
del intersection_set

# ===================================> Method 2:-
number_1 = {1, 2, 3, 4, 5, 6, 7}
number_2 = {4, 5, 9, 7, 2, 8, 9, 10}

intersection_set = set()
for i in number_1:
    for j in number_2:
        if i == j:
            intersection_set.add(i)

print(intersection_set)  # Output: {2, 4, 5, 7}

del number_1
del number_2
del intersection_set
del start_1, start_2
del step_1, step_2
del stop_1, stop_2
print("=============================================================>\n")


# 4) Remove an item from a set if it exists.
# ===================================> Method 1:-
number_1 = list({1, 2, 3, 4, 5, 6, 7})
number_2 = list({4, 5, 9, 7, 2, 8, 9, 10})

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    value = number_1[i]
    if value in number_2:
        number_2.remove(value)

print(number_2)		# output:- [8, 9, 10]

del number_1
del number_2
del start_1
del step_1
del stop_1

# ===================================> Method 2:-
number_1 = {1, 2, 3, 4, 5, 6, 7}
number_2 = {4, 5, 9, 7, 2, 8, 9, 10}

remove_items = set()
for i in number_1:
    if i in number_2:
        remove_items.add(i)

for item in remove_items:
    number_2.remove(item)

print(number_2)		# output:- {8, 9, 10}

del number_1
del number_2
del remove_items
print("=============================================================>\n")


# 5) Find the difference between two sets.
number_1 = list({1, 2, 3, 4, 5, 6, 7})
number_2 = list({4, 5, 9, 7, 2, 8, 9, 10})

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

remove_set = []

for i in range(start_1, stop_1, step_1):
    value = number_1[i]
    if value in number_2:
        remove_set.append(value)

start_2 = 0
stop_2 = len(remove_set)
step_2 = 1

for i in range(start_2, stop_2, step_2):
    number_2.remove(remove_set[i])

print(number_2)

del number_1
del number_2
del start_1, start_2
del stop_1, stop_2
del step_1, step_2
print("=============================================================>\n")


# 6) Check if two sets are disjoint (i.e., no common elements).
# ===================================> Method 1:-
number_1 = list({1, 2, 3})
number_2 = list({4, 5, 6})

status = False

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if number_1[i] in number_2:
        status = True
        break

print(status) # output:- False

del number_1
del number_2
del start_1
del stop_1
del step_1
del status

# ===================================> Method 2:-
number_1 = [1, 2, 3]
number_2 = [4, 5, 6]

status = False

for i in number_1:
    for j in number_2:
        if i == j:
            status = True
            break
    if status:
        break

print(status) # output:- False

del number_1
del number_2
del status
print("=============================================================>\n")


# 7) Convert a list of numbers into a set and find if there are any duplicates in the list.
number_1 = [0, 1, 2, 3, 4, 1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
number_2 = []

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if number_1[i] not in number_2:
        number_2.append(number_1[i])

set_number_2 = set(number_2)
print(set_number_2)	# output:- {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

del number_1
del number_2
del set_number_2

del start_1
del step_1
del stop_1
print("=============================================================>\n")

# 8) Add a new element to a set and then display the set.
fruits = ["Apple","Banana","Mango","Kiwi","Apple","Mango","Banana"]
rem_fruits = []

start_1 = 0
stop_1 = len(fruits)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if fruits[i] not in rem_fruits:
        rem_fruits.append(fruits[i])
print(rem_fruits)	# output:- ['Apple', 'Banana', 'Mango', 'Kiwi']
print("=============================================================>\n")


# 9) Find the symmetric difference between two sets.
numbers_1 = list({1, 2, 3, 4})
numbers_2 = list({4, 5, 6, 7})
symmetric = set()

start_1 = 0
stop_1 = len(numbers_1)
step_1 = 1

start_2 = 0
stop_2 = len(numbers_2)
step_2 = 1

for i in range(start_1, stop_1, step_1):
    if numbers_1[i] not in numbers_2:
        symmetric.add(numbers_1[i])

for i in range(start_2, stop_2, step_2):
    if numbers_2[i] not in numbers_1:
        symmetric.add(numbers_2[i])

print(symmetric)
