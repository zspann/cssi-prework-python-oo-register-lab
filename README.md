# Object Oriented Cash Register

## Objectives

1. Build a class with instance methods.
2. Call instance methods inside of other instance methods.
3. Use instance methods to track information pertinent to an instance of a class.

## Description

We're going to create an Object Oriented Cash Register that can:
* Add items of varying quantities and prices
* Calculate discounts
* Keep track of what's been added to it
* Void the last transaction

## Instructions

**This is a test-driven lab!** You will need to read the `register_test.py` file and the test output very carefully to solve this one.

**Hint #1:** Keep in mind that to call an instance method *inside* another instance method, we use the `self` keyword to refer to the instance on which we are operating. For example:

```python
class Person:
  def __init__(self,age):
    self.age = 0
  def birthday(self):
    self.age += 1
```

Follow along with the tests in `register_test.py`. By completing one test at a time, you'll end up with a relatively complex class at the end.

Take it one step at a time!

**Hint #2:** The `void_last_transaction` method will remove the last transaction from the total. You'll need to make an addition attribute and keep track of that last transaction amount somehow. In what method of the class are you working with an individual item?

## Resources
* [String Formatting](https://mkaz.tech/python-string-format.html)
