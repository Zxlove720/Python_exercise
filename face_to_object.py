class Animal:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        pass


class Dog(Animal):
    def shout(self):
        print(f"{self.name}在犬吠")


class Cat(Animal):
    def shout(self):
        print(f"{self.name}在猫叫")


def animal_world(animal: Animal):
    animal.shout()


if __name__ == '__main__':
    cat = Cat("Tom", 2)
    dog = Dog("旺财", 3)
    animal_world(cat)
    animal_world(dog)

