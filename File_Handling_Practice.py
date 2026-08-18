
# ============================================================
# 1. OPENING AND CLOSING A FILE
# ============================================================

file = open("example.txt", "w")
file.write("Hello Python!\n")
file.write("File handling is easy.\n")
file.close()

print("1. File created and closed successfully.")


# ============================================================
# 2. READING A FILE USING read()
# ============================================================

file = open("example.txt", "r")

content = file.read()
print("\n2. Output of read():")
print(content)

file.close()


# ============================================================
# 3. READING A FILE USING with STATEMENT
# ============================================================

with open("example.txt", "r") as file:
    content = file.read()

print("\n3. Reading using with:")
print(content)


# ============================================================
# 4. READING USING readline()
# ============================================================

with open("example.txt", "r") as file:
    first_line = file.readline()

print("\n4. Output of readline():")
print(first_line)


# ============================================================
# 5. READING USING readlines()
# ============================================================

with open("example.txt", "r") as file:
    lines = file.readlines()

print("\n5. Output of readlines():")
print(lines)


# ============================================================
# 6. READING FILE LINE BY LINE
# ============================================================

print("\n6. Reading line by line:")

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================================================
# 7. WRITING TO A FILE USING write()
#    w MODE OVERWRITES EXISTING CONTENT
# ============================================================

with open("write_demo.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This file was created using write().\n")

print("\n7. Data written using write().")


# ============================================================
# 8. WRITING MULTIPLE LINES USING writelines()
# ============================================================

lines = [
    "This is Delhi\n",
    "This is Paris\n",
    "This is London\n"
]

with open("writelines_demo.txt", "w") as file:
    file.writelines(lines)

print("8. Multiple lines written using writelines().")


# ============================================================
# 9. APPENDING TO A FILE USING a MODE
# ============================================================

with open("append_demo.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

# Append data
with open("append_demo.txt", "a") as file:
    file.write("Third line - appended\n")

print("\n9. Data appended successfully.")

with open("append_demo.txt", "r") as file:
    print(file.read())


# ============================================================
# 10. r+ MODE - READ AND WRITE
# ============================================================

with open("rplus_demo.txt", "w") as file:
    file.write("Hello World\n")

with open("rplus_demo.txt", "r+") as file:
    content = file.read()
    print("\n10. r+ mode - existing content:")
    print(content)

    file.write("New line added using r+\n")


# ============================================================
# 11. w+ MODE - WRITE AND READ
#    w+ OVERWRITES THE FILE
# ============================================================

with open("wplus_demo.txt", "w+") as file:
    file.write("Hello World!")

    # Move pointer to beginning
    file.seek(0)

    content = file.read()

print("\n11. w+ mode:")
print(content)


# ============================================================
# 12. BINARY FILE - WRITE USING wb
# ============================================================

with open("data.bin", "wb") as file:
    file.write(b"Hello Binary World")

print("\n12. Binary data written.")


# ============================================================
# 13. BINARY FILE - READ USING rb
# ============================================================

with open("data.bin", "rb") as file:
    data = file.read()

print("\n13. Binary data read:")
print(data)


# ============================================================
# 14. FILE POINTER - tell()
# ============================================================

with open("example.txt", "r") as file:
    position = file.tell()

    print("\n14. Current file pointer position:")
    print(position)


# ============================================================
# 15. FILE POINTER - seek()
# ============================================================

with open("example.txt", "r") as file:
    file.seek(5)

    print("\n15. Reading after seek(5):")
    print(file.read())


# ============================================================
# 16. read(n) - READ SPECIFIED NUMBER OF CHARACTERS
# ============================================================

with open("example.txt", "r") as file:
    data = file.read(5)

print("\n16. First 5 characters:")
print(data)


# ============================================================
# 17. readline(n) - READ SPECIFIED CHARACTERS FROM ONE LINE
# ============================================================

with open("example.txt", "r") as file:
    data = file.readline(5)

print("\n17. First 5 characters of first line:")
print(data)


# ============================================================
# 18. CHECK WHETHER FILE IS CLOSED - closed
# ============================================================

file = open("example.txt", "r")

print("\n18. Is file closed before close()?")
print(file.closed)

file.close()

print("Is file closed after close()?")
print(file.closed)


# ============================================================
# 19. EXCEPTION HANDLING WITH finally
# ============================================================

print("\n19. Exception handling using finally:")

file = None

try:
    file = open("example.txt", "r")

    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    if file is not None:
        file.close()

    print("File closed using finally.")


# ============================================================
# 20. CONTEXT MANAGER - with STATEMENT
#    AUTOMATICALLY CLOSES THE FILE
# ============================================================

with open("context_demo.txt", "w") as file:
    file.write("File automatically closes after with block.")

print("\n20. Context manager executed successfully.")


# ============================================================
# 21. CUSTOM CONTEXT MANAGER
# ============================================================

from contextlib import contextmanager


@contextmanager
def open_file(name, mode):
    file = open(name, mode)

    try:
        yield file

    finally:
        file.close()


with open_file("custom_context.txt", "w") as file:
    file.write("Using custom context manager.")

print("21. Custom context manager executed.")


# ============================================================
# 22. CSV FILE - WRITING USING csv.writer
# ============================================================

import csv

with open("people.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Rashmi", 30, "Pune"])
    writer.writerow(["Amit", 25, "Mumbai"])
    writer.writerow(["Sneha", 28, "Nashik"])

print("\n22. CSV file created using csv.writer.")


# ============================================================
# 23. CSV FILE - READING USING csv.reader
# ============================================================

print("\n23. Reading CSV using csv.reader:")

with open("people.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# 24. CSV - DictWriter
# ============================================================

with open("people_dict.csv", "w", newline="") as file:

    fieldnames = ["Name", "Age"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "Name": "Rashmi",
        "Age": 30
    })

    writer.writerow({
        "Name": "Amit",
        "Age": 25
    })

print("\n24. CSV created using DictWriter.")


# ============================================================
# 25. CSV - DictReader
# ============================================================

print("\n25. Reading CSV using DictReader:")

with open("people_dict.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# ============================================================
# 26. JSON - PYTHON DICTIONARY TO JSON
# ============================================================

import json

data = {
    "name": "Rashmi",
    "age": 30,
    "skills": ["Python", "ML"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("\n26. Python dictionary converted to JSON.")


# ============================================================
# 27. JSON - JSON TO PYTHON OBJECT
# ============================================================

with open("data.json", "r") as file:
    obj = json.load(file)

print("\n27. JSON data read into Python:")
print(obj)

print("Name:", obj["name"])
print("Skills:", obj["skills"])


# ============================================================
# 28. PICKLE - SAVE PYTHON OBJECT
# ============================================================

import pickle

numbers = [1, 2, 3, 4]

with open("data.pkl", "wb") as file:
    pickle.dump(numbers, file)

print("\n28. Python object saved using pickle.")


# ============================================================
# 29. PICKLE - LOAD PYTHON OBJECT
# ============================================================

with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("\n29. Pickle data loaded:")
print(loaded_data)


# ============================================================
# 30. XML - CREATING XML FILE
# ============================================================

import xml.etree.ElementTree as ET

root = ET.Element("people")

person1 = ET.SubElement(
    root,
    "person",
    attrib={"id": "1"}
)

ET.SubElement(person1, "name").text = "Rashmi"
ET.SubElement(person1, "age").text = "30"

person2 = ET.SubElement(
    root,
    "person",
    attrib={"id": "2"}
)

ET.SubElement(person2, "name").text = "Amit"
ET.SubElement(person2, "age").text = "25"

tree = ET.ElementTree(root)

tree.write("people.xml")

print("\n30. XML file created.")


# ============================================================
# 31. XML - READING XML FILE
# ============================================================

tree = ET.parse("people.xml")

root = tree.getroot()

print("\n31. Reading XML:")

for person in root:

    person_id = person.attrib["id"]
    name = person.find("name").text
    age = person.find("age").text

    print(person_id, name, age)


print("================================================")