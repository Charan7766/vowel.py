class Sbi:
    branch='v kota'
    ifsc='sbi00026'
    manager='charan'
    location='chit'
    def __init__(self,name,mob,acc,pan,bal):
        self.name=name
        self.mobile=mob
        self.account=acc
        self.pan=pan
        self.balance=bal
    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
chanda= Sbi('nara chandra',6305346774,4444556,'cbt44444',1)
lokesh= Sbi('nara lokesh',6305346775,4444557,'cbt44445',2)
print(chanda.name)
    