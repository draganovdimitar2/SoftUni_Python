journey_price = float(input())
months_to_collect_money = int(input())
collected_money = 0

for month in range(1, months_to_collect_money+1):
    if month % 2 != 0 and month != 1:
        collected_money -= collected_money * 0.16  # spend 16% on every odd month except the first one
    if month % 4 == 0:
        collected_money += collected_money * 0.25

    collected_money += journey_price * 0.25  # save 25 % of the cost of the journey

if collected_money >= journey_price:
    print(f"Bravo! You can go to Disneyland and you will have {collected_money-journey_price:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_price-collected_money:.2f}lv. more.")

