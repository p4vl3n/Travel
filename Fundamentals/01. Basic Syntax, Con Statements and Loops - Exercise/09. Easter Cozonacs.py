budget = float(input())
flour_price = float(input())
egg_pack = 0.75 * flour_price
litre_milk = 1.25 * flour_price
quarter_milk = litre_milk / 4
bread_cost = flour_price + egg_pack + quarter_milk
bread_count = 0
colored_eggs = 0

while budget > bread_cost:

    budget -= bread_cost
    bread_count += 1
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2
print(f"You made {bread_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

