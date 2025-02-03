class Whatsapp_version1():
    Application_name = "What'sApp" 
    def __init__(self,Username,password,chatting) -> None:
        self.Username = Username
        self.password = password
        self.chatting = chatting
    def Whatsapp_v1(self):
        print(f'Yes username is avilable {self.Username}')
        print(f'yes can set password {self.password}')
        print(f'yes can chat with contact members..{self.chatting}')
class Whatsapp_version2(Whatsapp_version1):
    def __init__(self, Username, password, chatting,Voice_call,Current_loc):
        Whatsapp_version1.__init__(self)
        self.Voice_call = Voice_call
        self.Current_loc = Current_loc
    def Whatsapp_v2(self):
        Whatsapp_version1.Whatsapp_v1(self)
        print(f'Yes can  you talk via voice calls {self.Voice_call}')
        print(f'yes can share current location {self.Current_loc}')
class Whatsapp_version3(Whatsapp_version2):
    def __init__(self, Username, password, chatting, Voice_call, Current_loc,Video_call,Status):
        Whatsapp_version2.__init__(self)
        self.Video_call = Video_call
        self.Status = Status
    def Whatsapp_v3(self):
        Whatsapp_version2.Whatsapp_v2(self)
        print(f'Yes can  you talk via video calls {self.Video_call}')
        print(f'yes can share  status{self.Status}')
user1 =Whatsapp_version3('Shaik',123,'yes','yes ','no','yes','yah sure')

        
    
        
        
