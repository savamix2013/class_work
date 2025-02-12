# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину"""
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         """Вернути коротке ім'я машини"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())


#________________________________________________________________________________________


# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Вернути коротке ім'я машини"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Виводити значення одометра"""
#         print(f"This car has {self.odometer_reading} miles on it")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


#________________________________________________________________________________________


# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Вернути коротке ім'я машини"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Виводити значення одометра"""
#         print(f"This car has {self.odometer_reading} miles on it")

#     def update_odometer(self, mileage):
#         """антизміна пробігу"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(-1)
# my_new_car.read_odometer()


#________________________________________________________________________________________



# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Вернути коротке ім'я машини"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Виводити значення одометра"""
#         print(f"This car has {self.odometer_reading} miles on it")

#     def update_odometer(self, mileage):
#         """антизміна пробігу"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """підвищення одометра"""
#         self.odometer_reading += miles

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()