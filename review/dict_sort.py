'''
sorted function in python creates ascending result by default

If we sort a dictionary, we sort by its keys by default
'''

counts = {"search":5, "payment":8, "profile":3}
result = sorted(counts)
# ['payment', 'profile', 'search']

# default ascending order
result = sorted(counts.items(), key=lambda x: x[1])
# print(result)
'''
[('profile', 3), ('search', 5), ('payment', 8)]
'''

# descending
result = sorted(counts.items(), key=lambda x: -x[1])
print(result)
# [('payment', 8), ('search', 5), ('profile', 3)]

# descending by value, then key ascending
counts = {"search":8, "payment":8, "profile":3}
result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
print(result)
# [('payment', 8), ('search', 8), ('profile', 3)]

# ascending by value, then key descending
