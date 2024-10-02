class Car:
    """Класс Автомобилей"""
    def __init__(self, model: str, vin: int, numbers: str): # атрибуты класса Car: модель, vin, номер
        self.model = model # модель автомобиля
        if self.__is_valid_vin(vin):
            self.__vin = vin  # vin номер автомобиля
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # номер автомобиля

    def __is_valid_vin(self, vin_number): # функция проверки vin
        if not isinstance(vin_number, int): # если vin не является числом int возвращает исключение
            raise IncorrectVinNumber('некорректный тип vin номер') # исключение
        elif len(str(vin_number)) != 7: # если длина не равна 7 возвращает исключение
            raise IncorrectVinNumber('неверный диапозон для vin номер') # исключение
        else:
            return True # возвращает True если vin соответствует условиям (длина 7)

    def __is_valid_numbers(self, numbers): # функция проверки номера
        if not isinstance(numbers, str): # если номер не является строкой возвращает исключение
            raise IncorrectCarNumbers('некорректный тип номера') # исключение
        elif len(numbers) != 6: # если длина нномера не равна 6 возвращает исключение
            raise IncorrectCarNumbers('неверная длина номера') # исключение
        else:
            return True # возвращает True если номер соответствует условиям (длина 6


class IncorrectVinNumber(Exception): # класс исключения IncorrectVinNumber
    def __init__(self, message):
        self.message = message # сообщение исключения INCORRECT_VIN_NUMBER


class IncorrectCarNumbers(Exception): # класс исключения IncorrectCarNumbers
    def __init__(self, message):
        self.message = message # сообщение исключения INCORRECT_CAR_NUMBERS


def CreateCar(model: str, vin: int, numbers: str): # функция создания автомобиля
    try:
        car = Car(model, vin, numbers) # создание объекта класса Car с атрибутами model, vin, numbers
    except IncorrectVinNumber as exc: # исключение INCORRECT_VIN_NUMBER как exc
        print(exc.message) # печать сообщения исключения
    except IncorrectCarNumbers as exc: # исключение INCORRECT_CAR_NUMBERS как
        print(exc.message) # печать сообщения исключения
    else:
        print(f'{car.model} успешно создан') # если все параметры автомобиля корректны печать сообщения


if __name__ == '__main__':
    first = CreateCar('Model1', 1000000, 'f123dj')
    second = CreateCar('Model2', 300, 'т001тр')
    third = CreateCar('Model3', 2020202, 'нет номера')
