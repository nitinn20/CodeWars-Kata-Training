def get_drink_by_profession(param):
    drink={
        "jabroni":"Patron Tequila",
        "school counselor":"Anything with Alcohol",
        "programmer":"Hipster Craft Beer",
        "bike gang member":"Moonshine",
        "politician":"Your tax dollars",
        "rapper":"Cristal"
    }
    if param.lower() in drink:
        return drink[param.lower()]
    else:
        return 'Beer'