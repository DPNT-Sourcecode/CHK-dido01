# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+

PRICE_TABLE = {
    "A" : {
        "price": 50,
        "offer": "3 for 130, 5 for 200"
    },
    "B" : {
        "price": 30,
        "offer": "2 for 45"
    },
    "C" : {
        "price": 20,
        "offer": None
    },
    "D" : {
        "price": 15,
        "offer": None
    },
    "E" : {
        "price": 40,
        "offer": "2 for 1.B"
    },
    "F" : {
        "price": 10,
        "offer": "3 for 20"
    },
}

PRIORITY = ['E']