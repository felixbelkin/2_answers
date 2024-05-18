class BankAccount:
    def __init__(self, account_number, owner, balance):
        """Инициализация объекта банковского счета с номером счета, владельцем и балансом."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополнение счета."""
        commission = amount * 0.01  # Рассчитываем комиссию
        total_amount = amount - commission  # Вычитаем комиссию из суммы пополнения
        self.balance += total_amount  # Увеличиваем баланс на сумму пополнения
        print(f"Счет пополнен на {total_amount:.2f} (включая комиссию 1%). Новый баланс: {self.balance:.2f}")

    def withdraw(self, amount):
        """Снятие средств со счета."""
        if amount <= self.balance:
            commission = amount * 0.01  # Рассчитываем комиссию
            total_amount = amount + commission  # Добавляем комиссию к сумме снятия
            self.balance -= total_amount  # Уменьшаем баланс на сумму снятия с учетом комиссии
            print(f"Со счета списано {total_amount:.2f} (включая комиссию 1%). Новый баланс: {self.balance:.2f}")
        else:
            print("Недостаточно средств на счете.")

    def check_balance(self):
        """Проверка баланса."""
        print(f"Текущий баланс на счете: {self.balance:.2f}")

# Пример
if __name__ == "__main__":
    account1 = BankAccount("123456789", "Иванов", 1000)
    account2 = BankAccount("987654321", "Петров", 500)

    account1.deposit(500)
    account2.withdraw(200)

    account1.check_balance()
    account2.check_balance()
