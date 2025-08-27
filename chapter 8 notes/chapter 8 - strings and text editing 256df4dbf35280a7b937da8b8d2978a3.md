# chapter 8 - strings and text editing

String literals

- refers to strings that appear in our code

Double Quotes

- using “” for strings, meaning a single quote can exist without being considered an end or a beginning of a strong

Escape Characters

- Allows you to use both single and double quotes
- \ allows you to escape a character, which you follow it with a character you want to add to a string

| \' | Single quote |
| --- | --- |
| \" | Double quote |
| \t | Tab |
| \n | Newline (line break) |
| \\ | Backslash |

Raw Strings

- Place an r before the quotation mark to make it a raw string
- enter string values with backslashes, which helps ignore all escape characters

```python
>>> print(r'The file is in C:\Users\Alice\Desktop')
The file is in C:\Users\Alice\Desktop
```

multiline strings

- using ‘’’ ‘’’ you can insert a new line into a string rather than using \n

multiline comments

- you can use “”” “”” to make multiline comments
- unused string literals, python ignores as they aren’t assigned

Indexes and Slices

- You can slice and index the same way you can do to a list
- s[0] first character
- s[-1] last character
- s[start:end]
- note that it excludes end but includes start

Membership

```python
"cat" in "concatenate"   # True

```

F-Strings - this is added after version 3.6

- you can put strings inside other strings
- a simple approach is using {} inside f strings

Alternative ways

- “My name is %s” % name
- str.format() : “My name is {}”.format(name) notice its the string first and then the variables following after in the parameters

String methods

- case conversion : `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase() isupper()`, `islower()`
- Tests :
- `isalpha()` → only letters
- `isalnum()` → letters + digits
- `isdecimal()` → only digits
- `isspace()` → only whitespace
- `istitle()` → title case
- Search : starswith(x), endswith(y)
- JOining and Splitting :
- join() - used when you have a list of strings that needs to be joined into a single string value, call it on a string and pass it on a list of strings

```python
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

```

- split() similar to how we attach it to a string in which we want to put between the list of strings
- instead we can specify what we want to remove  in the parameters

they are inverses of each other

- another thing to note that split with no arguments removes white space, new lines by default2

- **Trimming**:
    - `strip()`, `lstrip()`, `rstrip()` (strips whitespace, left and right if specified) trims from ends not in the middle
    - `strip("xyz")` → removes listed chars
- **Alignment**:
    - `rjust(width, fill)`, `ljust(width, fill)`, `center(width, fill)` - pads white space
- **Replace**:
    - `replace(old, new)` - reaplces substrings inside

- `pyperclip.copy("text")` → copies text to clipboard
- `pyperclip.paste()` → pastes text from clipboard

String Immutability

- Important to note that strings don’t change in place, any changes made returns a new string
- methods return new strings, they don’t modify in place

Strings can also be chained using multiple methods

**Unicode and Encoding Basics**

-