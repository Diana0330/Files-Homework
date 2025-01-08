# Problem 1
import os
def read_cook_book():
    cook_book = {}
    with open('recipes/recipes.txt', encoding='utf-8') as text_file:
        data = text_file.read()
        new_line = data.split('\n')


        i = 0 # current index where we start the recipe of one dish, starts with name omelette
        counter = len(new_line) # number of lines in a file
        while i < counter:
            dish_name = new_line[i]
            quantity = new_line[i+1]
            ingredients_list = []

            for k in range(0, int(quantity)):
                ingredients = new_line[i+2+k].split(' | ')
                ingredients_dict = {
                    'ingredients_name': ingredients[0],
                    'quantity': int(ingredients[1]),
                    'measure': ingredients[2]}
                ingredients_list.append(ingredients_dict)
                #print(ingredients_dict)
            cook_book[dish_name] = ingredients_list
            i = i + 2 + int(quantity) + 1

    return cook_book


result = read_cook_book()
print(result)

# Problem 2
def get_shop_list_by_dishes(dishes, person_count):
    dishes_list = {}
    menu = read_cook_book()
    print(menu)
    print(dishes)
    for line in dishes: # line is a key in a dictionary menu
        if line in menu:
            ingredients_list = menu[line]
            #print(ingredients_list)
            for ingredient in ingredients_list:
                ingredients_name = ingredient['ingredients_name']
                #print(ingredient)
                quantity = ingredient['quantity'] * person_count
                if ingredients_name not in dishes_list:
                    dishes_list[ingredients_name] = {'measure': ingredient['measure'], 'quantity': quantity}
                else:
                    dishes_list[ingredients_name]['quantity'] += quantity
    return dishes_list
#result_two = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
result_two = get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель'], 2)
print(result_two)

# Problem 3
def open_file(path):
    with open(path, encoding ='utf-8') as text_file:
        data = text_file.read()
        new_line = data.strip().split('\n')
        return new_line


def print_result(list_with_files):

    final_result = ''
    for line in list_with_files:
        final_result += f'{line[0]}\n'
        final_result += f'{line[2]}\n'
        final_result += f'{'\n'.join(line[1])}\n'
    return final_result


directory = 'Files for Problem 3'
file_one = '1.txt'
file_two = '2.txt'
file_three = '3.txt'
file_one_read = open_file(directory + '/' + file_one)
file_two_read = open_file(directory + '/' + file_two)
file_three_read = open_file(directory + '/' + file_three)
list_of_items = [(file_one, file_one_read, len(file_one_read)),
    (file_two, file_two_read, len(file_two_read)),
    (file_three, file_three_read, len(file_three_read))] # filing list with data
list_sorted = sorted(list_of_items, key=lambda x: x[2])

#print(file_one_read)
#print(file_two_read)
#print(file_three_read)
#print(list_sorted)
output = print_result(list_sorted)
print(output)

