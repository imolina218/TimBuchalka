import shelve

# blt = ["Bacon", "Lettuce", "Tomato", "Bread"]
# beans_on_toast = ["Beans", "Bread"]
# scrambled_eggs = ["eggs", "butter", "Milk"]
soup = ["tin of soup"]
# pasta = ["Pasta", "Cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["Beans and toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("Butter")
    # recipes["pasta"].append("tomato")
    # temp_list = recipes["blt"]
    # temp_list.append("Butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    #
    # recipes["soup"].append("croutons")
    # Don't do it:
    # recipes["soup"] = soup
    # recipes.sync()
    # soup.append("Cream")

    for snack in recipes:
        print(snack, recipes[snack])

