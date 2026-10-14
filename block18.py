#zadaniya s 86 po 90
#86
print("--- Task 86 ---")
numbers = [-5, 3, 0, 12, -8, 7]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(f"Положительные числа: {positive_numbers}")

#87
words = ["python", "программирование", "идея", "разработка", "мир"]
print(f"Исходный список слов: {words}")
long_words = [word for word in words if len(word) > 5]
print(f"Слова длиннее 5 символов: {long_words}")

#89
users = [
    {"name": "Алексей", "age": 25},
    {"name": "Ольга", "age": 19},
    {"name": "Иван", "age": 30}
]
sorted_users = sorted(users, key=lambda user: user["age"])
print("Пользователи, отсортированные по возрасту:")
for u in sorted_users:
    print(u)

#90
adults = [user["name"] for user in users if user["age"] > 18]
print(f"Имена пользователей старше 18: {adults}")