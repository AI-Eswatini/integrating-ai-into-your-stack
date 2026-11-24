"""
JSON is data written as text, so any program can send and read it.
The AI's JSON reply arrives as a string; json.loads() turns it into a dict or
list, json.dumps() turns Python data back into text.

Notebook: ask_json() reads the AI's reply, Part 3 sends tool results back.
(Not named json.py: that would hide Python's own json module.)
"""

import json

# what the AI sends back: text that looks like data
text = '{"item": "eggs", "quantity": 12, "urgent": false}'

print(type(text))
# text["item"] would fail: it's a string, not a dict

order = json.loads(text)

print(type(order))
print(order["item"])
print(order["urgent"])  # JSON false becomes Python False

order["quantity"] = 24

# and back to text, to send to an API or save to a file
print(json.dumps(order))
print(json.dumps(order, indent=2))
