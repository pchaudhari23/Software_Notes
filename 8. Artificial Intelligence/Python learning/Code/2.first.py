
from datetime import date
print(date.today())

#-------------------------------------
# Convert Parsec to lightyears
# 1 Parsec = 3.26 lightyears

parsecs = 14
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

#-------------------------------------
# Collecting input

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")