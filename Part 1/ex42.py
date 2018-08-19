## Animal is-a object.
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ## Animal has-a name (Dog).
        self.name = name

## Cat is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        ## Animal has-a name (Cat).
        self.name = name

# Person is-a object.
class Person(object):

    def __init__(self, name):
        ## Object has-a name (Person).
        self.name = name
        ## Person has-a pet of some kind.
        self.pet = None

## Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary):
        ## Super allows for multiple inheritance in the __init__ function.
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a fish.
class Halibut(Fish):
    pass

## rover is-a Dog.
rover = Dog("Rover")

## satan is-a Cat.
satan = Cat("Satan")

## Mary is-a Person.
mary = Person("Mary")

## mary has-a pet Cat.
mary.pet = satan

## frank is-a Employee.
frank = Employee("Frank", 120000)

## frank has-a pet Dog.
frank.pet = rover

## flipper is-a Fish.
flipper = Fish()

## crouse is-a Salmon.
crouse = Salmon()

## Harry is-a Halibut.
harry = Halibut()
