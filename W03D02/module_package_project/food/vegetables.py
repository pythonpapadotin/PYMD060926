# This is a vegetable module in food package

vegetable_database = ['brinjal', 'ladyfinger', 'carrot', 'onion']


def is_vegetable_present(veg_name):
    if veg_name in vegetable_database:
        return True
    return False
