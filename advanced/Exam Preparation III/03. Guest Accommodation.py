def accommodate(*args, **kwargs):
    room_data = {int(room_num[5:]): capacity for room_num, capacity in kwargs.items()}
    sorted_room_data = sorted(room_data.items(), key=lambda x: (x[1], x[0]))
    total_guests = sum(args)

    successful_accommodations = 0
    accommodation_rooms = {}
    result = []  # empty list for result output

    for guests in args:
        for room_num, capacity in sorted_room_data:
            if capacity >= guests:
                sorted_room_data.remove((room_num, capacity))
                successful_accommodations += 1
                total_guests -= guests
                accommodation_rooms[room_num] = guests
                break

    if successful_accommodations:
        result.append(f'A total of {successful_accommodations} accommodations were completed!')
        for room_num, guests in sorted(accommodation_rooms.items()):
            result.append(f'<Room {room_num} accommodates {guests} guests>')
    else:
        result.append(f"No accommodations were completed!")

    if total_guests > 0:  # if there are guests left
        result.append(f"Guests with no accommodation: {total_guests}")
    if sorted_room_data:  # if there are empty rooms
        result.append(f"Empty rooms: {len(sorted_room_data)}")

    return "\n".join(result)
