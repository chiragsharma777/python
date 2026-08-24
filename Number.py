numbers = [12, 45, 7, 23, 45, 89, 34, 89, 56]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("No second largest element")
else:
    print("Largest:", largest)
    print("Second Largest:", second_largest)