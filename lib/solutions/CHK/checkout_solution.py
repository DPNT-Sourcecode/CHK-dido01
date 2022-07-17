

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Question where is the sku -> price -> offer mapping data come from are we supposed to create a dummy dictionary?
    if not skus:
        return -1

    if not skus.isupper():
        # check if contains only uppercase letters
        return -1

    if not skus.isalpha():
        # check if it contains any special chars or numbers
        return -1

    return skus
