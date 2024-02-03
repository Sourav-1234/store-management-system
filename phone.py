from item import Item
class Phone(Item):
    all=[]
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        # assert price>=0 ,f"Price {price} is not greater than or equal to zero!"
        # assert quantity>=0 ,f"Quantity {quantity} is not greater or equal to than zero!"
        super().__init__(name,price,quantity
        )
        assert broken_phones>=0 ,f"Broken Phones {broken_phones} is not greater than zero!"

        
        self.name=name
        self.price=price
        self.quantity=quantity
        self.broken_phones=broken_phones

       

        Phone.all.append(self)
    
