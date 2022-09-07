class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} lat {self.age}"

    @property
    def person_name(self):
        return self.name

    @person_name.setter
    def person_name(self, name):
        self.name = name

    @property
    def person_surname(self):
        return self.surname

    @person_surname.setter
    def person_surname(self, surname):
        self.surname = surname


Maciej = Person("Maciej", "B", 2)

print(Maciej)
Maciej.person_name = "Janek"
Maciej.person_surname = "Nowak"
print(f"Nowe dane osoby to: {Maciej.person_name} {Maciej.person_surname}")
