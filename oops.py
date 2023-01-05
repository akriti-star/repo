class Students:
    In_Standard=7
    pass
Akriti=Students()
Karan=Students()
Shivani=Students()
Akriti.Marks=70
Karan.Marks=90
Shivani.Marks=60
Akriti.Roll_no=6
Karan.Roll_no=7
Shivani.Roll_no=4
print(Akriti.__dict__,Karan.__dict__,Shivani.__dict__)
print(Students.In_Standard)
print(Students.__dict__)