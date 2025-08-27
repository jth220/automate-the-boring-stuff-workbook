# chapter 7 - dictionaries and structuring data

Dictionary

- mutable collection of many values
- it doesnt have indexes for lists
- it has dictioanry indexes called keys, and a key has an associated value
- this is known as the key-value pair
- {} is notated as the dictionary

To access a Dictionary

- Access with square brackets + key
- Use specific keys
- Keys are unique

Lists vs Dictionary

- Lists are ordered ; Dictionaries are unordered
- order matters for list equality, not for dictionary equality

Errors

- accessing non existent key - KeyError
- Safe alternatives dict.get(key, default)

Adding & Updating

- Add new key : spam[”new”] = value
- update existing, just re assign value
- shortcut : setdefault(key, default) → sets key if missing

membership

- ‘key’ in dict → checks key existence
- ‘val’ in dict.values() → checks value existence

iterations

- .keys() → cycles through keys
- .values() → views of values
- .items → tuples of (key, value)
- used in combination with for loops
- remember it returns view objects and not full lists (you’ll have to convert it into a list)

```python
for k, v in spam.items():
    print(k, v)
```

Nesting

- Dictionaries can contain other dictionaries and list
- Useful for modeling structured/real-world data.
- Think of picnic guest lists

methods

- .get(key, default) → safe retriveal
- .setdefault(key, default) → insert if missing
- .pop(key[, default]) removes key and return its value
- .clear() removes all items
- .copy() shallow copy

dictionary basics

- keys can be many immutable types (strings, numbers, tuples) but can’t be mutable types (lists, dicts)
- Dictionaries are mutable, you can add, change or delete key value pairs

real world example

```python
message = 'hello'
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1
print(count)  # {'h':1,'e':1,'l':2,'o':1}

```

This shows dictionaries are great for frequency countrs, tallies , inventories

- you can easily create an empty dictionary, as you loop through the message, you can count the number of letters thanks to the unique key feature.