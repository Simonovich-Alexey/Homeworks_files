read_file = []
with open('recipes.txt', 'r', encoding='utf-8') as file:
    for i in file:
        read_file.append(i.strip())

count = 0
recipe_list = []
print(read_file)
for index in range(len(read_file)):
    if read_file[index] == '':
        recipe_list.append(read_file[count:index])
        print(read_file[count:index])
        count = index + 1

    elif index == len(read_file) - 1:
        recipe_list.append(read_file[count:])

print(recipe_list)

cook_book = {}


for i in recipe_list:
    print(i)
    name_recipe = i[0]
    ingredients = i[2:]
    cook_books = []
    print(name_recipe)
    for k in ingredients:
        ingredient = k.split(' | ')
        ingredients_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
        print(ingredients_dict)
        cook_books.append(ingredients_dict)
    cook_book[name_recipe] = cook_books
    print(cook_book)

print(cook_book)
# d = recipe_list[0][2]
# d = d.split(' | ')
#
# dict_test = {}
#
# dict_test['ingredient_name'] = d[0]
# dict_test['quantity'] = d[1]
# dict_test['measure'] = d[2]
# # print(dict_test)
#
# rec_dick = {}
# for u in recipe_list:
#     rec_dick[u[0]] = u[1:]
