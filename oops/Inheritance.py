#  1. Single Inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()   # Inherited from Animal
d.bark()    # From Dog



# 2. Multiple Inheritance

class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()


# 3. Multilevel Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()


# 4. Hierarchical Inheritance
class Parent:
    def display(self):
        print("Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.display()
c2.display()


#  5. Hybrid Inheritance (Combination)
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):  # Hybrid (multiple + multilevel)
    pass

d = D()
d.show()
