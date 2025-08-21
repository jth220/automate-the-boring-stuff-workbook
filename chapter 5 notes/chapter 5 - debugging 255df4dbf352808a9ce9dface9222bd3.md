# chapter 5 - debugging

Raising exceptions

- whenever invalid code is executed, it raises an exception

raise keyword

- you can raise your own exception message
- using the raise keyword
- then call the Exception() function when it encounters an error

```python
raise Exception("Helpful error message")

```

common uses

- inside a function
- the caller (code using the function) handles error with try/except

```python
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string")
    if width <= 2:
        raise Exception("Width must be greater than 2")
    if height <= 2:
        raise Exception("Height must be greater than 2")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

```

caller handles error

```python
try:
    box_print("ZZ", 3, 3)
except Exception as err:
    print("An exception happened:", str(err))
```

Exception is the class of errors to catch

err is the exception object instance that was raised

Key benefits

- enforce constraint and fail fast
- keeps code robust by handling invalid inputs gracefully
- prevents whole program from crashing

**Assertions**

- sanity check to ensure code isn’t doing something wrong
- raises AssertionError if these checks fail
- consists of the assert keyword
- a condition
- comma
- and a string to display when the condition is False

```python
>>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.sort()
>>> ages
[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
>>> assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.
```

Obviously the sort will sort the arrays from ascending order

- the assert function is followed by a condition that checks if the first index is ≤ the last age
- once it evaluates to true, then the statement does nothing
- otherwise if it evaluates to false, then an assertion error is raised

Benefits

- fail fast
- your program should crash, to shorten the time to identify the original cause of the bug
- programmer errors rather than user errors

**Logging**

Logging module - use to create a record of custom messages to describe how the program is running

- use to indicate when things go wrong, skipped or never executed

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
```

basicConfig() lets you specify what level of details you want to see and how those details are displayed

- logging.debug() function to print log information
- debug() function calls basicConfig() and prints a line of information in the format we specified in the function call

```python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')
```

```python
2035-05-23 16:20:12,664 - DEBUG - Start of program
2035-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2035-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2035-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2035-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2035-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2035-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2035-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2035-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2035-05-23 16:20:12,684 - DEBUG - End of program
```

- Logging in this example shows where logging messages are printed
- in this example, using logs, we can identify the variables whilst a program is being executed without having to use a print statement

**Logfiles**

- **logging.basicConfig() takes a filename named parameter**
- This will save log messages to a .txt file

Poor Practice : Debugging with print()

- This is because when you are done debugging, you may want to remove print() from your code for each message
- Where as you can simply disable logging using (logging.disable(logging.CRITICAL) call (you can selectively disable by levels)

| **Level** | **Logging function** | **Description** |
| --- | --- | --- |
| DEBUG | logging.debug() | The lowest level, used for small details. Usually, you’ll care about these messages only when diagnosing problems. |
| INFO | logging.info() | Used to record information about general events in your program or to confirm that it’s working at various points. |
| WARNING | logging.warning() | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future. |
| ERROR | logging.error() | Used to record an error that caused the program to fail to do something. |
| CRITICAL | logging.critical() | The highest level, used to indicate a fatal error that has caused, or is about to cause, the program to stop running entirely. |

Debugger (Mu / IDLE / IDE)

- Runs program one line at a time, inspect variable values step by step
- see exact program flow and variable states instead of guessing

Debugger Options

- Continue - runs normally until end or a breakpoint
- Step in - enter function calls, see inside
- Step Over - runs the line but skips inside functions
- Step out - finish current function and return to caller
- Stop - immediately terminate program

Breakpoints

- set a breakpoint - debugger pauses automatically at the line
- useful for when you don’t want to step line by line for large loops
- click the line number (read dot appears) to toggle breakpoint