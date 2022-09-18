# Создайте класс Car. Добавьте обязательные атрибуты класса: модель, год выпуска,
# объем двигателя, цена, пробег, количество колес = 4.
# Создайте 1 экземпляр класса
# Создать класс наследник - Грузовик. Который наследует все атрибуты класса,
# но количество колес = 8.
# Создать 1 экземпляр класса Наследника
# engine capacity, price, mileage, number of wheels

class Car():

    def __init__(self, model, data_release, engine_capacity, price, mileage):
        "Инициализация класса Car"
        self.model = model  # модель
        self.data_release = data_release  # год выпуска
        self.engine_capacity = engine_capacity  # объем двигателя
        self.price = price  # цена
        self.mileage = mileage  # пробег
        self.number_wheels = 4  # количество колес

    def description_car(self):
        "Описание всех автомобилей"
        description_car = "Модель грузовика: " + self.model + ", дата выпуска: " + str(self.data_release) \
                      + ", объём двигателя: " + str(self.engine_capacity) + ", цена: " + str(self.price) \
                      + ", пробег: " + str(self.mileage) + ", количество колес: " + str(self.number_wheels)
        return description_car

class Truck(Car):

    def __init__(self, model, data_release, engine_capacity, price, mileage):
        super().__init__(model, data_release, engine_capacity, price, mileage)
        self.number_wheels = 8

    def description_truck(self):
        "Описание грузовиков"
        description_truck = "Модель грузовика: " + self.model + ", дата выпуска: " + str(self.data_release) \
                      + ", объём двигателя: " + str(self.engine_capacity) + ", цена: " + str(self.price) \
                      + ", пробег: " + str(self.mileage) + ", количество колес: " + str(self.number_wheels)
        return description_truck


car_my = Car("UAZ", "20.02.2022", 120, 60000000, 140000)
print("Вывод автомобиля родителя: " + car_my.description_car())

truck_my = Truck("UAZ", "20.02.2022", 120, 60000000, 14000)
print("Вывод грузовика, как предка-автомобиля: " + truck_my.description_truck())

