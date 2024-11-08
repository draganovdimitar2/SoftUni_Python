filled_shelds = []
n = 0
shell = 0
electrons = int(input())

while electrons > 0:
    n += 1
    shell = (n**2)*2
    if electrons < shell:
        filled_shelds.append(electrons)
        break
    else:
        filled_shelds.append(shell)
        electrons -= shell

print(filled_shelds)