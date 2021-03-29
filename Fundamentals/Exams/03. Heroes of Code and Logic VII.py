class Hero:
    def __init__(self, hero_name, hit_points: int, mana_points: int):
        self.hero_name = hero_name
        self.hit_points = hit_points
        self.mana_points = mana_points

def define_action(cmnd, hrs):
    data = cmnd.split(" - ")
    action, hero_name = data[0], data[1]
    hero = [hero for hero in hrs if hero.hero_name == hero_name][0]
    if action == "CastSpell":
        mp_needed, spell_name = int(data[2]), data[3]
        return cast_spell(hero, mp_needed, spell_name)
    elif action == "TakeDamage":
        damage, attacker = int(data[2]), data[3]
        return take_damage(hero, damage, attacker, heroes)    
    elif action == "Recharge":
        amount = int(data[2])
        return recharge(hero, amount)
    elif action == "Heal":
        amount = int(data[2])
        return heal(hero, amount)
    

def cast_spell(hro, mp, spell):
    if mp <= hro.mana_points:
        hro.mana_points -= mp
        return f"{hro.hero_name} has successfully cast {spell} and now has {hro.mana_points} MP!"
    return f"{hro.hero_name} does not have enough MP to cast {spell}!"


def take_damage(hro, dmg, attckr, hrs):
    if dmg < hro.hit_points:
        hro.hit_points -= dmg
        return f"{hro.hero_name} was hit for {dmg} HP by {attckr} and now has {hro.hit_points} HP left!"
    hrs.remove(hro)
    return f"{hro.hero_name} has been killed by {attckr}!"
        

def recharge(hro, amnt):
    if hro.mana_points + amnt > 200:
        amnt = 200 - hro.mana_points
    hro.mana_points += amnt
    return f"{hro.hero_name} recharged for {amnt} MP!"


def heal(hro, amnt):
    if hro.hit_points + amnt > 100:
        amnt = 100 - hro.hit_points 
    hro.hit_points += amnt
    return f"{hro.hero_name} healed for {amnt} HP!"

heroes = []
n = int(input())
for _ in range(n):
    hero_name, hit_points, mana_points = input().split()
    hero = Hero(hero_name, int(hit_points), int(mana_points))
    heroes.append(hero)

command = input()
while not command == "End":
    outcome = define_action(command, heroes)
    print(outcome)
    command = input()

sorted_heroes = sorted(heroes, key= lambda hero: (-hero.hit_points, hero.hero_name))
for hero in sorted_heroes:
    print(f"{hero.hero_name}\nHP: {hero.hit_points}\nMP: {hero.mana_points}")