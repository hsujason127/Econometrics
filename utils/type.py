from re import A


class Investor: 
    # Constructor
    def __init__(self, institute, date, over_amount):
        self.institute_ = institute
        self.date_ = int(date)
        self.over_amount_ = int(over_amount)
    
    # # Member Functions
    # def GetOverAmount(self):
    #     return self.over_amount_
    
    # def GetInstitute(self):
    #     return self.institute_

class Rate:
    # Constructor
    def __init__(self, type, rate, date):
        self.type_ = type
        self.rate_ = rate
        self.date_ = date

    # # Member Functions
    # def GetType(self):
    #     return self.type_
    
    # def GetRate(self):
    #     return self.rate_




        