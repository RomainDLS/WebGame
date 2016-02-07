from physicalEngine2D import *
from shape import Shape, Rectangle

engine = Engine(3,3)

shape = Rectangle(10, 10)
print shape.pixelList
engine.addNewObject('ru',True,shape)