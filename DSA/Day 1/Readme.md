# 📘 **Day 1 – Introduction to Data Structures and Algorithms**

> Author: Varshini Siliveri
> Repo: 100 Days of Coding – DSA
> Duration: 30 mins/day (Python)
> Day 1 Topic: Core Foundations

---

## 🧩 1. What is a Data Structure?

A Data Structure is a specific way to store and organize data in a computer so that it can be used efficiently. It defines how data is arranged, accessed, and manipulated.

**Types:**

* Linear: Array, Stack, Queue, Linked List
* Non-linear: Tree, Graph
* Hash-based: Hash Table, Dictionary

**Python Example:**

```python
students = ["Varshini", "Aarav", "Diya"]
print("First student:", students[0])
```

---

## ⚙️ 2. What is an Algorithm?

An Algorithm is a finite, step-by-step procedure that defines a set of operations to solve a particular problem or perform a specific computation.

**Example:**

```python
# Algorithm to find the sum of two numbers
a = 10
b = 20
sum = a + b
print("Sum =", sum)
```

---

## ⏱️ **3. Time and Space Complexity**

* **Time Complexity**: Measures how the execution time of an algorithm grows with input size.
* **Space Complexity**: Measures how much memory an algorithm uses.

**Example:**

```python
# O(n)
for i in range(5):
    print(i)
```

---

## 📈 **4. Big O Notation**

**Big O Notation** expresses how efficiently an algorithm performs as the input grows.

| Notation | Type        | Description                                    | Example             |
| -------- | ----------- | ---------------------------------------------- | ------------------- |
| O(1)     | Constant    | Executes in same time regardless of input size | Access list item    |
| O(log n) | Logarithmic | Grows slowly as input grows                    | Binary Search       |
| O(n)     | Linear      | Grows proportionally to input                  | Loop through list   |
| O(n²)    | Quadratic   | Nested loops, grows fast                       | Comparing all pairs |

**Python Example:**

```python
# O(1)
nums = [10, 20, 30]
print(nums[0])

# O(n²)
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i], numbers[j])
```
## 🔍 Understanding **O(n²) – Quadratic Time Complexity**

**Definition:**
O(n²) (pronounced *“big O of n squared”*) means the runtime grows **proportionally to the square of the input size**.

In simple terms — for every element, you perform another full loop over the same data.

**Example:**
If you have 5 elements, total operations = 5 × 5 = 25 steps.
If 100 elements → 100 × 100 = 10,000 steps.

So it grows **very fast** — that’s why O(n²) algorithms are slow for large data.

**Python Example:**

```python
# Example of O(n²)
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i], numbers[j])
```

Here:

* Outer loop runs `n` times.
* Inner loop runs `n` times for each outer loop iteration.
  → Total = n × n = **O(n²)**.

**Real-life analogy:**
Imagine checking every student’s name with every other student to find duplicates.
For 10 students, you’ll do 100 comparisons — that’s quadratic growth.

✅ **Practice Idea:**
Write a program that prints all possible pairs from a list — that’s also O(n²).

---

## 🧠 **5. Steps in Algorithmic Problem Solving**

1. Understand the problem
2. Plan your approach
3. Design the logic (algorithm)
4. Implement in code
5. Test and optimize

**Example:**

```python
numbers = [3, 7, 1, 9, 5]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
```

---

## 🧮 **Practice Problems**

### 🧩 Basic (from lesson)

1. Create a list of 5 student names and print the 3rd one.
2. Write code to calculate the product of two numbers.
3. Write a loop that prints numbers 1–10 and count iterations.
4. Write Python code for **O(1)** and **O(n²)** examples.
5. Find the smallest number in a list.

---

### ⚡ Extra 10 Practice Questions

6. Write an algorithm to reverse a list without using built-in functions.
7. Count the number of even and odd numbers in a list.
8. Find the sum of all elements in a list.
9. Write a program to check if a number is prime.
10. Write an algorithm to find the maximum of three numbers.
11. Display all pairs of elements from a list (O(n²) approach).
12. Write a program that prints the factorial of a given number.
13. Implement a function to check if a string is a palindrome.
14. Create a list of integers and print only the unique elements.
15. Write a program that calculates the average of numbers in a list.

---

## 🧾 **Summary Table**

| Concept              | Definition                         | Key Takeaway                  |
| -------------------- | ---------------------------------- | ----------------------------- |
| **Data Structure**   | Organized way to store/manage data | Core of efficient programs    |
| **Algorithm**        | Set of steps to solve a problem    | Logical blueprint for coding  |
| **Time Complexity**  | Measures speed                     | Helps optimize performance    |
| **Space Complexity** | Measures memory                    | Keeps programs efficient      |
| **Big O Notation**   | Mathematical efficiency scale      | Compare algorithm performance |

---
