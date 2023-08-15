SRC_FILE_PATH = 'recipes.txt'


def create_structure():
    cook_book = {}
    with open(SRC_FILE_PATH, 'rt', encoding='utf-8') as src_file:
        while True:
            feed_name = src_file.readline().strip()
            ingredients_count = int(src_file.readline())
            ingredients = list()
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = src_file.readline().split('|')
                ingredients.append({'ingredient_name': ingredient_name.strip(),
                                    'quantity': int(quantity),
                                    'measure': measure.strip()})
            cook_book[feed_name] = ingredients
            if src_file.readline():
                continue
            break
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    result_dict = dict()
    cook_book = create_structure()
    ingredients_list = list()
    for dish in dishes:
        ingredients_list+=cook_book[dish]
    ingredients_map = dict()
    # ingredients_list = ingredients_list[0]
    for ingredient in ingredients_list:
        ingredient_name = ingredient['ingredient_name']
        quantity = ingredient['quantity']
        measure = ingredient['measure']
        if ingredient_name in ingredients_map.keys():
            ingredients_map[ingredient_name][quantity] += quantity*person_count
        else:
            ingredients_map[ingredient_name] = {'measure': measure, 'quantity': quantity*person_count}
    return ingredients_map

# print(create_structure())
# print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
