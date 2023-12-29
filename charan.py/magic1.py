class Employee:
    company='Radisys'
    CEO='charan'
    def __init__(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.Eid=eid



bhanu=Employee('bhanu',22,40000,'rad01')
print(bhanu.name)
print(bhanu.age)
print(bhanu.Eid)