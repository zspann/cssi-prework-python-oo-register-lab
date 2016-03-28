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

The `CashRegister` class is a blueprint that models attributes (adjectives) and methods (verbs) of an actual register.

### Adding Items
Items should be able to be added with their title, price and an option quantity using the `add_item` method

The register should keep track of which items have been purchased and keep a running total of the purchases.
```python
>>>cash_register.add_item("eggs", 0.98)
>>>cash_register.total
.98
>>>cash_register.items
["eggs"]
>>>cash_register.add_item("magazine", 5.00, 3)
>>>cash_register.total
15.98
>>>cash_register.items
["eggs", "magazine", "magazine", "magazine"]
```

### Discounts
Each time a new register is initialized, a discount can be added. This discount does not affect the total until the class method apply_discount is called.

In addition, the `apply_discount` method should return a message: `"After the discount, the total comes to $TOTAL."` where TOTAL is the current total for any added items.

If there is no discount for the current register, the returned message should be `"There is no discount to apply".`

```python
>>>cash_register2=CashRegister(20)
>>>cash_register2.add_item("chicken", 10)
>>>cash_register2.apply_discount()
"After the discount, the total comes to $8.00."
>>>cash_register2.total
8

```

### Void the Last Transaction

The `void_last_transaction` method will remove the last transaction from the total. You'll need to make an additional attribute and keep track of the number of recent items added to a list and one to keep track of their value.

Make sure your method can handle instances where the last transaction could include a quantity of 1 or greater.

```python
>>>cash_register.add_item("chicken", 10)
>>>cash_register.add_item("tomato", 1.76, 2)
>>>cash_register.items
["chicken", "tomato", "tomato"]
>>>cash_register.void_last_transaction()
>>>cash_register.total
10
>>>cash_register.items
["chicken"]
```

**This is a test-driven lab!** Follow along with the tests in `register_test.py`. By completing one test at a time, you'll end up with a relatively complex class at the end.

You can always run `python register_test.py` from the command line to clue you into your next step.

For example, if we run it without creating any code, we'll see that we first need to define  class called `CashRegister`
```python
>>>python register_test.py
Traceback (most recent call last):
  File "register_test.py", line 4, in <module>
    from register import CashRegister
ImportError: cannot import name CashRegister
```
All great developers, take their code one step at a time. Write one piece of functionality and make sure you get a new test to pass before moving on.


## Resources
* [String Formatting](https://mkaz.tech/python-string-format.html)
