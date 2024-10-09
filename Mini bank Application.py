class Canara_bank():
    Bank_name = 'Canara bank'
    Branch_name = 'Banglore'
    Branch_Ifsc = 'CBI01234'
    Rate_of_intrest = 8
    def __init__(self,name,Gender,Aadhar,Mobile_number,Pin,Balance):
        self.name = name
        self.Gender = Gender
        self.Aadhar = Aadhar
        self.Mobile_number = Mobile_number
        self.Pin = Pin
        self.Balance = Balance
    @classmethod
    def Changing_of_rate_of_intrest(cls):
        new_Rate_of_intrest = float(input("Enter the new Rate of intrest: "));
        cls.Rate_of_intrest = new_Rate_of_intrest
    @staticmethod
    def pin():
        password = int(input("enter the pin: "))
        return password
    def Cecking_balance(self):        
        if self.pin() == pin:
            print(f'Available balance is {self.Balance}')
        else:
            print('Wrong pin')
    def Checking_balance(self):        
        if self.pin() == self.Pin:
            print(f'Available balance is {self.Balance}')
        else:
            print('Wrong pin')
    def Withdraw(self):        
        if self.pin()== self.Pin:
            Amount_withdraw  = int(input("Enter the withdraw amount :"))
            if Amount_withdraw <= self.Balance:
                self.Balance -= Amount_withdraw
                print(f'{Amount_withdraw} Amount is Sucessfully debited........! ')
                print(f'Available balance is {self.Balance}......!')
            else:
                print('Insufficent amount ....!')
            print(f'Available balance is {self.Balance}......!')
        else:
            print('Wrong pin')
    def Deposite(self):      
        if self.pin() == self.Pin:
            Amount_withdraw  = int(input("Enter the withdraw amount :"))            
            self.Balance += Amount_withdraw
            print(f'{Amount_withdraw} Amount is Sucessfully debited........! ')
            print(f'Available balance is {self.Balance}......!')            
            print(f'Available balance is {self.Balance}......!')
        else:
            print('Wrong pin')
Applicant1 = Canara_bank('Shaik Allabakash','Male',236759679098,6300299581,3863,15000)
Applicant1.Checking_balance()
Applicant1.Withdraw()
Applicant1.Deposite()
            
