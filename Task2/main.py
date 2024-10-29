from collections import deque


def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    s = s.lower().replace(" ", "")

    # Створюємо двосторонню чергу
    char_deque = deque(s)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        # Видаляємо та порівнюємо символи з початку та кінця
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо хоч один символ не співпадає, це не паліндром

    return True  # Якщо всі символи співпадають, це паліндром


# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # Поверне True
print(is_palindrome("Hello world"))  # Поверне False