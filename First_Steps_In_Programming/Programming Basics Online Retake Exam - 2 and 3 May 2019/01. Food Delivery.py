chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
chicken_count = int(input())
fish_count = int(input())
vegetarian_count = int(input())
total_order = chicken_menu * chicken_count + fish_menu * fish_count + vegetarian_menu * vegetarian_count
dessert = 0.20 * total_order
delivery_cost = 2.50
print(f'Total: {total_order + dessert + delivery_cost:.2f}')