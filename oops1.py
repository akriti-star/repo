class Students:
    In_Standard=7
    def printDetails(self):
        return f"The name is {self.name}.Marks are{self.Marks}.Roll_no is{self.Roll_no}."
Akriti=Students()
Karan=Students()
Shivani=Students()
Akriti.name="Akriti"
Karan.name="Karan"
Shivani.name="Shivani"
Akriti.Marks=70
Karan.Marks=90
Shivani.Marks=60
Akriti.Roll_no=6
Karan.Roll_no=7
Shivani.Roll_no=4
print(Akriti.printDetails())
print(Karan.printDetails())
print(Shivani.printDetails())