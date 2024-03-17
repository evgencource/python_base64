# python_base64

Задача 1

0.0/5.0 points (graded)
Задано скрипт, який отримує список рядків, що містять етапи життєвого циклу розробки програмного забезпечення: "plan", "code", "test", "delivery", "deploy" та "monitor".

Скрипт циклічно переглядає список і виводить кожен елемент на консоль.

Приклад рішення на Python:

```
# Define an array of strings representing the steps in a software development lifecycle
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

# Loop through each step in the array and perform an operation
for step in steps:
    # Perform some operation related to the current step
    print(step)
```
У цьому коді визначено список з назвою steps, а потім виконано перебір кожного елемента списку за допомогою циклу for. Змінна циклу step набуває значення кожного елемента списку по черзі, а функція print() викликається для виведення кожного кроку на консоль.

Завдання: Проявіть інженерне мислення та модифікуйте цей скрипт, щоб виводити кожен елемент списку steps у вигляді рядка у форматі base64.

Наприклад, елемент “plan” буде виглядати як b'cGxhbg=='
