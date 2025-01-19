from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))
crafted_presents = {}
table = {  # required magic : present
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic_level:
    total_magic_level = materials[-1] * magic_level[0]
    if total_magic_level in table:
        present = table[total_magic_level]
        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
        materials.pop(), magic_level.popleft()
    elif total_magic_level < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif total_magic_level > 0:
        magic_level.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()

if ('Doll' in crafted_presents and "Wooden train" in crafted_presents) or (
        "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}") if materials else None
print(f"Magic left: {', '.join([str(x) for x in magic_level])}") if magic_level else None
for k, v in sorted(crafted_presents.items()):
    print(f'{k}: {v}')
