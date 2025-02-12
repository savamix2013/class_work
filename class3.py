# class Car:
#     """Проста спроба змоделювати автівку."""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"this car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("you can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """Тільки для електрокарів."""

#     def __init__(self, make, model, year):
#         """Започаткувати атрибути батьківського класу"""
#         super().__init__(make, model, year)
#         self.battery_size = 75

#     def describe_battery(self):
#         """Вивести інформацію про розмір батареї"""
#         print(f"This car has a {self.battery_size}-kWh battery")

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()


#_______________________________________________________________________________________


# class Car:
#     """Проста спроба змоделювати автівку."""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"this car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("you can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class Battery:
#     """Проста спроба змоделювати батарею електрокара."""

#     def __init__(self, battery_size=75):
#         """ініціалізувати атрибут акуму"""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Вивести інформацію про розмір батареї"""
#         print(f"This car has a {self.battery_size}-kWh battery")

#     def get_range(self):
#         """відстань на акумі"""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car can go about {range} miles on a full charge")

# class ElectricCar(Car):
#     """Тільки для електрокарів."""

#     def __init__(self, make, model, year):
#         """Започаткувати атрибути батьківського класу"""
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()