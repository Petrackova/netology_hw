from task1 import cook_book


def get_ingredients(dishes, person_count):
    dish_list = []
    ingr = {}
    if person_count == 0:
        print('Отсутствие людей в кафе\n')
    for name in dishes:
        if name not in cook_book.keys():
            print(f'Блюда {name} нет в меню')
            break
        for key, value in cook_book.items():
            if name == key:
                for i in value:
                    dish_list.append(i['ingredient_name'])
                    if len(set(dish_list)) == len(dish_list):
                        ingr[i['ingredient_name']] = {'quantity': int(i['quantity']) * person_count,
                                                              'measure': i['measure']}
                    else:
                        difference = len(dish_list) - len(set(dish_list))
                        ingr[i['ingredient_name']] = {'quantity': int(i['quantity']) * person_count * (difference + 1),
                                                              'measure': i['measure']}
    for key, value in ingr.items():
        print(key, value)


if __name__ == '__main__':
    get_ingredients(['Фахитос'], 5)
    print()
    get_ingredients(['Омлет'], 6)
    print()
    get_ingredients(['Борщ'], 2)
    print()
    get_ingredients(['Запеченный картофель'], 0)
    print()
    get_ingredients(['Утка по-пекински', 'Омлет'], 2)
