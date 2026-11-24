"""
A string is text inside quotes: "Hello", 'eggs'. Three quotes allow many lines.
Prompts are strings and the AI's reply is a string, so most AI work is
building text to send and cleaning up the text that comes back.

Notebook: every prompt, and splitting the batched labels in 1.3.
"""

name = "Thembinkosi"
item = "eggs"
price = 4.5

print("Hello " + name)
# or, with an f-string
print(f"Hello {name}, {item} cost R{price:.2f} each")

reply = "  ORDER\n"
print(reply.strip())
print(reply.strip().lower())

labels = "ORDER\nCOMPLAINT\nQUESTION"
print(labels.splitlines())

notes = """
Bed 3: chest pain.
Bed 5: fever.
"""
print("Summarise these notes:\n" + notes)
