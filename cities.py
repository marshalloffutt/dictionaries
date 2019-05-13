# 6-11

cities = {
    'new york': {
        'country': 'united states',
        'population': 8622698,
        'fun fact': 'the movie home alone 2 was shot here',
    },
    'london': {
        'country': 'england',
        'population': 8825000,
        'fun fact': 'there are no lions in london',
    },
    'paris': {
        'country': 'france',
        'population': 2206488,
        'fun fact': 'french people speak french',
    },
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fun_fact = city_info['fun fact']

    print("\n" + city.title() + ":")
    print("\t Country: " + country.title())
    print("\t Population: " + str(population))
    print("\t Fun fact: Did you know that " + fun_fact + "?")
