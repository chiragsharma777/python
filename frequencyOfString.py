text = input("Enter a string: ")

frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("Character frequency:")

for char, count in frequency.items():
    print(char, ":", count)