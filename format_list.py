def format_list(list_to_format):
    string = ''
    for i in range(len(list_to_format)):
        if i == len(list_to_format) - 1:
            string += ' and {}.'.format(list_to_format[i])
        elif i == len(list_to_format) -2:
            string += '{}'.format(list_to_format[i])
        else:
            string +=  list_to_format[i]+ ', '

    return string

bacon = ['apples', 'bananas', 'tofu', 'cats']
print(format_list(bacon))
