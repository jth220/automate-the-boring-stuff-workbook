# chapter 6 - lists

1. What is []?

literal syntax for an empty list

- a list is a mutable sequence type, holds multiple items

1. 

```python
spam[2] = 'hello'
```

1. 

```python
Assume spam = ['a', 'b', 'c', 'd']. What does spam[int(int('3' * 2) // 11)] evaluate to?
int('33' //11) #Recall that '' is a string, this is a string manipulation
33//11
= 
3
spam[3]

```

4.

```python
spam[-1] returns 'd'
```

5.

```python
spam[:2] returns 'a', 'b'
```

6.

```python
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')

#bacon.index('cat') would return 1, returns the first occurence of the found value as an intger
```

7.

```python
bacon = [3.14, 'cat', 11, 'cat', True, 99]
```

8.

```python
bacon = [3.14, 11, 'cat', True, 99]
```

9.

```python
# + for list concantenation, * for list replication
```

10.

```python
.append() #adds values at the end of a list
.insert() # adds values in a specified position
```

11.

```python
.remove()#removes a specified value, removes on the first occurence
.pop()#pops out the latest item from the list and returns the popped item
```

12.

```python
#string and list values are both sequence type, order matters, slicing methods works both the same on both a list and a string
#they both are iterable, membership tests can be performed, length functions and concatenation and reptition methods can be performed.
```

13.

```python
#strings are immutable and changing it requires you to create a new string where as lists are mutable and values can be interchangeable
```

14.

```python
{42,}
```

15.

```python
tuple(list_value) → converts list → tuple

list(tuple_value) → converts tuple → list
```

16.

```python
#variables that contain list values don't contain the actual list but the reference or the pointer to the variable that holds the list, so when you make changes to the list through the secondary variable, it makes changes to the actual list
```

17.

```python
copy.copy() #shallow copy of the list, nested lists will still share changes with the original variable
copy.deepcopy()#deep copies, copies the contents of the list in which the contents of the list is independent, and any changes made are made independently
```

### 1. **Comma Code**

- **Goal:** Write a function that takes a list of strings and returns them as a single string, separated by commas, with `"and"` before the last item.

What module and function can be used to “pretty-print” dictionary values?

- **Example:**
    
    ```python
    def comma_code(items):
        if not items:
            return ''
        elif len(items) == 1:
            return items[0]
        return ', '.join(items[:-1]) + ' and ' + items[-1]
    
    print(comma_code(['apples', 'bananas', 'tofu', 'cats']))
    # apples, bananas, tofu and cats
    
    ```
    

---

### 🔹 2. **Coin Flip Streaks**

- **Goal:** Write a program that flips a coin 100 times and checks whether a streak of 6 heads or tails occurs.
- **Skills tested:** Random numbers, loops, list indexing.
- **Hint:** Keep track of the current streak, reset it if flip changes.

---

### 🔹 3. **Project: Chessboard Simulator** (sometimes “Grid Printer” or “Character Picture Grid”)

- **Goal:** Represent a chessboard (or grid) as a **list of lists** and simulate moves.
- **Skills tested:** Nested lists, indexing, modifying lists.
- **Simpler example:**
    
    ```python
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'X', '.', '.', '.', '.'],
        ['.', '.', '.', '.', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    
    for row in board:
        print(' '.join(row))
    
    ```