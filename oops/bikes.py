# oops/bikes.py

class Bikes:
    def __init__(self, brand, rent):
        self.__bikename = brand
        self.__rentperday = rent

    @property
    def bikename(self):
        return self.__bikename

    @bikename.setter
    def bikename(self, value):
        self.__bikename = value

    def calculate_rent(self, days):
        return self.__rentperday * days
