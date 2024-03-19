def print_capitals():
    country_list = input().split(', ')
    capital_list = input().split(', ')
    pairs = {}

    pairs = {country: city for country, city in zip(country_list, capital_list)}
    # print(pairs)

    for country, city in pairs.items():
        print(f'{country} -> {city}')


print_capitals()
