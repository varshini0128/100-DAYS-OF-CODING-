🧩 Day 2 – Arrays in Data Structures (Python)

Author: Varshini Siliveri
Repo: 100 Days of Coding – DSA
Language: Python
Duration: 30 minutes/day
Goal: Understand arrays, their operations, and basic algorithms.

1️⃣ What is an Array?

Definition:
An Array is a linear data structure that stores a collection of elements of the same data type in contiguous memory locations.
Each element can be accessed directly using its index (starting from 0).

In Python, the closest built-in data structure to an array is a list, though Python also provides a dedicated array module.

Real-World Analogy:
Think of an array as a row of lockers 🧳 — each locker has an address (index) and stores one item.

Syntax (using list):

# Creating an array (list in Python)
arr = [10, 20, 30, 40, 50]

# Accessing elements
print(arr[0])  # Output: 10
print(arr[3])  # Output: 40

2️⃣ Array Characteristics

Fixed Size (in traditional arrays): Once created, size cannot change.
(In Python lists, size can be dynamic.)

Homogeneous Elements: All elements are of the same data type.

Contiguous Memory: Stored one after another in memory.

Index-based Access: You can directly access any element by index.

3️⃣ Array Operations

Let’s perform all major operations on arrays using Python lists.

➕ Insertion (Adding an Element)

Definition:
Adding a new element at a specific position or at the end.

Example:

arr = [10, 20, 30]
arr.append(40)       # Insert at end
arr.insert(1, 15)    # Insert at index 1
print(arr)           # Output: [10, 15, 20, 30, 40]


Time Complexity:

At end → O(1)

At specific index → O(n) (elements shift)

❌ Deletion (Removing an Element)

Definition:
Deleting an element from a specific position or by value.

Example:

arr = [10, 20, 30, 40, 50]
arr.remove(30)    # Remove by value
arr.pop(2)        # Remove by index
print(arr)


Time Complexity:

O(n), because elements after the deleted one shift left.

🔍 Traversal (Accessing Elements One by One)

Definition:
Visiting each element sequentially for operations like printing or searching.

Example:

arr = [10, 20, 30, 40]
for element in arr:
    print(element)


Time Complexity: O(n)

🔎 Searching (Finding an Element)

Linear Search Example:

arr = [10, 20, 30, 40, 50]
x = 30

for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element {x} found at index {i}")
        break


Time Complexity: O(n)

⚙️ Updating (Changing an Element)

Example:

arr = [5, 10, 15, 20]
arr[2] = 99
print(arr)  # Output: [5, 10, 99, 20]


Time Complexity: O(1)

4️⃣ Advantages & Disadvantages of Arrays
Advantages	Disadvantages
Easy to access using index	Fixed size (not in Python lists)
Simple and efficient for storing related data	Insertion/deletion is costly
Memory-efficient storage	Must know size in advance (traditional arrays)
5️⃣ Real-World Applications of Arrays

✅ Used in storing data like marks, salaries, or IDs.
✅ Basis for advanced structures like matrices, stacks, queues, and heaps.
✅ Used in searching, sorting, and dynamic programming problems.

🧮 Practice Problems

Create an array of 5 integers and print all elements using a loop.

Insert an element at the beginning, middle, and end of an array.

Delete a given element from an array.

Search for an element in an array and print its index.

Update a specific element in an array.

Find the sum and average of all array elements.

Find the maximum and minimum elements in an array.

Count even and odd numbers in an array.

Reverse an array without using built-in functions.

Merge two arrays and display the result.

Copy elements of one array into another.

Print all elements greater than a given value.

Print all pairs of elements (nested loop → O(n²)).

Find the second largest number in an array.

Check if an element exists in an array (True/False).

🧾 Summary Table
Operation	                 Description	                Time Complexity
Access                   	Retrieve by index	                    O(1)
Search                  	Find an element	                        O(n)
Insertion	                Add element                            	O(n)
Deletion	                Remove element	                        O(n)
Update	                    Change element                         	O(1)
Traverse                  	Visit each element	                    O(n)