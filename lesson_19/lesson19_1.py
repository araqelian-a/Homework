# Write a Class named TemperatureSensor that has the attribute
# temperature(private)., default value is 0:
# write a getter and setter for the temperature attribute. use the @property
# decorator for the getter and the @attribute.setter for setter
# if the temperature is less than 0 or greater than 100 raise a ValueError
class TemperatureSensor:
    def __init__(self, temperature=0):
        self.__temperature = temperature
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, new_temperature):
        if 0 < new_temperature < 0:
            raise ValueError("Write other temperature")
        else:
            self.__temperature = new_temperature
temp_1 = TemperatureSensor(10)
print(temp_1.temperature)
temp_1.temperature = 15
print(temp_1.temperature)

