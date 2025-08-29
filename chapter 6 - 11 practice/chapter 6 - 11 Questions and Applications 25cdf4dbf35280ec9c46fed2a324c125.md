# chapter 6 - 11 Questions and Applications

## Practice Questions & Projects — Chapters 6–11

---

## Chapter 6 - Lists

**Practice Questions**

1. What is `[]`?
2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)
3. Assume `spam = ['a', 'b', 'c', 'd']`. What does `spam[int(int('3' * 2) // 11)]` evaluate to?
4. What does `spam[-1]` evaluate to?
5. What does `spam[:2]` evaluate to?
6. Assume `bacon = [3.14, 'cat', 11, 'cat', True]`. What does `bacon.index('cat')` evaluate to?
7. What does `bacon.append(99)` make the list value in `bacon` look like?
8. What does `bacon.remove('cat')` make the list value in `bacon` look like?
9. What are the operators for list concatenation and list replication?
10. What is the difference between the `append()` and `insert()` list methods?
11. What are two ways to remove values from a list?
12. Name a few ways that list values are similar to string values.
13. What is the difference between lists and tuples?
14. How do you write the tuple value that has just the integer value 42 in it?
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
17. What is the difference between `copy.copy()` and `copy.deepcopy()`?

**Practice Programs**

- Comma Code
- Coin Flip Streaks
- Project 1: Interactive Chessboard Simulator

---

## Chapter 7 - Dictionaries and Structuring Data

**Practice Questions**

1. What does the code for an empty dictionary look like?
2. What does a dictionary value with a key `'foo'` and a value `42` look like?
3. What is the main difference between a dictionary and a list?
4. What happens if you try to access `spam['foo']` if `spam = {'bar': 100}`?
5. If a dictionary is stored in `spam`, what is the difference between `'cat' in spam` and `'cat' in spam.keys()`?
6. If a dictionary is stored in `spam`, what is the difference between `'cat' in spam` and `'cat' in spam.values()`?
7. What is a shortcut for the following code?
    
    if 'color' not in spam:
    
    spam['color'] = 'black'
    
8. What module and function can be used to “pretty-print” dictionary values?

**Practice Programs**

- Chess Dictionary Validator
- Fantasy Game Inventory
- List-to-Dictionary Loot Conversion

---

## Chapter 8 - Strings and Text Editing

**Practice Questions**

1. What are escape characters?
2. What do the `\n` and `\t` escape characters represent?
3. How can you put a `\\` backslash character in a string?
4. The string value `"Howl's Moving Castle"` is valid. Why isn’t the single quote a problem here?
5. If you don’t want to put `\n` in your string, how can you write a string with newlines in it?
6. What do the following expressions evaluate to?
    - `'Hello, world!'[1]`
    - `'Hello, world!'[0:5]`
    - `'Hello, world!'[:5]`
    - `'Hello, world!'[3:]`
7. What do the following expressions evaluate to?
    - `'Hello'.upper()`
    - `'Hello'.upper().isupper()`
    - `'Hello'.upper().lower()`
8. What do the following expressions evaluate to?
    - `'Remember, remember, the fifth of November.'.split()`
    - `'-'.join('There can be only one.'.split())`
9. What string methods can you use to right-justify, left-justify, and center a string?
10. How can you trim whitespace characters from the beginning or end of a string?

**Practice Program**

- Table Printer
- Project 2: Add Bullets to Wiki Markup
- Pig Latin Translator

---

## Chapter 9 - Text Pattern Matching with Regular Expressions

**Practice Questions**

1. What is the function that returns Regex objects?
2. Why are raw strings often used when creating Regex objects?
3. What does the `search()` method return?
4. How do you get the actual strings that match the pattern from a Match object?
5. In the regex `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, what does group 0 cover? Group 1? Group 2?
6. How would you specify that you want a regex to match actual parentheses and period characters?
7. The `findall()` method returns a list of strings or a list of tuples. What makes it return one or the other?
8. What does the `|` character signify in regex?
9. What two things does the `?` character signify in regex?
10. What is the difference between the `+` and  characters in regex?
11. What is the difference between `{3}` and `{3,5}` in regex?
12. What do the `\d`, `\w`, and `\s` shorthand character classes signify?
13. What do the `\D`, `\W`, and `\S` shorthand character classes signify?
14. What is the difference between `.*` and `.*?` regexes?
15. What is the character class syntax to match all numbers and lowercase letters?
16. How do you make a regex case-insensitive?
17. What does the `.` character normally match? What if `re.DOTALL` is passed?
18. If `num_re = re.compile(r'\d+')`, what will `num_re.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` return?
19. What does passing `re.VERBOSE` as the second argument to `re.compile()` allow you to do?

**Practice Programs**

- Strong Password Detection
- Regex Version of `strip()`
- Project 3: Extract Contact Information from Large Documents

---

## Chapter 10 - Reading and Writing Files

**Practice Questions**

1. What are file objects?
2. What function is used to open a file? What modes can you pass?
3. What does the `read()` method do?
4. What does the `readlines()` method return?
5. How do you write data to a file?
6. What does `close()` do and why is it important?
7. What does the `with open(...) as f:` syntax do?
8. What’s the difference between absolute and relative file paths?
9. What does `os.getcwd()` return?
10. How can you create directories using Python?

**Practice Projects**

- Project 4: Generate Random Quiz Files

---

## Chapter 11 - Organizing Files

**Practice Questions**

1. What module lets you move and copy files and folders?
2. What function is used to delete a file? A folder?
3. What function can you use to safely delete files by sending them to the recycle bin?
4. What function can you use to rename files?
5. What function walks a directory tree?
6. What does `os.path.join()` do?
7. What does `os.path.abspath()` return?
8. What does `os.path.exists()` check for?
9. What do `os.path.isfile()` and `os.path.isdir()` do?

**Practice Projects**

- Selective Copy
- Deleting Unneeded Files
- Filling in the Gaps
- Project 5: Rename Files with American-Style Dates to European-Style Dates
