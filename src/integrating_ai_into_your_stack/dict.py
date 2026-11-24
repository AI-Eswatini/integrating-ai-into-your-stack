"""
A dict stores data as key-value pairs: {"name": "Thembinkosi", "age": 20}.
Like a form: each label (key) has an answer (value), so you look things up
by name instead of by position. Keys are unique.

Notebook: every structured AI response becomes a dict, e.g. result["category"].
"""

user = {
    "name": "Thembinkosi",
    "surname": "Mkhonta",
    "age": 20,
}

# Read a value
print(user["name"])
# or, with .get()
print(user.get("name"))

# .get() is safer: a missing key gives None (or a default) instead of an error
print(user.get("email"))
print(user.get("email", "no email"))

# Check if a key exists
print("age" in user)

# Change a value
user["age"] = 29
print(user["age"])

# Add a new key
user["email"] = "thembi@example.com"
print(user)

# Remove a key
user.pop("age")
print(user)

# Loop over keys and values
for key, value in user.items():
    print(key, "=", value)

# A dict can hold other dicts, like the shop's stock in the notebook
stock = {
    "eggs": {"price": 4.50, "in_stock": 30},
    "bread": {"price": 18.00, "in_stock": 20},
}

print(stock["eggs"]["price"])
print(stock.get("sugar", "We don't sell sugar"))
