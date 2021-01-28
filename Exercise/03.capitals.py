country = input().split(", ")
capital_cities = input().split(", ")

country_capital = list(zip(country, capital_cities))

result = {el[0]: el[1] for el in country_capital}
for country, city in result.items():
    print(f"{country} -> {city}")
