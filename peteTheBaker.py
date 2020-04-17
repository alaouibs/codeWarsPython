def cakes(recipe, available):
    number = []
    for key in recipe:
        if not key in available:
            return 0
        number.append(available[key]/recipe[key])
    return min(number)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available)