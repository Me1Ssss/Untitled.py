class Pet:
    def __init__(self, name, species, age, gender):
        self.__name = name      # приватный атрибут
        self.__species = species
        self.__age = age
        self.__gender = gender
    
    # Геттеры для доступа к приватным атрибутам
    def get_name(self):
        return self.__name
    
    def get_species(self):
        return self.__species
    
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    def get_info(self):
        return f"Имя: {self.__name}, Вид: {self.__species}, Возраст: {self.__age}, Пол: {self.__gender}"

class Dog(Pet):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, "Собака", age, gender)  # Вызываем конструктор родительского класса
        self.__breed = breed  # приватный атрибут породы
    
    def get_breed(self):
        return self.__breed
    
    def bark(self):
        return "Гав!"
    
    # Переопределяем get_info для включения породы
    def get_info(self):
        return f"{super().get_info()}, Порода: {self.__breed}"

class Cat(Pet):
    def __init__(self, name, age, gender, color):
        super().__init__(name, "Кошка", age, gender)
        self.__color = color  # приватный атрибут цвета
    
    def get_color(self):
        return self.__color
    
    def meow(self):
        return "Мяу!"
    
    # Переопределяем get_info для включения цвета
    def get_info(self):
        return f"{super().get_info()}, Цвет: {self.__color}"

# Демонстрация работы классов
def main():
    # Создаем экземпляры
    dog = Dog("Шарик", 3, "Мужской", "Лабрадор")
    cat = Cat("Мурка", 2, "Женский", "Серый")
    
    # Демонстрация полиморфизма через метод get_info()
    pets = [dog, cat]
    print("Информация о питомцах:")
    for pet in pets:
        print(pet.get_info())
    
    # Вызов специфичных методов
    print("\nДемонстрация специфичных методов:")
    print(f"{dog.get_name()} говорит: {dog.bark()}")
    print(f"{cat.get_name()} говорит: {cat.meow()}")
    
    # Демонстрация инкапсуляции
    print("\nДемонстрация доступа через геттеры:")
    print(f"Порода собаки: {dog.get_breed()}")
    print(f"Цвет кошки: {cat.get_color()}")

if __name__ == "__main__":
    main()
