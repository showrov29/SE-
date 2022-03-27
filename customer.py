


from sqlite3 import Cursor


class User:
    
        
    _name=None
    _id=None
    _email=None
    _password=None
    _address=None

    def __init__(self,name,id,address,email,password) -> None:
        self._name=name
        self._email=email
        self._password=password
        self._id=id
        self._address=address

    def getSession(self):
        print("Request is valid.")


class customer(User):
    
    _address=None
    _billing_address=None

    def login(self,email,pasword):
        if User._email==email and User._password==pasword:
            return True

 
    def __init__(self, name, id, address, email, password) -> None:
        super().__init__(name, id, address, email, password)

    # def __init__(self,name, address, billing_address) :
    #     super().__init__(self,name)
    #     self.address=address
    #     self.billing_address=billing_address
 
    def customerInfo(User):
        print("Name : ",User._name)
        print("Address : ",User._address)
        


user1=customer("Atif",2042824,"Basundhara","showrovislam29@gmail.com",29082001)



# if (c1.login('showrovislam29@gamil.com',29082001)):
user1.customerInfo()
# else:
#     print("Invalid user")

