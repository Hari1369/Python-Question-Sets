#=========================================================================================================#
#=========================================== QUESTIONS ON DICTIONARIES =====================================#
#=========================================================================================================#

# 1) Create a dictionary with keys as strings and values as integers. Add some key-value pairs.
developer = {
    'name':'hari',
    'age':23,
    'gender':'male'
}
print(developer)
del developer
print("=============================================================>\n")

# 2) Access a value from the dictionary using its key.
# ===================================> Method 1:-
developer = {
    'name': 'hari',
    'age': 23,
    'gender': 'male'
}
keys_list = list(developer.keys())
start_1 = 0
stop_1 = len(keys_list)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    key = keys_list[i]
    print(developer[key])

del developer
del keys_list
del start_1
del stop_1
del step_1
# ===================================> Method 2:-
developer = {
    'name': 'hari',
    'age': 23,
    'gender': 'male'
}
for i in developer.values():
	print(i)

del developer
print("=============================================================>\n")

# 3) Check if a key exists in a dictionary.
# ===================================> Method 1:-
developer = {
    'name': 'hari',
    'age': 23,
    'gender': 'male'
}
keys_list = list(developer.keys())
status = False
dict_name = 'name'

start_1 = 0
stop_1 = len(keys_list)
step_1 = 1

for i in range(start_1, stop_1, step_1):
	if dict_name == keys_list[i]:
		status = True
print(status)

del developer
del keys_list
del dict_name
del start_1
del stop_1
del step_1
del status

# ===================================> Method 2:-
developer = {
    'name': 'hari',
    'age': 23,
    'gender': 'male'
}
status = False
dict_name = 'name'
for i in developer.keys():
	if i == dict_name:
		status = True
print(status)

del developer
del status
del dict_name
print("=============================================================>\n")

# 4) Iterate over all keys in a dictionary.
# ===================================> Method 1:-
developer = {
    'name': 'hari',
    'age': 23,
    'gender': 'male'
}
keys_list = list(developer.keys())

start_1 = 0
stop_1 = len(keys_list)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    print(keys_list[i])


# ===================================> Method 2:-
developer = {
    'name': 'hari',
    'age': 23,
    'gender': 'male'
}
for i in developer.keys():
	print(i)
del developer
print("=============================================================>\n")

# 5) Merge two dictionaries into one.
Dict_1 = {
	'name':'Hari',
	'age':23,
	'gender':'male'
}
Dict_2 = {
	'name':'Ashish',
	'age':23,
	'gender':'male'
}
merged_dictionary = {}
for i in Dict_1:
	merged_dictionary[i] = Dict_1[i]
for j in Dict_2:
	merged_dictionary[j] = Dict_2[j]

print(merged_dictionary)
print("=============================================================>\n")

# 7) Remove a key-value pair from a dictionary.
developer = {
'name':'Hari',
'age':23,
'gender':'male'
}

developer.pop('name')
print(developer)
del developer
print("=============================================================>\n")

# 8) Update a value in a dictionary.
developer = {
'name':'Hari',
'age':23,
'gender':'male'
}
developer.update({'age': 40})
print(developer)
del developer
print("=============================================================>\n")

# 9) Sort a dictionary by keys and print it.
scores = {'Hari': 80, 'Ashish': 90, 'Manoj': 70}
items = list(scores.items())

start_1 = 0
stop_1 = len(items)
step_1 = 1

for i in range(start_1, stop_1, step_1):
    for j in range(0, stop_1 - i - 1):
        if items[j][0] > items[j + 1][0]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_scores = dict(items)
print(sorted_scores)
del scores
del items
del sorted_scores

del start_1
del step_1
del stop_1
print("=============================================================>\n")


# 10) Find the key with the maximum value in the dictionary.
scores_1 = {'Hari': 80, 'Ashish': 90, 'Manoj': 70}
items = list(scores_1.items())
n = len(items)

start = 0
stop = n
step = 1

max_key = items[0][0]
max_value = items[0][1]
for i in range(start, stop, step):
	key = items[i][0]
	value = items[i][1]

	if value > max_value:
		max_value = value
		max_key = key
print(max_key)

del scores_1
del items

del n

del start
del stop
del step

del max_key
del max_value
print("=============================================================>\n")

