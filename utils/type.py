class Investor: 
    # Constructor
    def __init__(self, institute, date, over_amount):
        self.institute_ = institute
        self.date_ = date
        self.over_amount_ = int(over_amount)
    
    # Member Functions
    def GetOverAmount(self):
        return self.over_amount_
    
    def GetInstitute(self):
        return self.institute_

class Rate:
    # Constructor
    def __init__(self, type, rate, date):
        self.type_ = type
        self.rate_ = rate
        self.date_ = date

    # Member Functions

a = Investor("自營商", "20220428", "100")
b = Investor("外資", "20220428", "200")

x = [a, b]

print(x[0].GetOverAmount(), x[1].GetInstitute())




        