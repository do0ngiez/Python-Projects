class Car:
    def __init__(self, make, model):
        self.__fuel_level = 0 #private attribute

        #protected attributes
        self._make = make
        self._model = model
    

    #method to add fuel to the car object
    def add_fuel(self, amount):
        if amount > 0:
            self.__fuel_level += amount
        else:
            print("Not enough fuel")
    
    #method to drive th car
    #will deduct fuel from the car
    def drive(self, distance):
        fuel_needed = distance * 0.2
        if fuel_needed <= self.__fuel_level:
            self.__fuel_level -= fuel_needed
            print(f"Drove {distance} km")
        else:
            print("Not enough fuel")

    #method to get fuel level
    def getFuelLevel(self):
        return self.__fuel_level

#create an instance of the car
newCar = Car("Toyota", "Vios")

#add fuel to the created car instance
newCar.add_fuel(50)

#drive the car
newCar.drive(100)

#print the remaining fuel level
print(f"Remaining fuel level: {newCar.getFuelLevel()} liters.")

