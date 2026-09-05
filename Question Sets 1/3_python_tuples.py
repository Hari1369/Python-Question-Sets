#=========================================================================================================#
#=========================================== QUESTIONS ON TUPLES ==========================================#
#=========================================================================================================#

# 1) Create a tuple with 5 elements and print it.
numbers_1 = (1,2,3,4,5,6,7,8,9,10)
print(numbers_1)
del numbers_1
print("=============================================================>\n")

# 2) Access an element by index from a tuple.
numbers_1 = (1,2,3,4,5,6,7,8,9,10)
print(numbers_1[3])
del numbers_1
print("=============================================================>\n")

# 3) Concatenate two tuples into one.
number_1 = (1,2,3,4,5)
number_2 = (6,7,8,9,10,11)
number_3 = (number_1 + number_2)
print(number_3)
del number_1
del number_2
del number_3
print("=============================================================>\n")

# 4) Repeat a tuple multiple times.
set_unique = (1,2,3,4,5)
set_details = (set_unique * 3)
print(set_details)
del set_unique
del set_details
print("=============================================================>\n")

# 5) Convert a tuple into a list.
number_1 = (1,2,3,4,5,6,7,8,9,10)
number_1 = list(number_1)
print(number_1)
del number_1
print("=============================================================>\n")

# 6) Find the length of a tuple.
number_1 = (1,2,3,4,5,6,7)
print(len(number_1))
del number_1
print("=============================================================>\n")

# 7) Count the occurrences of a specific element in a tuple.
number_1 = (1, 2, 3, 4, 5, 5, 6, 5, 6, 5)
index_count = 5
count = 0

start_1 = 0
stop_1 = len(number_1)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    if number_1[i] == index_count:
        count += 1

print(count)
del number_1
del start_1
del stop_1
del step_1
del index_count
del count
print("=============================================================>\n")


# 8) Unpack a tuple into multiple variables.
unpack_tuples = (1,2,3,4)
a,b,c,d = unpack_tuples
print(a)
print(b)
print(c)
print(d)
del unpack_tuples
del a, b, c, d
print("=============================================================>\n")

# 9) Create a tuple with mixed data types and access elements using index.
mix_tuple = (1,2,["Hari","Ashish","Manoj"],"A","B",{4,5,6})
print(mix_tuple)
del mix_tuple
print("=============================================================>\n")

# 10) Sort a tuple (if possible).
sort_tuple = (4, 5, 6, 1, 2, 5, 10)
list_tuple = list(sort_tuple)

start_1 = 0
stop_1 = len(list_tuple)
step_1 = 1

start_2 = 0
stop_2 = len(list_tuple)
step_2 = 1

for i in range(start_1, stop_1, step_1):
    for j in range(start_2, stop_2 - i - 1, step_2):
        if list_tuple[j] > list_tuple[j + 1]:
            list_tuple[j], list_tuple[j + 1] = list_tuple[j + 1], list_tuple[j]

reverse_tuple = tuple(list_tuple)
print(reverse_tuple)

del sort_tuple
del list_tuple
del start_1, start_2
del stop_1, stop_2
del step_1, step_2 
del reverse_tuple
print("=============================================================>\n")
