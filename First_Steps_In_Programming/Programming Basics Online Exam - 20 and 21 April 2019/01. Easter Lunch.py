bread = 3.20
carton_eggs = 4.35
carton = 12
cookies = 5.40
egg_paint = 0.15
bread_count = int(input())
carton_eggs_count = int(input())
kg_cookies = int(input())
cost = bread * bread_count + carton_eggs * carton_eggs_count + cookies * kg_cookies + (carton_eggs_count * carton * egg_paint)
print(f'{cost:.2f}')
