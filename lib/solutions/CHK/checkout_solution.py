from .data import PRICE_TABLE

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

    total_price = 0
    for sku, quantity in items_mapping.items():
        try:
            sku_data = PRICE_TABLE[sku]
            if sku_data['offer']:
                num_of_items, offer_price = sku_data['offer'].split('for')
                num_of_items = int(num_of_items)
                offer_price = int(offer_price)
                available_offers = quantity // num_of_items # find how many times the offer applies
                remaining_non_offer_skus = quantity % num_of_items # find how many items are left that have a normal price
                total_price_of_sku = available_offers * offer_price + remaining_non_offer_skus * sku_data['price']
            else:
                total_price_of_sku = quantity * sku_data['price']
        except KeyError:
            # pass as we dont have clear instrucitons of what to do with unknown skus
            pass
        total_price += total_price_of_sku

    return total_price

