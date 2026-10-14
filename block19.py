#91
class User:
    def init(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f" {self.name},  {self.age}")

user1 = User("Анна", 20)
user1.show_info()

#92
class Car:
    def init(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        print(f" {self.brand} {self.model}, {self.year} ")
my_car = Car("Toyota", "Camry", 2021)
my_car.description()

#93
class BankAccount:
    def init(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Счет пополнен на {amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято {amount}. Остаток: {self.balance}")
        else:
            print("Недостаточно средств на счете!")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)

#96
filename = "users.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("Анна\n")
    file.write("Иван\n")
    file.write("Алексей\n")
print(f"Данные успешно записаны в файл {filename}")

#97
try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"Количество строк в файле: {len(lines)}")
        print("Содержимое файла:")
        for line in lines:
            print(f" - {line.strip()}")
except FileNotFoundError:
    print("Файл не найден!")

#98              
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Ошибка: делить на ноль нельзя!")

#100
todo_list = ["Купить продукты", "Сделать домашку по Python"]
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")
new_task = "Помыть посуду"
todo_list.append(new_task)
print(f"Добавлена задача: '{new_task}'")
print(f"Всего задач в списке: {len(todo_list)}")