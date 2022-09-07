class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} lat {self.age}"

    def get_person_name(self):
        return self.name

    def set_person_name(self, name):
        self.name = name

    def get_person_surname(self):
        return self.surname

    def set_person_surname(self, surname):
        self.surname = surname


Maciej = Person("Maciej", "B", 2)

print(Maciej)
Maciej.set_person_name("Adam")
Maciej.set_person_surname("Jakis")
print(f"Nowe dane to: {Maciej.get_person_name()} {Maciej.get_person_surname()}")
