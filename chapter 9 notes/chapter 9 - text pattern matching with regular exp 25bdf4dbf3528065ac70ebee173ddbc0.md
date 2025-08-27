# chapter 9 - text pattern matching with regular expressions

Why Regex Matters

- searches for a pattern even if you don’t know the exact string
- regex allows the program to recognise a string the same level a human does (such as recognising a phone number)

regexes

- \d = stands for decimal number between 0-9
- Example: `\d{3}-\d{3}-\d{4}` matches phone number.
- use r’’ to avoid backslash escapes
- {n} where n is any number, in curly brackets is the equivalent of “match the pattern n times”

using regex in python

- import re
- pattern = re.compile(r’…’) → pattern object
- match = pattern.search(text) → match object (or None)
- match.group() → matched string
- .findall() all matches → list of strings or tuples
- .sub(replacement, text) → substitutes

groups and capturing

- use parentheses () to group parts of regex.

Example: `(\d{3})-(\d{3}-\d{4})`

- `.group(1)` → area code
- `.group(2)` → rest of number
- `.groups()` → tuple of all groups

escaping special characters

- Special chars: `$ () * + - . ? [\] ^ {|}`
- Escape with `\` if literal.
    - Example: `\.` matches a literal dot.
- Example with parens:
    
    ```python
    re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    
    ```
    

Alternation using |

- `r'Cat|Dog'` matches either.
- Group alternation: `r'Cat(astrophe|egory|ch)'`.
- Escape literal pipe: `\|`.

```python
import re
>>> pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
>>> match = pattern.search('Catch me if you can.')
>>> match.group()
'Catch'
>>> match.group(1)
'ch'
```

Search vs Findall

- .search() → first match (Match Object).
- .findall() → all matches
- regex without groups leaves → list of strings
- regex with groups → list of tuples

```python
>>> import re
>>> pattern = re.compile(r'\d{3}')
>>> pattern.findall('1234')
['123']
>>> pattern.findall('12345')
['123']
>>> pattern.findall('123456')
['123', '456']
```

Character Classes

- `[abc]` → match any one char.
- `[a-zA-Z0-9]` → ranges.
- `[^abc]` → negate (not a, b, or c).
- Inside brackets, most symbols lose special meaning.

```python
>>> import re
>>> vowel_pattern = re.compile(r'[aeiouAEIOU]')
>>> vowel_pattern.findall('RoboCop eats BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']
```

Shorthand Classes

- `\d` → digit
- `\D` → not digit
- `\w` → word char (letters, digits, underscore)
- `\W` → not word char
- `\s` → whitespace (space, tab, newline)
- `\S` → not whitespace

```python
>>> import re
>>> pattern = re.compile(r'\d+\s\w+')
>>> pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '
6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

- this example follows more than 1+ digit, followed by a white space followed by multiple characters

## Quantifiers

- `?` → 0 or 1 (optional)
- → 0 or more
- `+` → 1 or more
- `{n}` → exactly n
- `{n,}` → n or more
- `{,m}` → up to m
- `{n,m}` → between n and m

```python
import re

# Optional ? → 'u' is optional
print(re.findall(r'colou?r', "color colour colouur"))
# ['color', 'colour']

# Zero or more * → 'o' can appear 0 or more times
print(re.findall(r'go*gle', "ggle gogle google gooooogle gle"))
# ['ggle', 'gogle', 'google', 'gooooogle']

# One or more + → 'o' must appear at least once
print(re.findall(r'go+gle', "ggle gogle google gooooogle"))
# ['gogle', 'google', 'gooooogle']

# Exactly {n} → 'ha' repeated exactly 3 times
print(re.findall(r'(ha){3}', "ha haha hahaha hahahaha"))
# ['ha'] (from 'hahaha'), ['ha'] (from 'hahahaha') → matches "hahaha" only

# Range {m,n} → 'ha' repeated 2 to 4 times
print(re.findall(r'(ha){2,4}', "ha haha hahaha hahahaha hahahahaha"))
# ['ha'] (matches 'haha')
# ['ha'] (matches 'hahaha')
# ['ha'] (matches 'hahahaha')
```

quantifiers come after the element they control

## Greedy vs Lazy

- Greedy (default) → match longest possible.
- Lazy → add `?` after quantifier.
    - `.*` → greedy
    - `.*?` → lazy

```python
import re

text = "<tag>content</tag><tag>more</tag>"

# Greedy * → grabs as much as possible
print(re.findall(r'<tag>.*</tag>', text))
# ['<tag>content</tag><tag>more</tag>']

# Lazy *? → grabs as little as possible
print(re.findall(r'<tag>.*?</tag>', text))
# ['<tag>content</tag>', '<tag>more</tag>']
```

## Anchors & Boundaries

- `^` → start of string
- `$` → end of string
- `^...$` → entire string
- `\b` → word boundary
- `\B` → not word boundary

Mnemonic: “^carrots $cost dollars” (caret at start, dollar at end).

- anchors match positions in a string

```python
import re

# Must start with HTTP
print(bool(re.match(r'^HTTP', "HTTP/1.1 200 OK")))   # ✅ True
print(bool(re.match(r'^HTTP', "XHTTP/1.1")))         # ❌ False
```

```python
# Must end with ".jpg"
print(bool(re.search(r'\.jpg$', "photo.jpg")))   # ✅ True
print(bool(re.search(r'\.jpg$', "photo.jpeg")))  # ❌ False
```

```python
# Validate a 5-digit US ZIP code
print(bool(re.fullmatch(r'\d{5}', "12345")))   # ✅ True
print(bool(re.fullmatch(r'\d{5}', "123456")))  # ❌ False
print(bool(re.fullmatch(r'\d{5}', "12 345")))  # ❌ False
```

```python
text = "The cat scattered the catalog."

print(re.findall(r'\bcat\b', text))
# ['cat'] ← only the standalone word

print(re.findall(r'cat', text))
# ['cat', 'cat', 'cat'] ← also matches inside "scattered" and "catalog"
```

avoid partial matches inside bigger words

think of boundaries that seperates characters to non characters, the placement is used to identify if the word itself is standalone

\B is the opposite, python matches words where there are characters are before or after the word you’re looking for

- **`^`** → Match only at the **start** (validation, prefixes).
- **`$`** → Match only at the **end** (extensions, suffixes).
- **`^...$`** → Whole string must fit the pattern.
- **`\b`** → Match words as standalone units.
- **`\B`** → Match words **inside** bigger words (not at edges).

## Dot Character

- `.` → any char except newline.
- With `re.DOTALL`, `.` matches everything (including newline).

```python
>>> import re
>>> at_re = re.compile(r'.at')
>>> at_re.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']

```

thinks of the . as the place holder for any character, and then the characters or whatever following after

## Options

- `re.IGNORECASE` / `re.I` → case-insensitive.
- `re.DOTALL` → dot matches newline. (changes the meaning of . so that it includes \n)

```python
pattern = re.compile(r'cat.*dog', re.DOTALL)
text = "cat\nis with dog"

print(pattern.search(text).group())
# cat
# is with dog
```

- `re.VERBOSE` → allow whitespace & comments in regex string.

Combine with `|` (bitwise OR). Example:

```python
pattern = re.compile('foo', re.I | re.DOTALL | re.VERBOSE)

```

With Verbose

```python
pattern = re.compile(r"""
    \d{3}     # area code
    -         # dash
    \d{3}     # prefix
    -         # dash
    \d{4}     # line number
""", re.VERBOSE)

print(bool(pattern.fullmatch("415-555-4242")))
# True
```

## Without verbose

```python
re.compile(r"\d{3}-\d{3}-\d{4}")
```

**Substitution**

- `.sub(replacement, text)` replaces matches.
- Use backreferences (`\1`, `\2`, …) for captured groups in replacement.
- Example:
    
    ```python
    re.compile(r'Agent (\w)\w*').sub(r'\1****', 'Agent Alice met Agent Bob')
    # "A**** met B****"
    
    ```