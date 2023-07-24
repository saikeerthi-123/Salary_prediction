import re

with open('setup.py', 'r') as f:
    content = f.read()
    match = re.search(r'name\s*=\s*[\'\"]([^\'\"]+)[\'\"]', content)
    if match:
        print(match.group(1))
