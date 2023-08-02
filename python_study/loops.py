# While Loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

# For Loops
nums = [1, 2, 3, 4, 5]

for i in nums:
    print(i)

for i in range(10):
    print(i)
    # range(x, y) gives us all of the numbers from x to the input y, excluding y
        # when there is only one input for range(y), then it will assume x = 0

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}") 

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 3, 5, 2]
for x_count in numbers:
    output = ""
    for x in range(x_count):
        output += "x"
    print(output)