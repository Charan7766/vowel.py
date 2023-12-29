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
dhoni=Employee()
charan=Employee()

Employee.insert_member(bhanu,'bhanu',22,40000,'rad01')
Employee.insert_member(bindu,'lokesh',23,50000,'rad02')
dhoni.insert_member('dhoni',45,60000,'rad03')
charan.insert_member('dhoni',45,60000,'rad03')
print(charan.name)
print(dhoni.sal)
print(dhoni.Eid)
print(dhoni.age)