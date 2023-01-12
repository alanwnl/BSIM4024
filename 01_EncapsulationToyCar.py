class ToyCar:
    def __init__(self):
        self.__speed = 0 # private variable

    def set_speed(self, speed):
        if speed <= 0 or speed > 5:
            print("Invalid speed, please enter a value between 1 and 5")
        else:
            self.__speed = speed
    
    def get_speed(self):
        return self.__speed

car = ToyCar()
car.set_speed(3)
print(car.get_speed()) # prints 3
car.set_speed(-1) # Invalid speed, please enter a value between 1 and 5