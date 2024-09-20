#parent class
class Vehicle:
    make = 'Unknown'  #manufacturer of the vehicle
    model = ''  #model of the vehicle

#child class for car
class Car(Vehicle):
    doors = 4  #number of doors on the car
    fuel_type = 'Gasoline'  #type of fuel the car uses

#child class for motorcycle
class Motorcycle(Vehicle):
    engine_size = '500cc'  #engine size of the motorcycle
    has_sidecar = False  #whether the motorcycle has a sidecar
