import re

# find digits in a string
res = re.findall(r"-?\d+", "sdflsj90 sdf32 34 -120")
print(res)
# ['90', '32', '34', '-120']

''' 
negative decimal numbers

(?:       start a non-capturing group
\.        literal decimal point
\d+       one or more digits
)         end the group
?         the entire group is optional

'''
text = "Temperatures: -12.5, 8.2, -0.75"

numbers = re.findall(r"-?\d+(?:\.\d+)?", text)

print(numbers)
# ['-12.5', '8.2', '-0.75']

'''
Capture values
'''
text = "search: 120ms, payment: -35ms"
matches = re.findall(r"(\w+):\s*(-?\d+)ms", text)
print(matches)
# [('search', '120'), ('payment', '-35')]
result = {name: int(val) for name, val in matches}
# print(result)

'''
search only return the first result
pattern = re.compile(r"(\w+):\s*(-?\d+)ms")
matches = pattern.search(text)
result = {}
'''

'''
Advanced split
split a string whenever it finds
a comma ,
a semicolon ;
a pipe |
followed by zero or more whitespace characters
'''
text = "search, 120; payment| -35"

parts = re.split(r"[,;|]\s*", text)

print(parts)