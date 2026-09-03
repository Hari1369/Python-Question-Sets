# =========================================================================================================#
# ============================================ QUESTIONS SETS =============================================#
# =========================================================================================================#


# 1) Find the largest number Take 5 numbers from the user and find the largest number.
number = []
for i in range(5):
    a = input("Enter 5 number : ")
    number.append(a)

n = len(number)
largest = number[0]
for i in range(n):
    if largest < number[i]:
        largest = number[i]

print("Largest Number :", largest)
print("=============================================================>\n")



# 2) Find the smallest number: Take 5 numbers and find the smallest number.
number = []
for i in range(5):
    a = input("Enter 5 Number : ")
    number.append(a)

n = len(number)
smallest = number[0]
for i in range(n):
    if smallest > number[i]:
        smallest = number[i]

print("Smallest Number :", smallest)
print("=============================================================>\n")



# 3) Count even and odd numbers: Given a list of numbers, count how many are even and how many are odd.
number = []
for i in range(10):
    a = int(input("Enter 10 Numbers : "))
    number.append(a)

n = len(number)
odd_count = 0
even_count = 0
for i in range(n):
    if number[i] % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("EVEN NUMBER : ", even_count)
print("ODD NUMBER : ", odd_count)



# 4) Reverse a number Input: 12345 Output: 54321
number = []
reverse = []
for i in range(5):
    a = int(input("Enter a Number : "))
    number.append(a)

n = len(number)
for i in range(n-1,-1,-1):
    reverse.append(number[i])

print(reverse)


# 5) Check palindrome number - Input: 121 Output: Palindrome
number = []
for i in range(3):
    a = int(input("Enter a pallindrome Number : "))
    number.append(a)

n = len(number)
left = 0
right = len(number) - 1

for i in range(n):
    if number[left] != number[right]:
        print("Not a Pallindrome")
        break
    else:
        print("Pallindrome")
        break


# 6) Find the sum of digits - Input: 1234 Output: 10
number = []
sum_numbers = 0
for i in range(4):
    a = int(input("Enter 4 number: "))
    number.append(a)

n = len(number)
for i in range(n):
    a = number[i]
    sum_numbers = sum_numbers + a

if sum_numbers != 10:
    print("No Digits are equal to sum!")
else:
    print("SUM Of NUMBERS : ", sum_numbers)



# 7) Find factorial - Input: 5 Output: 120
factorial = 1
a = int(input("Enter Number: "))

for i in range(1, a + 1):
    factorial = factorial * i

print("Factorial : ", factorial)


# 8) Print Fibonacci series - Input: 7 Output: 0 1 1 2 3 5 8 Find duplicate elements in a list
number = int(input("Enter Number : "))
first = 0
second = 1
fibonacci = []
for i in range(number):
    fibonacci.append(first)

    third = first + second
    first = second
    second = third

print(fibonacci)



# 9) Find duplicate elements in a list - Input: [1, 2, 3, 2, 4, 1] - Output: 1, 2
number = [1, 2, 3, 2, 4, 1]
n = len(number)
for i in range(n):
    for j in range(i+1, n):
        if number[i] == number[j]:
            print(number[i])


# 10) Find the second largest number - Input: [10, 5, 8, 20, 15] - Output: 15
number = [10, 5, 8, 20, 15]
n = len(number)
largest = number[0]
second_largest = number[1]

if second_largest > largest:
    largest = number[1]
    second_largest = number[0]

for i in range(2, n):

    if number[i] > largest:
        second_largest = largest
        largest = number[i]

    elif number[i] > second_largest and number[i] < largest:
        second_largest = number[i]

print("Second Largest Number:", second_largest)