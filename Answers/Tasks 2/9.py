class Product:
    def __init__(self, name, price, quantity):
        """Инициализация объекта продукта с названием, ценой и количеством."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def increase_quantity(self, amount):
        """Увеличение количества товара."""
        self.quantity += amount
        print(f"Количество товара '{self.name}' увеличено на {amount}.")

    def decrease_quantity(self, amount):
        """Уменьшение количества товара."""
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Количество товара '{self.name}' уменьшено на {amount}.")
        else:
            print(f"Недостаточно товара '{self.name}' на складе.")

    def total_price(self):
        """Расчет общей стоимости товара."""
        total_cost = self.price * self.quantity
        return total_cost

# Пример
if __name__ == "__main__":
    product1 = Product("Книга", 20, 50)
    product2 = Product("Флешка", 10, 100)

    product1.increase_quantity(20)
    product2.decrease_quantity(50)

    total_cost_product1 = product1.total_price()
    total_cost_product2 = product2.total_price()
    print(f"Общая стоимость товара '{product1.name}': {total_cost_product1}")
    print(f"Общая стоимость товара '{product2.name}': {total_cost_product2}")