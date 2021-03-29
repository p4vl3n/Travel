import re

planets = {'attacked': [], 'destroyed': []}
lines = int(input())
for line in range(lines):
    encrypted_message = input()
    star_pattern = r"[starSTAR]"
    key = len(re.findall(star_pattern, encrypted_message))
    decyphered_message = ""
    for el in encrypted_message:
        temp_key = ord(el)
        new_el = chr(temp_key - key)
        decyphered_message += new_el
    planet_pattern = r"(?<=@)(?P<planet>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*(!(?P<attack_destruct>A|D)!)[^@!:>-]*(->(?P<soldiers>\d+))"
    planet = [obj.groupdict() for obj in re.finditer(planet_pattern, decyphered_message)]
    if planet:    
        if planet[0]['attack_destruct'] == "A":
            planets['attacked'].append(planet[0]['planet'])
        else:
            planets['destroyed'].append(planet[0]['planet'])
for planet in planets.values():
    planet.sort()
print(f"Attacked planets: {len(planets['attacked'])}")
if planets['attacked']:
    for planet in planets['attacked']:
        print(f"-> {planet}")
print(f"Destroyed planets: {len(planets['destroyed'])}")
if planets['destroyed']:
    for planet in planets['destroyed']:
        print(f"-> {planet}")