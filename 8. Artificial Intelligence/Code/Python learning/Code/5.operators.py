first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

#-------------------------------------------------------------------

first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print(abs(distance_km))