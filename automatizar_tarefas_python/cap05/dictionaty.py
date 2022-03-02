def totalBrought(guest, item):
    total = 0
    for k, v in guest.items():
        total += v.get(item, 0)
    return total

allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
    }

print('Number of things being brought: ')
print('Apples: {}.'.format(totalBrought(allGuests, 'apples')))
print('Cups: {}'.format(totalBrought(allGuests, 'cups')))
print('Cakes: {}'.format(totalBrought(allGuests, 'cakes')))
print('Ham sandwiches: {}'.format(totalBrought(allGuests, 'ham sandwiches')))
print('Apple Pies: {}'.format(totalBrought(allGuests, 'apple pies')))
