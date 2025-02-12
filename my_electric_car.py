from car import Car

class Battery:
    """Проба змоделювати батарею"""

    def __init__(self, battery_size=75):
        """інціалізувати атрибути, що описують батарею"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вивести повідомлення про розмір акамулятора"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Вивести повідомлення про діапазон дії батареї"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Проба змоделювати електромобіль"""

    def __init__(self, make, model, year):
        """ініціалізувати атрибути батьківського класу
        тоді ініціалізувати атрибути електрокара"""
        super().__init__(make, model, year)
        self.battery = Battery()