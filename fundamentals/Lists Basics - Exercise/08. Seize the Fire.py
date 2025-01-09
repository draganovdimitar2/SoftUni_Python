fire_cells = input()
water = int(input())
fire_cells = fire_cells.split('#')

total_effort = 0
total_fire = 0
cells_put_out = []

for cell in fire_cells:
    type_of_fire, value_of_cell = cell.split(' = ')
    value_of_cell = int(value_of_cell)
    
    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        valid = True
    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        valid = True
    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        valid = True
    else:
        valid = False
    
    if valid and water >= value_of_cell:
        water -= value_of_cell
        effort = value_of_cell * 0.25
        total_effort += effort
        total_fire += value_of_cell
        cells_put_out.append(value_of_cell)

print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")