# chapter 1 - 5 Practice Questions and Applications

Learning Objectives : 

## Learning Objectives (linked to Ch.1–5)

### **Chapter 1 – Python Basics**

- **Practice Qs:**
    - Age categorizer → apply `if/elif/else`
    - Even numbers → use operators (`%`) and list iteration
- **Applications:**
    - Calculator → reinforces operators, user input, and variables
- **Objective:** Build comfort with Python’s fundamental building blocks (variables, types, operators).

---

### **Chapter 2 – Flow Control**

- **Practice Qs:**
    - Fibonacci numbers → `for` loops, iteration
    - Password input loop → `while` loops, breaking conditions
    - Number guessing game → combines loop control + conditionals
- **Applications:**
    - Password strength checker → uses branching (`if` checks for rules)
- **Objective:** Learn how decisions and repetition control program flow.

---

### **Chapter 3 – Functions**

- **Practice Qs:**
    - is_prime() → writing functions with return values
    - box_print with `fill` → multiple parameters, string manipulation
- **Applications:**
    - To-do list app → modular functions for `add`, `remove`, `show`
- **Objective:** Encapsulate code in reusable blocks, use parameters and return values effectively.

---

### **Chapter 4 – Handling Errors with try/except**

- **Practice Qs:**
    - safe_divide() → raise exception if divide by zero
    - average() with exception → force handling empty lists
- **Applications:**
    - Calculator with error handling → wrap math ops in try/except
- **Objective:** Anticipate and handle runtime problems gracefully.

---

### **Chapter 5 – Debugging, Assertions, Logging**

- **Practice Qs:**
    - assert sorted list → sanity check for programmer errors
    - dice roll with logging → track program execution
- **Applications:**
    - Log analyzer → real use case of logging + string parsing
    - Guessing game with logging → shows how logs reveal program state
- **Objective:** Debug actively with tools (asserts, logs), not just guesswork.

---

## 🧩 Big Picture

Each set of practice questions/applications:

- **Ch. 1–2 → Syntax & Control Flow** (write correct programs).
- **Ch. 3 → Functions** (organize and reuse code).
- **Ch. 4 → Exceptions** (handle wrong input safely).
- **Ch. 5 → Debugging tools** (find & fix problems faster).

## Practice Questions (Ch. 1–5)

### Basics & Flow Control

1. Write a program that asks the user for their age. If they are under 18, print “You are a minor.” If 18–65, print “You are an adult.” If 65+, print “You are a senior.”
2. Write a loop that prints the first 10 Fibonacci numbers.
3. Given a list of integers, write code that prints only the even numbers.
4. Ask the user to input a password. Keep prompting until they type `"open_sesame"`.
5. Write a program that calculates the factorial of a number using both a `for` loop and a recursive function.

### Functions

1. Create a function `is_prime(n)` that returns True if `n` is prime.
2. Write a function `box_print(symbol, width, height)` (like the book’s example) but add a parameter `fill` that can be `"empty"` or `"solid"`.
3. Create a function `safe_divide(a, b)` that returns `a / b`, but raises an exception with a helpful message if `b == 0`.

### Debugging / Assertions / Exceptions

1. Write a function `average(numbers)` that raises an exception if the list is empty.
2. Insert an `assert` in a function that sorts a list to confirm the first element is <= the last.
3. Add `logging.debug()` calls to a loop that simulates rolling a dice 10 times.

---

## 💻 Small Applications

These are more "real-world" exercises where you apply chapters 1–5.

### 1. **Password Strength Checker**

- Input: string password.
- Rules: must be at least 8 chars, contain a digit, and a capital letter.
- Use exceptions to raise errors when rules aren’t met.

---

### 2. **Simple Calculator with Error Handling**

- Ask the user for two numbers and an operator (`+ - * /`).
- Use a function to perform the calculation.
- Handle division by zero with `try/except`.

---

### 3. **Number Guessing Game**

- Generate a random number between 1–100.
- Let the user guess until correct.
- After each guess, tell them “Too high!” or “Too low!”
- Add logging to track how many guesses were taken.

---

### 4. **Basic To-Do List (Console App)**

- Use a list to store tasks.
- Commands: `add`, `remove`, `show`, `quit`.
- Add assertions to confirm the list behaves correctly (e.g., removing a task that doesn’t exist should raise an exception).

---

### 5. **Log Analyzer**

- Write a function that simulates processing log lines (strings).
- Example log line: `"2025-08-21 12:00:00 - ERROR - Disk full"`
- Count how many ERRORs, WARNINGs, and INFOs appear.
- Use logging to output progress while parsing.
