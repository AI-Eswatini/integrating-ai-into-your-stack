"""
A function is a named set of steps: give it inputs, it returns a result.
Like a recipe, write it once and use it many times. It only runs when called.

Notebook: ask(), ask_json(), and running the AI's tool calls in Part 3.
"""

def greet(name):
    return f"Hello {name}"


print(greet("Thembinkosi"))


def order_total(price, quantity):
    """Work out the cost of one order line."""
    return price * quantity


print(order_total(4.5, 12))
# or, naming the arguments
print(order_total(quantity=12, price=4.5))

# the AI sends arguments as a dict, ** unpacks it into named arguments
arguments = {"price": 4.5, "quantity": 12}
print(order_total(**arguments))

# functions can be stored in a dict and looked up by name
functions = {"order_total": order_total}
print(functions["order_total"](**arguments))
