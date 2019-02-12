from roundcent import to_nearest_even

class Job:
    
    def __init__(self, extra_margin = False):
    
        self.extra_margin = extra_margin
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):

        self.total = 0
        for item in self.items:

            job_cost = item.cost * (0.16 if self.extra_margin else 0.11)
            self.total += (item.price + job_cost)

    def __str__(self):

        r_str = ""

        for item in self.items:
            r_str += str(item) + "\n"
        
        return r_str + "total: $%s" % format(to_nearest_even(self.total), '.2f')