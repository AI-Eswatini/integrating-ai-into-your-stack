"""
A for loop repeats the same steps for every item in a list.
if / else runs code only when something is true. Indented lines belong to the block.

Notebook: numbering and matching messages in 1.3, checking stock in Part 4.
"""

messages = [
    "Do you open on Sunday?",
    "pls send 2 breads and milk to number 14",
    "The eggs I bought yesterday were broken!",
]

for message in messages:
    print(message)

# number each item, starting from 1
for i, message in enumerate(messages, 1):
    print(f"{i}. {message}")

# walk two lists side by side
labels = ["QUESTION", "ORDER", "COMPLAINT"]
for label, message in zip(labels, messages):
    print(label, "-", message)

# if / else
stock = 0
if stock > 0:
    print("In stock")
else:
    print("Not available")

# build a new list from an old one
complaints = [message for message, label in zip(messages, labels) if label == "COMPLAINT"]
print(complaints)
