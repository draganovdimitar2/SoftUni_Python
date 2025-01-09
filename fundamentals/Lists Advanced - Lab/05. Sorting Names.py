name_list = input().split(", ")
sorted_names = sorted(name_list, key=lambda name: (-len(name), name))
print(sorted_names)
