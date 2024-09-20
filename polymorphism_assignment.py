#parent class
class Animal:
    def __init__(self, name, age):
        self.name = name  #name of the animal
        self.age = age    #age of the animal

    def sound(self):
        return "This animal makes a sound"
    
#child class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  #inherit name and age from Animal
        self.breed = breed  #specific breed of the dog

    def sound(self):
        return f"{self.name} barks!"

#child class 
class Cat(Animal):
    def __init__(self, name, age, fur_length):
        super().__init__(name, age)  #inherit name and age from Animal
        self.fur_length = fur_length  #specific fur length of the cat

    def sound(self):
        return f"{self.name} meows!"  

dog1 = Dog("Buddy", 3, "Golden Retriever")
cat1 = Cat("Whiskers", 2, "Short")

print(dog1.sound()) 
print(cat1.sound())
