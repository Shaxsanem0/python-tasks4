#zadaniya s 81 po 85
#81
squares=[x**2 for x in range(21)]
print(f"{squares}")

#82
even_squares=[x**2 for x in range(15) if x%2==0]
print(f"{even_squares}")

#83
words = ["python", "код", "программирование", "идея", "разработка", "мир"]
print(f"Исходный список слов: {words}")
long_words = [word for word in words if len(word) > 5]
print(f"Слова длиннее 5 символов: {long_words}")

#85
celsius_temps = [0, 10, 20, 25, 30, 100]
print(f"Температуры в Цельсиях: {celsius_temps}")
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(f"Температуры в Фаренгейтах: {fahrenheit_temps}")