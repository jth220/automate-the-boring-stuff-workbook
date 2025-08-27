# chapter 6 - lists

List 

- contains multiple values in ordered sequence
- notated by []
- lists can hold mixed types

Indexes

- starts at 0
- negative indexes count backwards

Slices

- can extract sublists with start:stop

```python
spam[1:3] → ['bat', 'rat']
spam[:2] → ['cat', 'bat']
spam[2:] → ['rat', 'elephant']
spam[:] → full copy
```

**len()** 

- returns number of items

**updating values**

- assign new values by index

```python
spam[1] = 'aardvark'
spam[-1] = 12345
```

**concatenation & replication**

- + joins lists * repeats

```python
[1, 2] + [3, 4] → [1, 2, 3, 4]
['X', 'Y'] * 3 → ['X', 'Y', 'X', 'Y', 'X', 'Y']
```

**del statement**

- delete by index

```python
spam = ['cat','bat','rat']
del spam[1] → ['cat','rat']
```

**loops with list**

- you can iterate over items directly

```python
for item in spam: print(item)
```

important to note that this directly interacts with the last

**iterate over indexes**

```python
for i in range(len(spam)):
    print(i, spam[i])
```

whereas this references the list using range

**membership operators**

```python
'cat' in ['dog','cat'] → True
'bird' not in ['dog','cat'] → True

```

**tuple unpacking**

```python
cat = ['fat','gray','loud']
size, color, mood = cat
```

notice how in order, it unpacks to corresponding variables

enumerate

- returns (index, value) in a loop

```python
for i, item in enumerate(['pens','staplers']):
    print(i, item)
```

random lists

```python
random.choice(lst) → random element.

random.shuffle(lst) → shuffle in place.
```

augmented assignment

```python
bacon = ['Zophie']
bacon *= 3 → ['Zophie','Zophie','Zophie']
```

list methods

```python
index(val) → first index of value.

append(val) → add to end.

insert(i,val) → add at position.

remove(val) → remove first occurrence.

sort() → sort list (in place).

reverse() → reverse order.
```

lists vs strings

- both are sequences (supports indexing, slicing, len(), membership options and loops)
- lists are mutable (changeable items)
- strings are immutable (must create new strings

tuples

- similar to lists, immutable
- uses ()
- tuples are faster and signal fixed data

type conversion

```python
list(('cat','dog')) → ['cat','dog']

tuple(['cat','dog']) → ('cat','dog')

list('hello') → ['h','e','l','l','o']
```

References

- Variables hold references and not actual list values

Copying lists

- assignments don’t copy lists and they just copy the reference

```python
spam = [0, 1, 2]
eggs = spam
eggs[1] = 'Hi!'
print(spam)   # [0, 'Hi!', 2]
```

Notice how spam was changed although it was the eggs variable that the assignment operator was done on

sort()

- only works when all items are comporable

Short Circuit

```python
True or print("skip")
```

If LHS is true, it prints nothing as left side is already true