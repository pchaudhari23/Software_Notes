# =============================================================================
# PYTHON BEGINNER PROGRAMS
# A consolidated collection of beginner Python exercises and concepts
# =============================================================================


# =============================================================================
# SECTION 1: INTRODUCTION & BASICS
# - Printing output, constants, and taking user input
# =============================================================================

print("Hello world!")

# Defining a constant (by convention, constants are written in ALL_CAPS)
PI = 3.14
print(PI)

# Taking two numbers as input from the user and printing their sum
first_number = int(input('Type the first number: '))
second_number = int(input('Type the second number: '))
print("The sum is: ", first_number + second_number)


# =============================================================================
# SECTION 2: DATES, VARIABLES & TYPE CONVERSION
# - Working with the datetime module, variables, and converting between types
# =============================================================================

from datetime import date

# Print today's date
print(date.today())

# Convert Parsec to lightyears (1 Parsec = 3.26 lightyears)
parsecs = 14
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

# Collecting input from the user for unit conversion
parsecs_input = input("Input number of parsecs: ")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")


# =============================================================================
# SECTION 3: BOOLEANS & CONDITIONALS
# - if/else statements and logical operators (and, or, not)
# =============================================================================

# Basic if/else — check object size
object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')

# Using the AND operator — both conditions must be True
object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')


# =============================================================================
# SECTION 4: STRINGS
# - String manipulation, splitting, searching, and formatting
# =============================================================================

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. \
There are several interesting facts about the Moon and how it affects life here on Earth. \
On average, the Moon moves 4cm away from the Earth every year. \
This yearly drift is not significant enough to cause immediate effects on Earth. \
The highest daylight temperature of the Moon is 127 C."""

# Split the text into a list of sentences
sentences = text.split('. ')
print(sentences)

# Search for a specific keyword in each sentence
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)

# String formatting using .format()
name = 'Ganymede'
planet = 'Mars'
gravity = 1.43

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))


# =============================================================================
# SECTION 5: OPERATORS & ARITHMETIC
# - Mathematical operators and working with large numbers
# =============================================================================

# Calculate the distance between two planets (in km and miles)
first_planet = 149597870    # Earth's distance from the Sun in km
second_planet = 778547200   # Jupiter's distance from the Sun in km

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

# User-input version: calculate distance between any two planets
first_planet_input = input('Enter the distance from the sun for the first planet in km: ')
second_planet_input = input('Enter the distance from the sun for the second planet in km: ')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print(abs(distance_km))  # abs() ensures a positive result regardless of order


# =============================================================================
# SECTION 6: LISTS
# - Creating lists, appending, indexing, and slicing
# =============================================================================

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)
print("There are", len(planets), "planets")

# Append an item to the list
planets.append("Pluto")
print("Actually, there are", len(planets), "planets")
print(planets[-1], "is the last planet")  # -1 index accesses the last element

# Ask the user for a planet and show planets closer/further from the sun
user_planet = input("Please enter the name of the planet (with a capital letter to start): ")
planet_index = planets.index(user_planet)

print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])               # Slice from start to planet

print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])            # Slice from planet to end


# =============================================================================
# SECTION 7: LOOPS
# - while loops and for loops
# =============================================================================

# while loop: keep collecting planet names until the user types 'done'
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Enter a new planet, or 'done' if done: ")

print(planets)

# for loop: iterate over the collected planets and print each one
for planet in planets:
    print(planet)


# =============================================================================
# SECTION 8: DICTIONARIES
# - Key-value pairs, nested dictionaries, and iterating over dictionaries
# =============================================================================

# Basic dictionary
planet = {
    'name': 'Mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

# Adding a nested dictionary as a value
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

# Dictionary of all planets and their moon counts
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Calculate the average number of moons per planet
moons = planet_moons.values()
total_planets = len(planet_moons.keys())
print(moons)
print(total_planets)

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets
print(f'Each planet has an average of {average} moons')


# =============================================================================
# SECTION 9: FUNCTIONS
# - Defining functions, positional arguments, and keyword (**kwargs) arguments
# =============================================================================

# Function with fixed positional arguments
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)

generate_report(80, 70, 75)

# Function with variable keyword arguments (**kwargs)
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)


# =============================================================================
# SECTION 10: ERROR HANDLING
# - try/except blocks and raising custom errors with ValueError
# =============================================================================

# Parsing a config file — handle lines that don't follow the key=value format
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        # Lines without '=' (like comments and the end marker) are skipped
        print(f'Unable to parse: {line}')

print(parsed_config)

# Function that raises a ValueError for invalid input
true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')

str_to_bool("y")  # Returns True


# =============================================================================
# SECTION 11: MISCELLANEOUS / SCRATCH
# - Simple arithmetic scratch work
# =============================================================================

a = 4
b = 9
c = a * b
print(c)  # Output: 36