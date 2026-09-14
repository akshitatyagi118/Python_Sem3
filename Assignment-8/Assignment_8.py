# Program to count lines, extract first two lines,
# and write them into a new file

# Open the input file
file = open("input.txt", "r")

# Read all lines
lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Display line count
print("Total number of lines:", line_count)

# Extract first two lines
first_two_lines = lines[:2]

# Close input file
file.close()

# Open output file
output_file = open("output.txt", "w")

# Write first two lines into output file
for line in first_two_lines:
    output_file.write(line)

# Close output file
output_file.close()

print("First two lines have been written to output.txt")


# ---------------- OUTPUT ----------------
# Total number of lines: 5
# First two lines have been written to output.txt


# ---------------- output.txt ----------------
# Python is a programming language.
# It is easy to learn.