from physicalEngine2D import *


engine = Engine(3,3)

shape = Rectangle(5, 5, 10, 10)
print shape.linkedPoints
print "centroid : "
print shape.centroid
shape.rotate(45)
print shape.linkedPoints
print len(shape.linkedPoints)
#engine.addNewObject('ru',True,shape)