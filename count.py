numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20, 50]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element Frequency:")

for key, value in frequency.items():
    print(key, "->", value)