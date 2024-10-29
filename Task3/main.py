def check_brackets(expression):
    # Відповідні пари дужок
    brackets = {')': '(', ']': '[', '}': '{'}
    # Стек для відкритих дужок
    stack = []

    for char in expression:
        # Якщо символ є відкритою дужкою, додаємо його в стек
        if char in brackets.values():
            stack.append(char)
        # Якщо символ є закритою дужкою
        elif char in brackets:
            # Перевіряємо, чи стек не порожній і чи останній символ у стеці є парою до поточної дужки
            if stack and stack[-1] == brackets[char]:
                stack.pop()  # Витягуємо зі стеку, оскільки знайшли відповідну пару
            else:
                return "Несиметрично"  # Дужки не симетричні або не відповідають парі

    # Перевірка, чи стек порожній (усі дужки мали пару)
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


# Приклади використання
print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_brackets("( 23 ( 2 - 3);"))  # Несиметрично
print(check_brackets("( 11 }"))  # Несиметрично