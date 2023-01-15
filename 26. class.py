class Person:
    pass
    
p1 = Person()
p1.name = "Artur"
p1.surname = "Buhil"
p1.birth = "Ukraine"

p2 = Person()
p2.name = "Dasha"
p2.surname = "Bohdan"
p2.birth = "Ukraine"

print(p1.name)
print(f"{p1.name} {p1.surname}")