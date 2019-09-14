class Peson():
    def __init__(self,name,occupation=None, address=None):
        self.name=name 
        self.occupation= occupation
        self.address= address
        self.validator()

    def validator(self):
        if self.address and self.occupation:
            print(self.occupation , self.address)
            return self.address , self.occupation
        elif self.address:
            print(self.address)
            return self.address
        elif self.occupation:
            print("here")
            print(self.occupation)
            return self.occupation
        else:
            print("enter address or occupations")
            return False 

        

