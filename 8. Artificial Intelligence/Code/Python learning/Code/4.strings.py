text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#---------------------------------------------------
sentences = text.split('. ')
print(sentences)
# #---------------------------------------------------
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)
#---------------------------------------------------


name: 'Ganymede'
planet: 'Mars'
gravity: 1.43

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))

