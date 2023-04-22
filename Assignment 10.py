fileH = open("input.txt", "r")
text = fileH.readlines()
fileH.close()

fileH = open("destination.txt", "w")
for s in text:
    fileH.write(s)
fileH.close()

print("\nFile Copied Successfully!")
