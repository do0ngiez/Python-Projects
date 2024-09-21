from abc import ABC, abstractmethod

#create parent class called Pet
class Pet(ABC):
    #abstract method to be implemented by subclasses
    def sound(self):
        pass
    
    #method that can be used by all subclasses
    def eat(self):
        print("The pet is eating.")

#create a subclass Dog that inherits from Pet
class Dog(Pet):
    #implement the abstract method inherited from Pet class
    #define an implementation for the method
    def sound(self):
        print("Dog barking")

#create another subclass Cat that inherits from Pet
class Cat(Pet):
    #implement the abstract method from Pet
    def sound(self):
        print("Cat meows")

#create instances of Dog and Cat
dog = Dog()
cat = Cat()

#call the abstract method
dog.sound()
cat.sound()

#call the regular method from parent class
dog.eat()
cat.eat()
