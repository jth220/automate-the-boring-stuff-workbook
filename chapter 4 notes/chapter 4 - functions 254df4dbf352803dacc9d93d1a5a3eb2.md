# chapter 4 - functions

functions

- prevent duplicate code
- creates abstraction (black box, no need to see the machinery, just in and comes with an out)
- organise modular chunks

parameters - variables inside a function that receives arguments

arguments - values you pass in

def statements

- states a function
- function executes once called

function calls

- function can be called by the functions name and () after
- this can be done in combination with number of arguments in the parenthesis
- once a function is finished, returns to the line where it was called

Return values and return statement

- you can specify return values with a return statement
- return keyword followed by the value or expression that the function should return
- return values can be passed into arguments to other functions

None value

- none represents absence of value
- every function always returns something, default is None

Named arguments

- functions can have named arguments in which can require input
- a strong example is print(), can include end=”” at the end (meaning it doesn’t create a new line that it normally does)

call stack

- functions execute functions in order, until that function is completed it will return to the function that called it previously

Frame object

- store line number of the original function call so python remembers where to return, it will keep adding frame objects above the other on that call stack

Local and Global Scopes

- code within a function can access those parameters and variables assigned in that block (local scope)
- code anywhere in the program can be accessed (global scope)

scope rule

- code in the global scope can’t use local variables
- code in a function can’t use variables in any other local scope
- code in a local scope can access global variables
- same names can be used for different variables in different scopes

Exception Handling

- errors can be handled with try and except statements
- potential error statements can use a try clause
- except clause is used if an error happens
- execution jumps to except immediately after an error and will never go back to try (important for debugging flow)

global lets you modify global inside a function

however it is best to use return values