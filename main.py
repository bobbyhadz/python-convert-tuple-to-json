# Convert a Tuple to JSON in Python

import json

my_tuple = ('bobby', 'hadz', 'com')

json_str = json.dumps(my_tuple)

print(json_str)  # 👉️ '["bobby", "hadz", "com"]'
print(type(json_str))  # 👉️ <class 'str'>