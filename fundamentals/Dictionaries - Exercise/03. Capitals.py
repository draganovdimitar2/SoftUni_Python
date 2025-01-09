countries = input().split(', ')
capitals = input().split(', ')
mydict = {country: capital for (country, capital) in zip(countries, capitals)}
# another way -> using dict comprehension
for country, capital in mydict.items():
    print(f'{country} -> {capital}')

# countries = input().split(', ')
# capitals = input().split(', ')
# mydict = dict(zip(countries, capitals))  # zip returns an iterator object, that's why it needs dict()
#
# for country,capital in mydict.items():
#     print(f'{country} -> {capital}')
