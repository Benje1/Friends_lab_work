

def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food_item):
    for snack in person:
        if person["favourites"]["snacks"] == food_item:
            return True