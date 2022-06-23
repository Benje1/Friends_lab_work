

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

# find way to add to list within dictionanry
# get the length of the friends list
def add_friend(person, friend):
    person["friends"].append(friend)
    return len(person["friends"])

def remove_friend(person, friend):
    person["friends"].remove(friend)
    return len(person["friends"])

def total_money(scoby_gang):
    total_money = 0
    for person in scoby_gang:
        total_money += person["monies"]
    return total_money

