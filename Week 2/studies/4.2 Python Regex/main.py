import re

test_string = "123abc456789abc123ABC"


pattern = re.compile(r'abc')
# 'r' prefix means it is a raw string
matches=pattern.finditer(test_string)


for match in matches:
    print(match.start(),match.end(),match.group())