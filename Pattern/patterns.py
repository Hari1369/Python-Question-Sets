# 1) Right-Angle Star Triangle Print a right-angle triangle of stars with n rows. Row i prints i stars.
# *
# **
# ***
# ****
# *****
# ================> SOLUTION 1 ================
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
del n
print("==============================")

# 2) Inverted Star Triangle Print an inverted right-angle triangle. Row 1 has n stars, decreasing by 1 each row.
# *****
# ****
# ***
# **
# *
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
del n
print("==============================")


# 3) Number Staircase Each row i prints numbers 1 through i.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(j + 1, end="")
    print()
del n
print("==============================")


# 4) Same-Number Rows Row i prints the number i repeated i times.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
    print()
del n
print("==============================")


# 5) Pyramid of Stars Print a centred pyramid. Row i has (2i - 1) stars with leading spaces.
#     *
#    ***
#   *****
#  *******
# *********
n = 5
for i in range(1, n+1):
    for s in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")
    print()
del n
print("==============================")



# 6) Diamond Pattern Print a full diamond (pyramid + inverted pyramid).
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
n = 5
for i in range(1, n+1):
    for s in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower Pyramid
for i in range(n - 1, 0, -1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
del n
print("==============================")


# 7) Hollow Rectangle Print a rectangle border of stars with spaces inside.
# *****
# *   *
# *   *
# *   *
# *****
rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 8) Pascal's Triangle Each element is the sum of the two elements above it.
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

n = 5
row = [1]

for i in range(n):
    for num in row:
        print(num, end=" ")
    print()

    new_row = [1]

    for j in range(len(row)-1):
        new_row.append(row[j] + row[j+1])
    
    new_row.append(1)
    row = new_row



# 9) Hollow Pyramid A centred pyramid where only the border stars are printed.
#     *
#    * *
#   *   *
#  *     *
# *********

n = 5

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()



# 10) Butterfly Pattern Two mirrored triangles forming wings
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for s in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")

    print()


for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    for s in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()


