from data import PRICE_TABLE

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    # Question where is the sku -> price -> offer mapping data come from are we supposed to create a dummy dictionary?
    if not skus:
        # empty skus are allowed
        return 0

    if not skus.isupper():
        # check if contains only uppercase letters
        return -1

    if not skus.isalpha():
        # check if it contains any special chars or numbers
        return -1
    
    items_mapping = {}
    for char in skus:
        try:
            items_mapping[char] += 1
        except KeyError:
            # if item not already in the mapping dictionary initialize it to 1
            items_mapping[char] = 1
    
    print(items_mapping)

    return 10


checkout("AAA")

