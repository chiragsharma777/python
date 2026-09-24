print("===== NUMBER ANALYSIS =====")

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

print("\nNumbers:", numbers)

largest = numbers[0]
smallest = numbers[0]
even = 0
odd = 0
positive = 0
negative = 0

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

total = sum(numbers)
average = total / n

print("\n===== RESULT =====")
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Total:", total)
print("Average:", average)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Positive Numbers:", positive)
print("Negative Numbers:", negative)