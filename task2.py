import turtle

# Функція для малювання дерева Піфагора
def draw_tree(branch_length, level):
    if level > 0:
        # Малюємо гілку
        turtle.forward(branch_length)
        
        # Поворот для малювання лівої гілки
        turtle.left(45)
        draw_tree(branch_length * 0.7, level - 1)
        
        # Поворот для малювання правої гілки
        turtle.right(90)
        draw_tree(branch_length * 0.7, level - 1)
        
        # Повертаємось до початкової позиції та кута
        turtle.left(45)
        turtle.backward(branch_length)

# Основна функція для ініціалізації малювання
def pythagoras_tree(level):
    # Налаштування Turtle
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.left(90)  # Поворот вліво на 90 градусів
    turtle.up()      # Підняти перо
    turtle.backward(200) # Переміститися вниз екрану
    turtle.down()    # Опустити перо

    # Виклик рекурсивної функції для малювання дерева
    draw_tree(100, level)

    # Зупинити відображення вікна після завершення малювання
    turtle.done()

# Запитуємо у користувача рівень рекурсії
level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
pythagoras_tree(level)
