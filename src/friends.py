

from unittest import result
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

def lend_money(lender, lendee, cash):
    lender["monies"] -= cash
    lendee["monies"] += cash

def all_favourite_foods(scoby_gang):
    result = list()
    for person in scoby_gang:
        for snack in person["favourites"]["snacks"]:
            result.append(snack)
    return result

def find_no_friends(scoby_gang):
    no_mates = []
    for person in scoby_gang:
        if len(person["friends"]) == 0:
            no_mates.append(person)
    return no_mates

def unique_favourite_tv_shows(scoby_gang):
    result = []
    for person in scoby_gang:
        if person["favourites"]["tv_show"] not in result:
            result.append(person["favourites"]["tv_show"])
    return result
