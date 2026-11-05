print("Рады приветстовать Вас в нашем приложении! Давай знакомиться!")

user_name = input("Как Вас зовут?")
print(f"Привет, {user_name}!")
user_age = int(input("Сколько Вам полных лет: "))
print(f"Спасибо за ответы, {user_name}!")

print("Давайте рассчитаем Ваш индекс массы тела (ИМТ)")
print("ИМТ рассчитывается по формуле: ИМТ = вес (кг) / (рост (м) * рост (м))")
print("Позвольте уточнить Ваши данные для расчета ИМТ")
user_weight_kg = float(input("Ваш вес в килограммах (например, 70.5): "))
user_height_m = float(input("Ваш рост в метрах (например, 1.75) : "))

bmi = user_weight_kg / (user_height_m ** 2)
bmi = round(bmi, 1)

water_ml = user_weight_kg * 30
water_liters = water_ml / 1000
water_liters = round(water_liters, 2)

print("Спасибо за предоставленные данные!")
print(f"Отчет для пользователя:\n"
      f"Имя: {user_name}, возраст: {user_age} г.")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды в день: {water_liters} литров")

print("Спасибо за использование нашего приложения!")
print("Желаем Вам здоровья и хорошего настроения!")