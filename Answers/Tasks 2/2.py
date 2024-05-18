class Soda:
    def __init__(self, additive=None):
        """Инициализация объекта газированной воды с добавкой (если есть)."""
        self.additive = additive

    def show_my_drink(self):
        """Выводит описание напитка в зависимости от наличия добавки."""
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")

#for example
 
if __name__ == "__main__":
    soda_with_additive = Soda("лимон")
    soda_without_additive = Soda()
    soda_with_additive.show_my_drink()
    soda_without_additive.show_my_drink()
