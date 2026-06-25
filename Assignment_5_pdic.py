# -------------------------------
# Question 1
# Repeat a tuple three times
# -------------------------------

t = (1, 2, 3)

result = t * 3

print("Question 1")
print(result)

print()

# -------------------------------
# Question 2
# Join three tuples
# -------------------------------

t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

new_tuple = t1 + t2 + t3

print("Question 2")
print(new_tuple)

print()

# -------------------------------
# Question 3
# Check if an element exists
# -------------------------------

numbers = (10, 20, 30, 40)

if 30 in numbers:
    print("Question 3")
    print("30 is present")
else:
    print("30 is not present")

print()

# -------------------------------
# Question 4
# Find total, highest and lowest
# without sum(), max(), min()
# -------------------------------

nums = (12, 45, 7, 89, 23)

total = 0
highest = nums[0]
lowest = nums[0]

for num in nums:

    total = total + num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Question 4")
print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

print()

# -------------------------------
# Question 5
# Filter tuple values > 10
# -------------------------------

n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for num in n:

    if num > 10:

        filtered = filtered + (num,)

print("Question 5")
print(filtered)

print()

# -------------------------------
# Question 6
# Count elements in a set
# without len()
# -------------------------------

s = {"cat", "dog", "bird", "fish"}

count = 0

for item in s:

    count = count + 1

print("Question 6")
print("Number of elements =", count)

print()

# -------------------------------
# Question 7
# Combine two sets
# -------------------------------

set1 = {1, 2, 3}

set2 = {3, 4, 5}

combined = set1.union(set2)

print("Question 7")
print(combined)

print()

# -------------------------------
# Question 8
# Find common elements
# -------------------------------

s1 = {1, 2, 3, 4}

s2 = {3, 4, 5, 6}

common = s1.intersection(s2)

print("Question 8")
print(common)