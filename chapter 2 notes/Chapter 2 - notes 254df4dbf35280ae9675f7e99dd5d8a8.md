# Chapter 2 - notes

IF-ELSE and FLOW CONTROL

**flow control statements** - python instructions execute under conditions

Boolean Values

- two type of values (true and false)

== operator asks whether two values are the same as each other

= operator puts values on the right into variable on the left

**Components of Flow Control**

- starts with condition, followed by block of code (clause)
- note that a condition will always evaluate to a Boolean value

**Blocks of code**

- block begins when indentation increase
- blocks can contain other blocks

**Colons**

- flow control statements end wit ha colon and followed by a clause

**else** - doesn't necessarily have a condition, always follows after an if statement doesn’t evaluate to true

**elif** - when you want one of many possible clauses to execute, after it follows an if or another elif statement (provided all previous conditions were False)

Boolean operators : evaluation order = not → and → or

short circuit : A and B will stop at A if A is false, like wise A or B will stop if A is true

True vs ‘True’ Booleans are not strings, non empty strings always evaluate as truthy

Elif ordering - first true condition executes, later ones are skipped, order matters

Else clause - ensures one block will execute if no conditions match (catches all)

Outcome

Order matters

be aware of short circuits