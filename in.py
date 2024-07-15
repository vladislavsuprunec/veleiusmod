import re

acronym9 = r'\b(\w+)\s/\s(\w+)\b'

text = "This is a test with w1 / w2 acronym"

matches = re.findall(acronym9, text)
print(matches)
