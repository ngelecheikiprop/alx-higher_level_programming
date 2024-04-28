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