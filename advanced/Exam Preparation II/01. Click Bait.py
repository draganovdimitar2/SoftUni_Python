from collections import deque

links = deque([int(x) for x in input().split()])
articles = [int(x) for x in input().split()]
target_value = int(input())
FFD = []

while links and articles:
    links_el = links.popleft()
    articles_el = articles.pop()
    greater_element = max(links_el, articles_el)  # dividend
    smaller_element = min(links_el, articles_el)  # divisor
    remainder = greater_element % smaller_element

    if articles_el > links_el:
        FFD.append(remainder)
        if remainder != 0:
            articles.append(remainder * 2)
    elif articles_el < links_el:
        FFD.append(-remainder)
        if remainder != 0:
            links.append(remainder * 2)
    else:  # if they are equal
        FFD.append(0)

print(f'Final Feed: {", ".join(str(el) for el in FFD)}')
total_value = sum(FFD)
if total_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_value}")
else:
    shortfall = target_value - total_value
    print(f"Goal not achieved! Short by: {shortfall}")
