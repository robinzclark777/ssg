import re

text = "fish dog cat fish dog cat"
print(f"text is {text}")
pattern = r'dog cat'
print(f"pattern is 'dog cat'")
print("findall results:")
print(re.findall(pattern, text))
print("split results:")
print(re.split(pattern, text))

