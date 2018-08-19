# Maps countries to abbrevation.
countries = {
    'England': 'Eng',
    'France': 'Fra',
    'Germany': 'Ger',
    'Italy': 'Ita',
    'Spain': 'Esp'
}

# Lists some countries and capitals.
capitals = {
    'Eng': 'London',
    'Fra': 'Paris',
    'Ger': 'Berlin'
}

# Adding more capitals.
capitals['Ita'] = 'Rome'
capitals['Esp'] = 'Madrid'

#prints some cities.
print('-' * 10)
print("Ita capital is: ", capitals['Ita'])
print("Esp capital is: ", capitals['Esp'])

# prints some countries.
print('-' * 10)
print("France's abbrevation is: ", countries['France'])
print("Germany's abbrevation is: ", countries['Germany'])

# Use the countries then capitals dict.
print('-' * 10)
print("France has: ", capitals[countries['France']])
print("Germany has: ", capitals[countries['Germany']])

# prints every countries abbrevation.
print('-' * 10)
for country, abbrev in list(countries.items()):
    print(f"{country} is abbravated as {abbrev}")

# print every capital of a country.
print('-' * 10)
for abbrev, capital in list(capitals.items()):
    print(f"{abbrev} has the capital {capital}")

# Now do both at the same time.
print('-' * 10)
for country, abbrev in list(countries.items()):
    print(f"{country} is abbravated as {abbrev}")
    print(f"and it's capital city is {capitals[abbrev]}")

print('-' * 10)
# Get an abbrevation of a country not listed

country = countries.get('Belgium')

if not country:
    print("Belgium is not a worthy country!")

# Get a capital with a default value
capital = capitals.get('Bel', 'NOT worthy')
print(f"The capital for that country 'Bel' is:' {capital}")
