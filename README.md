# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

Name: todo_checker
Parameters: one string
Return: return a boolean (true/false)

>>> includes_todo("#TODO buy milk")
True
>>> includes_todo("drink tea")
False
>>> includes_todo("learn to test-drive my code #TODO")
True


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a empty string
It returns FALSE
"""
todo_checker("") => False

"""
Given #TODO is lowercase 
It returns True
"""
todo_checker("#todo buy milk") => True

"""
Given any value other than a string
It returns Error - Please entry a string
"""
todo_checker(2000) => "Please entry a string"


"""
Given only #TODO
It returns an error - Please also include task
"""
todo_checker("#TODO") => "Please also include task"

"""
Given #TODO
It returns True
"""
todo_checker("#TODO buy milk") => True

"""
Given an string contains no #TODO
It returns False
"""
todo_checker("buy milk") => False


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
