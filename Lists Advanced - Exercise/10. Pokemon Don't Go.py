sequence = list(map(int, input().split()))

total_sum = 0

while sequence:
    index = int(input())

    if index < 0:
        removed_value = sequence.pop(0)
        sequence.insert(0, sequence[-1])
    elif index >= len(sequence):
        removed_value = sequence.pop(-1)
        sequence.append(sequence[0])
    else:
        removed_value = sequence.pop(index)

    total_sum += removed_value

    sequence = [
        num + removed_value if num <= removed_value else num - removed_value
        for num in sequence
    ]

print(total_sum)
