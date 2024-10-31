# Get the size of the array and elements from the user
n = int(input("Enter the size of the array: "))
array = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# Initialize largest and smallest with the first element
largest = array[0]
smallest = array[0]

# Traverse the array
for num in array:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Print results
print("Largest number:", largest)
print("Smallest number:", smallest)
