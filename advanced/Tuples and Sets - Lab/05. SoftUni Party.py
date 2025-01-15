n = int(input())
vip_guests = set()
regular_guests = set()

for _ in range(n):
    guest_num = input()
    if guest_num[0].isdigit():
        vip_guests.add(guest_num)
    else:
        regular_guests.add(guest_num)

command = input()
while command != 'END':
    if command[0].isdigit():
        vip_guests.remove(command)
    else:
        regular_guests.remove(command)
    command = input()

absent_guests = sorted(vip_guests) + sorted(regular_guests)

print(len(absent_guests))  # Number of absent guests
print("\n".join(absent_guests))
