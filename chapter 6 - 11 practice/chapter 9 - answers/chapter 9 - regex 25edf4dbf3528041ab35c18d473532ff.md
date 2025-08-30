# chapter 9 - regex

1.

```python
pattern = re.compile(#Here you can construct the patterns of the string you want to find)
#now pattern is a Regex objects, this can be used in unison with search functions
match = pattern.search(text) → match object (or None) 

```

2.

```python
#raw strings are often used because regex uses \, so its used to avoid escaping characters
```

3.

```python
search() #returns match objects after it finds any matches with the pattern object, returns the first occurrence
```

4.

```python
#So using the pattern object, if there is a match, it returns a match object, you can simply just print the match object using
#match.group()
```

5.

```python
r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
#group 0 - the entire string
#group 1 - the first paranthesis set
#group 2 - the second paranthesis set

```

6.

```python
#Escape each literal metachar: r'\(', r'\)', and for a period r'\.'
```

7.

```python
#Returns a list of strings if the pattern has no capturing groups, returns a tuple if it has groups
```

8.

```python
# | alternation operator, will match either side of | (the pipe)
```

9.

```python
#Optional quantifier, 0 or 1
```

10.

```python
# + says that it has to atleast appear once or more
# * says that it can appear either 0 or more
```

11.

```python
{3} #matches in groups of 3
{3, 5}# matches in groups of 3 to 5
```

12.

```python
#digit
#word
#white spaces
```

13.

```python
#not digit
#not word
#no whitespaces
```

14.

```python
#.* is greedy (much as possible)
#.*? is lazy (as little as possible)
```

15.

```python
[a-z0-9]
```

16.

```python
pattern = re.compile(r'cat.*dog', re.IGNORECASE)
```

17.

```python
.#normally matches with any new character except newline
#DOTALL allows . to match with \n (including new lines)
```

18.

```python
#Will return a string as
#X drummers, X pipers, five rings, X hens
```

19.

```python
#Verbose allows you to add comments in the pattern, you can add # and multiline strings
#allows you to spread pattern over multiople lines, ignores unescaped white spaces and add comments
```

### **Strong Password Detection**

- **Goal:** Write a program that checks if a string is a “strong” password.
- **Typical criteria (you decide the exact rules):**
    - At least a certain length (e.g. 8+ characters).
    - Contains uppercase and lowercase letters.
    - Has at least one digit.
    - Maybe includes at least one special character.
- **Regex angle:** You’ll be combining multiple patterns or using lookaheads to enforce the different rules.

---

### **2. Regex Version of `strip()`**

- **Goal:** Re-create Python’s `strip()` method (removes whitespace by default, or given chars from start/end of string).
- **Challenge:** Do it using regex substitution (`re.sub`).
- **Steps to think about:**
    - Handle leading and trailing spaces/characters separately.
    - Make it flexible so you can optionally pass in a custom set of chars to strip.

---

### **3. Extract Contact Information from Large Documents**

- **Goal:** Scan a big text blob and pull out:
    - Phone numbers.
    - Email addresses.
- **Regex angle:**
    - Write one regex for phone numbers (different formats: dashes, spaces, parentheses).
    - Write one regex for emails (usernames, domains, dots).
- **Output:** Likely a list of all found contacts.