class BankOfBaroda:
    BankName  = 'Bank of Baroda'
    customers =  15000
    Branch    = 'Madanapalli'
    IFSC      = 'BOBNO123498'
    Address   = '10-387-7 opp RTC Bus Stand  Madanapalli'
    RateOfIntrest = 7.0

    
    def __init__(self,name,Aadhar,phn,pan,age,balance,pin):
        self.name    = name
        self.Aadhar  = Aadhar
        self.phn     = phn
        self.pan     = pan
        self.age     = age
        self.balance = balance
        self.pin     = pin

    def CheckBalance(self):
        if self.pin == self.Takepin():
            print(f'Available balance is {self.balance}')
        else:
            print('Invalid Pin')


    def WithdrawAmount(self):
        if self.pin==self.Takepin():
            Amount = int(input('Enter the Amount : '))
            if Amount <= self.balance:
                self.balance -= Amount
                print(f'From Your Account {Amount} is debited is Successfully... \n Available balance is {self.balance}')
            else:
                print('Insufficient Amount')
        else:
            print('Invalid Pin')


    def DepositeAmount(self):
        if self.pin==self.Takepin():
            Amount = int(input('Enter the Amount : '))
            if Amount <= self.balance:
                self.balance += Amount
                print(f'From Your Account {Amount} is Credited is Successfully... \n Available balance is {self.balance}')
            else:
                print('Insufficient Amount')
        else:
            print('Invalid Pin')


    @staticmethod
    def Takepin():
        password = int(input('Enter your Pin :'))
        return password



    @classmethod
    def ChangeOfRateOfIntrest(cls):
        new_roi = float(input('Enter the New Rate of Intrest  : '))
        cls.RateOfIntrest = new_roi

Applicant1 = BankOfBaroda('Shaik',236759679098,6300299581,'SAB12486',22,25000,1435)
Applicant1.DepositeAmount()
        
    
