
# The __init__() Function ........

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Sagar", 21)

print(p1.name)
print(p1.age)   


### Object Methods:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Sagar", 21)
p1.myfunc()