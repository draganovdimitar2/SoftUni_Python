first_sequence = input().split(", ")
second_sequence = input().split(", ")

result = [substring for substring in first_sequence if any(substring in word for word in second_sequence)]

print(result)
