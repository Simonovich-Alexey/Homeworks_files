def read_file():
    read_file_list = []
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        for i in file:
            read_file_list.append(i.strip())

    cook_book = {}
    count = 0
    for index in range(len(read_file_list)):
        if read_file_list[index] != '' and index != len(read_file_list) - 1:
            continue
        else:
            if read_file_list[index] == '':
                recipe_slice = read_file_list[count:index]
                count = index + 1
            else:
                recipe_slice = read_file_list[count:]

        name_recipe = recipe_slice[0]
        ingredients = recipe_slice[2:]
        recipe = []
        for j in ingredients:
            ingredient = j.split(' | ')
            recipe.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})

        cook_book[name_recipe] = recipe
    return cook_book


def get_shop_list_by_dishes(dishes, person):
    shop_list = {}
    for key, values in read_file().items():
        if key in dishes:
            for ingredient_one in values:
                name_ingredient = ingredient_one.setdefault('ingredient_name')
                measure = ingredient_one.setdefault('measure')
                product_quantity = ingredient_one.setdefault('quantity') * person
                if shop_list.get(name_ingredient):
                    sum_numb = shop_list.setdefault(name_ingredient).setdefault('quantity') + product_quantity
                    shop_list[name_ingredient] = {'measure': measure,
                                                  'quantity': sum_numb}
                else:
                    shop_list[name_ingredient] = {'measure': measure,
                                                  'quantity': product_quantity}
    return shop_list


print(read_file())
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


# def read_file_in_files(name_file):
#     if isinstance(name_file, list):
#         file_list = []
#         for file_name in name_file:
#             with open("files/" + file_name, "r", encoding="utf-8") as text_file:
#                 len_file = 0
#                 text = []
#                 for t in text_file:
#                     len_file += 1
#                     text.append(t.strip())
#                 file_dict = {'name': file_name, 'len': len_file, 'text': text}
#                 file_list.append(file_dict)
#         return file_list
#     else:
#         file_list = []
#         with open("files/" + name_file, "r", encoding="utf-8") as text_file:
#             len_file = 0
#             text = []
#             for t in text_file:
#                 len_file += 1
#                 text.append(t.strip())
#             file_dict = {'name': name_file, 'len': len_file, 'text': text}
#             file_list.append(file_dict)
#         return file_list


def read_file_and_sort(*name_file):
    file_list = []
    for file_name in name_file:
        with open("files/" + file_name, "r", encoding="utf-8") as text_file:
            text = []
            for t in text_file:
                text.append(t.strip())
            file_dict = {'name': file_name, 'len': len(text), 'text': text}
            file_list.append(file_dict)
    return sorted(file_list, key=lambda x: x['len'])


def write_file(file_read):
    with open('files/4.txt', 'w', encoding='utf-8') as file:
        for value in file_read:
            text_change = '\n'.join(value['text'])
            added = f"{value['name']}\n{value['len']}\n{text_change}\n"
            file.write(added)


write_file(read_file_and_sort('1.txt', '2.txt', '3.txt'))
