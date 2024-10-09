class Indain_bank():
    Name ='Indian Bank'
    Barnch = 'Bengaluru'
    IFSC = 'INBNO123'
    RAte_of_intrest = 5
    def __init__(self,Accountant_name,Age,Gender,Pin,Balance,Mobile):
        self.Accountant_name = Accountant_name
        self.Age = Age
        self.Gender = Gender
        self.Pin= Pin
        self.Balance = Balance
        self.Mobile = Mobile
    @staticmethod
    def Take_pin():
        password = int(input('Enter the Pin: '))
        return password
    @classmethod
    def Change_of_ROI(cls):
        new_ROi = float(input('Enter the new rate of intrest: '))
        cls.RAte_of_intrest = new_ROi
    def Withdraw_money(self):
        if self.Pin == self.Take_pin():
            withdraw_amount = int(input('Enter the withdraw amount: '))
            if self.Balance >= withdraw_amount:
                self.Balance -= withdraw_amount
                print(f'{withdraw_amount} is Debited successfully !....')
                print(f'Available balance is {self.Balance} RS')
            else:
                print('Insufficient funds!...')
        else:
            print('Invalid pin !....')
    def Deposite(self):
        if self.Pin == self.Take_pin():
            Deposite_amount = int(input('Enter the withdraw amount: '))
            self.Balance += Deposite_amount
            print(f'{Deposite_amount} is Credited successfully !....')
            print(f'Available balance is {self.Balance} RS')
        else:
            print('Invalid pin !....')
    def Checking_balance(self):
        if self.Pin == self.Take_pin():
            print(f'Available balance is {self.Balance} RS')
        else:
            print('Invalid pin .....')
user1 = Indain_bank('shaik',19,'male',6300,1598746321,90006300855)
user1.Checking_balance()
user1.Withdraw_money()
user1.Deposite()
    
