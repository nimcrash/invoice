from roundcent import to_nearest

class Item:

    def __init__(self, name, cost, exempt = False):

        self.name = name
        self.cost = cost
        self.exempt = exempt
        #self.tax = 0 if exempt else cost * 0.07
        self.price = cost * (1 if exempt else 1.07)

    def __str__(self):

        return "%s: $%s" % (self.name, format(to_nearest(self.price), '.2f'))