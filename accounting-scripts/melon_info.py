"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, new_dictionary



def print_melon(name, price, seedless,flesh_color, rind_color, average_weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name} \n Price: {price} \n seedless: {seedless} '
    f'\n flesh_color: {flesh_color} \n rind_color: {rind_color}'
    f'\n average_weight: {average_weight}')
    


for melon_name in new_dictionary:
    print_melon(melon_name, new_dictionary[melon_name]['price'],
     new_dictionary[melon_name]['seedlessness'], new_dictionary[melon_name]['flesh_color'], 
     new_dictionary[melon_name]['rind_color'], new_dictionary[melon_name]['average_weight'])

