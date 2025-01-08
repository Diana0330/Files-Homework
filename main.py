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

with open('Files for Problem 3/1.txt', encoding = 'utf-8') as text_file:
    data = text_file.read()
    new_line = data.split('\n')
    print(data)
with open('Files for Problem 3/2.txt', encoding='utf-8') as text_file_two:
    data_two = text_file_two.read()
    new_line = data.split('\n')
    print(data_two)
with open('Files for Problem 3/3.txt', encoding='utf-8') as text_file_three:
    data_three = text_file_three.read()
    new_line = data.split('\n')
    print(data_three)

