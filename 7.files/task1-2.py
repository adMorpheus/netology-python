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
        ingredients_list.append(cook_book[dish])
    ingredients_map = dict()
    for ingredient_name, quantity, measure in ingredients_list:
        if ingredients_map[ingredient_name]:


# print(create_structure())
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
