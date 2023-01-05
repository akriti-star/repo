class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
Akriti=Employee("Akriti",18)
Karan=Employee("Karan",19)
print(Akriti.__dict__)
print(Karan.__dict__)
        