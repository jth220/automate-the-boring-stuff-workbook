# chapter 8 - strings and text editing

1.

```python
#Escape characters are used to allow characters that wouldn't usually be allowed in a stirng literal
#Examples such as ' in a string, which would have to be rewritten as \'
```

2.

```python
\n #New Line
\t #Tab
```

3.

```python
\\ #Used to put a back slash in a string

```

4.

```python
"Howl's Moving Castle" #Is a literal string, this is because it is enclosed in double quotes
```

5.

```python
""" """ #Used for multiline strings
```

6.

```python
'e'
'Hello'
'Hello'
'world!'
```

7.

```python
'HELLO'
True
'hello'
```

8.

```python
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
'There-can-only-be-one-.''
```

1. 

```python
ljust()
rjust()
center()
```

10.

```python
rstrip()
lstrip()
strip()
```

# 1) Table Printer

### Goal

Write `printTable(tableData: list[list[str]]) -> None` that neatly prints a table with each column right-justified.

### Requirements

- Each inner list is a column, **not** a row.
- All inner lists are the same length.
- Find the longest string in each column, use that width for right justification.
- Print row by row, with spaces between columns.

### Example

```python
tableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]
printTable(tableData)

#Hashing out the logic here, if I was to manually print the table by column x row
# tableData[0][0], tableData[1][0], tableData[2][0] up to length of outerLists
# Increment Outerlist (column) first, than inner row (row) So
```

**Expected output** (columns aligned):

```
 apples  Alice   dogs
oranges    Bob   cats
cherries  Carol  moose
 banana  David  goose

```

---

# 2) Add Bullets to Wiki Markup

### Goal

Write a script that:

- Gets multi-line text from the clipboard.
- Adds  at the start of each line.
- Copies the new text back to the clipboard.

### Requirements

- Use `pyperclip` for clipboard access.
- Input:
    
    ```
    Lists of animals
    Lists of aquarium life
    Lists of biologists by author abbreviation
    Lists of cultivars
    
    ```
    
- Output after script runs:
    
    ```
    * Lists of animals
    * Lists of aquarium life
    * Lists of biologists by author abbreviation
    * Lists of cultivars
    
    ```
    

### Bonus

- Allow different bullet symbols (, `+`, etc.) passed as a variable/argument.
- Don’t add extra trailing  if the line is blank.

---

# 3) Pig Latin Translator

### Goal

Write a translator that converts English text into **Pig Latin**.

### Rules

- If a word starts with a consonant, move consonant cluster to the end and add `"ay"`.
    - `hello → ellohay`, `python → ythonpay`
- If a word starts with a vowel, just add `"yay"` at the end.
    - `apple → appleyay`, `orange → orangeyay`
- Preserve capitalization:
    - `Hello → Ellohay`, `APPLE → APPLEYAY`
- Preserve non-letter characters (spaces, punctuation).

### Input/Output Example

Input:

```
Hello there, my name is Ada.

```

Output:

```
Ellohay erethay, ymay amenay isyay Aday.

```