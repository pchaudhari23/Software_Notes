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
        print(f'Unable to parse {line}')
print(parsed_config)

#-----------------------------------------------------------------------
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
    
str_to_bool("y")
