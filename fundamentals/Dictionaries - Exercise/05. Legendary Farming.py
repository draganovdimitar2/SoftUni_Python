items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
command = input().split(' ')
won_item = ''
flag_var = False
while not flag_var:
    for i in range(0, len(command), 2):
        material = command[i + 1].lower()
        quantity = int(command[i])

        if material in items:
            items[material] += quantity

            if items[material] >= 250:

                if material == 'shards':
                    won_item = "Shadowmourne"
                elif material == 'fragments':
                    won_item = "Valanyr"
                else:
                    won_item = "Dragonwrath"

                items[material] -= 250
                flag_var = True
                break

        else:
            if material in junk_items.keys():
                junk_items[material] += quantity
            else:
                junk_items[material] = quantity
    if flag_var:
        break
    command = input().split(' ')

print(f"{won_item} obtained!")
print(
    f'shards: {items["shards"]}\n'
    f'fragments: {items["fragments"]}\n'
    f'motes: {items["motes"]}'
)
for k, v in junk_items.items():
    print(f'{k}: {v}')
