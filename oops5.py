class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")
    def speak(self):
        return f"{self.name} says {self.sound} while wagging its tail!"

c = Animal("Cat", "Meow")
d = Dog("Buddy")

print(c.speak())
print(d.speak())