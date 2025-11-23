#a
filename = "example.txt"
lines = 0
words = 0
characters = 0
with open(filename, "r") as file:
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

print("Total Lines:", lines)
print("Total Words:", words)
print("Total Characters:", characters

#b
filename = "example.txt"
lines_list = []

with open(filename, "r") as file:
    for line in file:
        lines_list.append(line.strip())

print(lines_list)

#c
import csv

filename = "data.csv"

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#d
 file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
merged = open("merged.txt", "w")

data1 = file1.read()
data2 = file2.read()

merged.write(data1)
merged.write("\n")      # line break so both files look separate
merged.write(data2)

file1.close()
file2.close()
merged.close()

# PRINT the merged output on terminal also
print("---- Merged Output ----")
print(data1)
print(data2)
