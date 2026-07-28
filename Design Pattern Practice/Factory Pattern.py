from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak()) 
print(cat.speak()) 

# Output: 
# Woof!
# Meow!
