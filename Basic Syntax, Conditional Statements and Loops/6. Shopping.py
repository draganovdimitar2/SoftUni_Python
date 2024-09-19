budget = int(input())
command = input()

while command.isdigit():
    command = int(command)
    budget -= command
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")