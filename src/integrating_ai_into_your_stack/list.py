"""
A list holds many values in order: ["eggs", "bread", "milk"].
Like a shopping list or an inbox. Positions start at 0, so items[0] is the first.
Use a list for many things of the same kind, a dict for one thing with named fields.

Notebook: the messages to sort, and an order's "items" (a list of dicts).
"""

messages = [
    "Do you open on Sunday?",
    "pls send 2 breads and milk to number 14",
]

print(messages[0])
print(len(messages))

messages.append("The eggs I bought yesterday were broken!")

print(messages)

messages.remove("Do you open on Sunday?")

print(messages)

# a list can hold dicts too
order = [
    {"item": "eggs", "quantity": 12},
    {"item": "bread", "quantity": 2},
]

print(order[0]["item"])
