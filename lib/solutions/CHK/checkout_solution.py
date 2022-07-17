from .data import PRICE_TABLE, PRIORITY

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
                    "num_of_items": num_of_items,
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

def calculate_deductions(items_mapping, sku):
    """Calculate deductions and remove items from quantity mapping"""
    sku_data = PRICE_TABLE[sku]

    if sku_data['offer']:
        offers = calculate_offers(sku_data['offer'])

        if offers['deduction']:
            sku_deductions = items_mapping[sku] // int(offers['deduction']['num_of_items'])
            total_sku_deductions = offers['deduction']['quantity'] * sku_deductions

            try:
                if total_sku_deductions < items_mapping[offers['deduction']['chosen_sku']]:
                    items_mapping[offers['deduction']['chosen_sku']] = items_mapping[offers['deduction']['chosen_sku']] - total_sku_deductions
                else:
                    items_mapping[offers['deduction']['chosen_sku']] = 0
            except KeyError:
                pass

        total = items_mapping[sku] * PRICE_TABLE[sku]['price']
        del items_mapping[sku]
        return total, items_mapping

def get_total_price_from_offers(total_quantity, offers, normal_price):
    """Calculate total price from available"""
    total_price_of_sku = 0
    remaining_quantity = total_quantity
    for num_of_items, offer_price in sorted(offers.items(), reverse=True):
        available_offers = remaining_quantity // num_of_items # find how many times the offer applies
        remaining_quantity = remaining_quantity % num_of_items # find how many items are left that have a normal price
        total_price_of_sku += available_offers * offer_price
    if remaining_quantity > 0:
        total_price_of_sku += remaining_quantity * normal_price

    return total_price_of_sku

def checkout(skus):
    is_sku_valid = check_validity_of_skus(skus)
    if not is_sku_valid:
        return is_sku_valid

    total_price = 0
    items_mapping = create_item_quantity_mapping(skus)
    for priority in PRIORITY:
        try:
            items_mapping[priority]
            total_price, items_mapping = calculate_deductions(items_mapping, priority)
            print(total_price, items_mapping)
        except KeyError:
            pass

    for sku, quantity in items_mapping.items():
        try:
            sku_data = PRICE_TABLE[sku]

            if sku_data['offer']:
                offers = calculate_offers(sku_data['offer'])
                total_price_of_sku = get_total_price_from_offers(quantity, offers, sku_data['price'])
            else:
                total_price_of_sku = quantity * sku_data['price']
        except KeyError:
            pass

        total_price += total_price_of_sku

    return total_price

