from data import PRICE_TABLE

# noinspection PyUnusedLocal
# skus = unicode string

def check_validity_of_skus(skus):
    if not skus:
        # empty skus are allowed
        return 0

    if not skus.isupper():
        # check if contains only uppercase letters
        return -1

    if not skus.isalpha():
        # check if it contains any special chars or numbers
        return -1

    return True


def create_item_quantity_mapping(skus):
    """Returns a dictionary mapping the skus with the corresponding quantity"""
    items_mapping = {}
    for char in skus:
        try:
            items_mapping[char] += 1
        except KeyError:
            # if item not already in the mapping dictionary initialize it to 1
            items_mapping[char] = 1

    return items_mapping


def calculate_offers(sku_data):
    offers = {}
    available_offers = sku_data.split(',')
    for available_offer in available_offers:
        num_of_items, offer_price = available_offer.split('for')

        try:
            quantity, chosen_sku = offer_price.split('.')
            if quantity and chosen_sku:
                offers['deduction'] = {
                    "quantity": int(quantity),
                    "chosen_sku": chosen_sku
                }
                continue
        except ValueError:
            pass

        num_of_items = int(num_of_items)
        offer_price = int(offer_price)
        offers[num_of_items] = offer_price

    return offers

def get_total_price_from_offers(offers, price):
for offer in sorted(offers.items(), reverse=True):
                    print(offer)

def checkout(skus):
    is_sku_valid = check_validity_of_skus(skus)
    if not is_sku_valid:
        return is_sku_valid

    items_mapping = create_item_quantity_mapping(skus)

    total_price = 0
    for sku, quantity in items_mapping.items():
        try:
            sku_data = PRICE_TABLE[sku]
            print(PRICE_TABLE[sku])
            if sku_data['offer']:
                offers = calculate_offers(sku_data['offer'])
                for offer in sorted(offers.items(), reverse=True):
                    print(offer)
                # available_offers = quantity // num_of_items # find how many times the offer applies
                # remaining_non_offer_skus = quantity % num_of_items # find how many items are left that have a normal price
                # total_price_of_sku = available_offers * offer_price + remaining_non_offer_skus * sku_data['price']
        #     else:
        #         total_price_of_sku = quantity * sku_data['price']
        except KeyError:
            # pass as we dont have clear instrucitons of what to do with unknown skus
            pass
        # total_price += total_price_of_sku

    return total_price

checkout("AAA")