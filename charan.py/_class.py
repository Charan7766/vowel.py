class Employee:
    company='Radisys'
    CEO='charan'
    def insert_member(obj,name,age,sal,eid):
        obj.name=name
        obj.age=age
        obj.sal=sal
        obj.Eid=eid

bhanu=Employee()
bindu=Employee()      


Employee.insert_member(bhanu,'bhanu',22,40000,'rad01')
Employee.insert_member(bindu,'lokesh',23,50000,'rad02')
print(bhanu.age)
print(bhanu.name)
print(bhanu.sal)
