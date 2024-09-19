budget = float(input())
price_per_kg_flour = float(input())
pack_of_eggs = 0.75 * price_per_kg_flour
milk = (1.25 * price_per_kg_flour) / 4
loaves = 0
colored_eggs = 0

while True:

    if budget >= pack_of_eggs + price_per_kg_flour + milk:
        budget -= pack_of_eggs
        budget -= price_per_kg_flour
        budget -= milk
        loaves += 1
        colored_eggs += 3

    else:
        break

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')