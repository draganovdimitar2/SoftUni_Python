n = int(input())
parking_lot = set()

for _ in range(n):
    command = input().split(', ')
    direction = command[0]
    car_number = command[-1]

    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if len(parking_lot) > 0:
    print('\n'.join(car_num for car_num in parking_lot))
else:
    print("Parking Lot is Empty")
