numbers = list(map(int, input().split(", ")))
group = 10

while numbers:  # Loop until all numbers are processed
    current_group = [num for num in numbers if num <= group]  # Get numbers in current group
    print(f"Group of {group}'s: {current_group}")
    numbers = [num for num in numbers if num > group]   # Remove the numbers that were already grouped
    group += 10