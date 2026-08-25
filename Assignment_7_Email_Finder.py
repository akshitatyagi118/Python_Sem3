import re

text = """
Contact us at student@gmail.com for more information.
You can also email admin@college.edu or support123@yahoo.com.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)
