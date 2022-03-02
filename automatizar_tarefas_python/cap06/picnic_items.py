def printPicnic(picnic_items, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '='))
    for k, v in picnic_items.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width,'.'))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 30, 5)
