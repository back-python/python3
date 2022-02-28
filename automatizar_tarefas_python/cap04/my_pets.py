my_cats = ['Mate', 'Make', 'Lua', 'Dembe']

cat_name = input('Enter a cat name: ')

if cat_name in my_cats:
    print('{} is my cat!'. format(cat_name))
else:
    print('I do not have a cat named {}!'. format(cat_name))
