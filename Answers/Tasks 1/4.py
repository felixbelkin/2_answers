import random

def determine_winner(user_choice, computer_choice):
    """Определение победителя."""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

def main():
    # Возможные ходы
    choices = ["камень", "ножницы", "бумага"]

    # Запрашиваем ход пользователя
    user_choice = input("Введите ваш ход (камень, ножницы, бумага): ").strip().lower()

    if user_choice not in choices:
        print("Неправильный выбор. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
        return

    # Ход компьютера
    computer_choice = random.choice(choices)
    print(f"Ход компьютера: {computer_choice}")

    # Определяем победителя
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
