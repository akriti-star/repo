class Employee:
    no_of_leaves=6
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    
Akriti=Employee("Akriti",18)
Karan=Employee("Karan",19)
Karan.change_leaves(4) 
Akriti.change_leaves(45)


print(Akriti.no_of_leaves)
print(Karan.no_of_leaves)
        