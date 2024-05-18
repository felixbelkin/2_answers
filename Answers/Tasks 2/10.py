class Student:
    def __init__(self, name, age):
        """Инициализация объекта студента с именем, возрастом и пустым списком предметов."""
        self.name = name
        self.age = age
        self.subjects = []

    def add_subject(self, subject):
        """Добавление предмета в список."""
        self.subjects.append(subject)
        print(f"Предмет '{subject}' добавлен для студента '{self.name}'.")

    def remove_subject(self, subject):
        """Удаление предмета из списка."""
        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"Предмет '{subject}' удален для студента '{self.name}'.")
        else:
            print(f"Предмет '{subject}' не найден у студента '{self.name}'.")

    def average_score(self):
        """Расчет среднего балла студента."""
        if not self.subjects:
            print(f"Для студента '{self.name}' нет предметов.")
            return None
        total_score = sum(self.subjects)
        average = total_score / len(self.subjects)
        return average

# Пример
if __name__ == "__main__":
    student1 = Student("Иванов", 20)
    student2 = Student("Петров", 22)

    student1.add_subject(5)
    student1.add_subject(4)
    student1.add_subject(3)
    student2.add_subject(4)
    student2.add_subject(4)
    student2.add_subject(5)

    student1.remove_subject(3)
    student2.remove_subject(4)

    avg_score_student1 = student1.average_score()
    avg_score_student2 = student2.average_score()
    print(f"Средний балл студента '{student1.name}': {avg_score_student1}")
    print(f"Средний балл студента '{student2.name}': {avg_score_student2}")
