from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])
scored_goals = 0

while strength and accuracy:
    current_sum = accuracy[0] + strength[-1]

    if current_sum == 100:
        scored_goals += 1
        accuracy.popleft(), strength.pop()

    elif current_sum < 100:
        if accuracy[0] > strength[-1]:
            strength.pop()
        elif accuracy[0] < strength[-1]:
            accuracy.popleft()
        else:
            strength.pop()
            strength.append(current_sum)
            accuracy.popleft()

    else:
        strength[-1] -= 10
        accuracy.rotate(-1)

if scored_goals:
    if scored_goals == 3:
        print("Paul scored a hat-trick!")
    elif scored_goals > 3:
        print("Paul performed remarkably well!")
    else:
        print("Paul failed to make a hat-trick.")
    print(f"Goals scored: {scored_goals}")
else:
    print("Paul failed to score a single goal.")

if strength:
    print(f'Strength values left: {", ".join([str(x) for x in strength])}')
if accuracy:
    print(f'Accuracy values left: {", ".join([str(x) for x in accuracy])}')
