yearly_subscription = int(input())
sneakers = 0.60 * yearly_subscription
equip = 0.80 * sneakers
ball = 0.25 * equip
accessories = 0.20 * ball
total = yearly_subscription + sneakers + equip + ball + accessories
print(f'{total:.2f}')