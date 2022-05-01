class Investor: 
    # Constructor
    def __init__(self, institute, date, over_amount):
        self.institute_ = institute
        self.date_ = int(date)
        self.over_amount_ = int(over_amount)
    

class Rate:
    # Constructor
    def __init__(self, name, date, rate):
        self.name_ = name
        self.date_ = int(date)
        self.rate_ = float(rate)


class Index:
    # Constructor
    def __init__(self, name, date, price):
        self.name_ = name
        self.date_ = int(date)
        self.price_ = float(price)




        