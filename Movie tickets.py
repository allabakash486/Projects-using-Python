def booking(arg):
    l=[]
    def inner():
        if len(l)==0:
            l.append(arg())
            return l[0]
    return inner
@booking
class Devara():
    def __init__(self) -> None:
        self.max_no_tickets = 500

    def Booking(self,request):
        if self.max_no_tickets>=request:
            self.max_no_tickets -= request
            print(f'{request} Tickets  is booked successfully....!😊😊😊😊😊😊😉😉😉')
        else:
            print('Insuffcient tickets...!😒😒😒😒')
@booking
class Swag():
    def __init__(self) -> None:
        self.max_no_tickets = 250

    def Booking(self,request):
        if self.max_no_tickets>=request:
            self.max_no_tickets -= request
            print(f'{request} Tickets  is booked successfully....!😊😊😊😊😊😊😉😉😉')
        else:
            print('Insuffcient tickets...!😒😒😒😒')
def Google_pay():
    print('Available Movies are shown in below ...\n 1) Devara   😎😎😎 \n2)Swag  😉😉😉😉😉')
    choice = int(input('Enter the number...!'))
    if choice == 1:
        object1 = Devara()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    elif choice==2:
        object1 = Swag()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    else:
        print('invalid number')
def Phone_pay():
    print('Available Movies are shown in below ...\n 1) Devara   😎😎😎 \n2)Swag  😉😉😉😉😉')
    choice = int(input('Enter the number...!'))
    if choice == 1:
        object1 = Devara()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    elif choice==2:
        object1 = Swag()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    else:
        print('invalid number')
def Paytm_pay():
    print('Available Movies are shown in below ...\n 1) Devara   😎😎😎 \n2)Swag  😉😉😉😉😉')
    choice = int(input('Enter the number...!'))
    if choice == 1:
        object1 = Devara()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    elif choice==2:
        object1 = Swag()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    else:
        print('invalid number')
def Whatsapp_pay():
    print('Available Movies are shown in below ...\n 1) Devara   😎😎😎 \n2)Swag  😉😉😉😉😉')
    choice = int(input('Enter the number...!'))
    if choice == 1:
        object1 = Devara()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    elif choice==2:
        object1 = Swag()
        No_of_tickets = int(input('Enter the number of ticktes :'))
        object1.Booking(No_of_tickets)
    else:
        print('invalid number')
user1= Whatsapp_pay()
user3 = Google_pay()
    
        
        