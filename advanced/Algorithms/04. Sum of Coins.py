def choose_coins(coins, target):
    coins.sort(reverse=True)
    used_coins = {}

    idx = 0
    while target != 0 and idx < len(coins):
        coins_count = target // coins[idx]
        target %= coins[idx]

        if coins_count > 0:
            used_coins[coins[idx]] = coins_count

        idx += 1

    if target != 0:
        return 'Error'

    result = f'Number of coins to take: {sum(used_coins.values())}\n'
    for value, count in used_coins.items():
        result += f'{count} coin(s) with value {value}\n'

    return result.strip()


coin_list = [int(x) for x in input().split(', ')]
target_sum = int(input())

print(choose_coins(coin_list, target_sum))
