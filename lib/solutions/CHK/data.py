# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
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
    "G" : {
        "price": 20,
        "offer": None
    },
    "H" : {
        "price": 10,
        "offer": "5 for 45, 10 for 80"
    },
    "I" : {
        "price": 35,
        "offer": None
    },
    "J" : {
        "price": 60,
        "offer": None
    },
    "K" : {
        "price": 70,
        "offer": "2 for 120"
    },
    "L" : {
        "price": 90,
        "offer": None
    },
    "M" : {
        "price": 15,
        "offer": None
    },
    "N" : {
        "price": 40,
        "offer": "3 for 1.M"
    },
    "O" : {
        "price": 10,
        "offer": None
    },
    "P" : {
        "price": 50,
        "offer": "5 for 200"
    },
    "Q" : {
        "price": 30,
        "offer": "3 for 80"
    },
    "R" : {
        "price": 50,
        "offer": "3 for 1.Q"
    },
    "S" : {
        "price": 20,
        "offer": "Group"
    },
    "T" : {
        "price": 20,
        "offer": "Group"
    },
    "U" : {
        "price": 40,
        "offer": "4 for 120"
    },
    "V" : {
        "price": 50,
        "offer": "2 for 90, 3 for 130"
    },
    "W" : {
        "price": 20,
        "offer": None
    },
    "X" : {
        "price": 17,
        "offer": "Group"
    },
    "Y" : {
        "price": 20,
        "offer": "Group"
    },
    "Z" : {
        "price": 21,
        "offer": "Group"
    },
}


PRIORITY = ['E', 'N', 'R']

GROUP_OFFER = ['Z', 'Y', 'T', 'S', 'X'] # price desc order