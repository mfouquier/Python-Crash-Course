sandwich_orders = ['pastrami', 'cuban', 'rueben', 'pastrami', 'roast beef', 'turkey', 'pastrami']
finished_sandwiches = []

print('We are all out of Pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
