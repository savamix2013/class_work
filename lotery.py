import random

# Наш квиток
my_ticket = [3, 7]

# Функція для створення випадкового квитка
def generate_ticket():
    return random.sample(range(1, 11), 2)  # Числа від 1 до 10

# Лічильник спроб
attempts = 0

while True:
    drawn_ticket = generate_ticket()  # Генеруємо новий квиток
    attempts += 1  # Додаємо 1 до спроб

    print(f"Спроба {attempts}: {drawn_ticket}")  # Показуємо поточний квиток

    if drawn_ticket == my_ticket:  # Якщо збіглося — виходимо
        break

print(f"🎉 Виграшний квиток {my_ticket} з'явився через {attempts} спроб!")
