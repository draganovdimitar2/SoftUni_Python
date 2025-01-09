A = []
B = []
command = input().split()
game_terminated = False  

for char in command:
    if char[0] == 'A' and char not in A:
        A.append(char)
    elif char[0] == 'B' and char not in B:
        B.append(char)
    
    if len(A) > 4 or len(B) > 4: 
        game_terminated = True
        break  

print(f'Team A - {11-len(A)}; Team B - {11-len(B)}')

if game_terminated:
    print('Game was terminated')
