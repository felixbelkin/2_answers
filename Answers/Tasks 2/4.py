class Nikola:
    def __init__(self, name, age):
        """Инициализация с именем и возрастом."""
        self.age = age
        if name.lower() == "николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"

    def get_name(self):
        """Возвращает имя."""
        return self.name

    def get_age(self):
        """Возвращает возраст."""
        return self.age

#for example
if __name__ == "__main__":
    person1 = Nikola("Николай", 30)
    person2 = Nikola("Максим", 25)
    print(f"Имя: {person1.get_name()}, Возраст: {person1.get_age()}")
    print(f"Имя: {person2.get_name()}, Возраст: {person2.get_age()}")
