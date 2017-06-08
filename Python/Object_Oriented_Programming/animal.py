class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Your health is", self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = health
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = health
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        self.displayHealth()
        print "I am a Dragon"
        return self

animal1 = Animal("bird", 105)
animal1.walk().walk().walk().run().run().displayHealth()
dog1 = Dog("german shephard", 150)
dog1.walk().walk().walk().run().run().displayHealth()
dragon1 = Dragon("wallie", 170)
