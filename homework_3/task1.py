from pprint import pprint

cook_book = {}


def get_cook_book():
    with open('recipes.txt', encoding='UTF-8') as f:
        for line in f:
            name = line.strip()
            cook_book[name] = []
            f.readline()
            i = 0
            while i == 0:
                ingr = f.readline()
                if len(ingr) > 1:
                    ingr = ingr.strip()
                    ingr = ingr.split(' | ')
                    in_cook_book = {'ingredient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}
                    cook_book[name].append(in_cook_book)
                else:
                    i += 1
    pprint(cook_book)

get_cook_book()