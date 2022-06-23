

from xml.etree.ElementPath import prepare_descendant


def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food_item):
    snacks = person["favourites"]["snacks"]
    food_item_there = False
    for snack in snacks:
        if snack == food_item:
            food_item_there = True   
    return food_item_there