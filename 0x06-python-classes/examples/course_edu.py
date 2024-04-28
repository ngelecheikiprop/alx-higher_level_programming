class Robot:
    pass
x = Robot()
Robot.brand = "kuka"
print(x.brand)

x.brand = "thales"
print(Robot.brand)

y = Robot()
print(y.brand)
print("------")
print (x.__dict__)
print(y.__dict__)
print(Robot.__dict__)

#raises an attribute error
#print(x.energy)

#how you can prevent this error
print(getattr(x,'energy', 100))

#METHODS
#-------------

def hi(obj):
    print("hi there {}".format(obj.name))
class Robot:
    pass

x = Robot()
x.name = "kip"
hi(x)

#the __INIT__ METHOD

class A:
    def __init__(self):
        print("init is running now")

x = A()

#adding to init to our initial class
class Robot:
    def __init__(self, name = None):
        self.name  = name
    def say_hi(self):
        if self.name:
            print("Hi I am {}".format(self.name))
        else:
            print("I dont have a name but hi anyway")

x = Robot()
x.say_hi()

y = Robot("Kiprop")
y.say_hi()
