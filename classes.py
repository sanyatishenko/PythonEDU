####################################
# Классы
####################################

from math import pi

class Shape():
    
    cordX = 0
    cordY = 0
    
    def __init__(self, x, y):
        self.cordX = x
        self.cordY = y
       
    def move(self, MoveX, MoveY):
        self.cordX += MoveX
        self.cordY += MoveY

    def __str__(self):
        return("This is shape with center: " + str(self.cordX)+":"+str(self.cordY))



class Circle(Shape):

    radius = 0

    def __init__(self, cordX, cordY, radius):
        super().__init__(cordX, cordY)
        self.radius = radius

    def area(self):
        return(pi*self.radius**2)

    def length(self):
        return(2*pi*self.radius)

    def __str__(self):
        return("This is circle with center: " + str(self.cordX)+":"+str(self.cordY)+\
                " and radius: "+str(self.radius))

C = Circle(1, 1, 1)
S = Shape(2,2)
print(C)                                        # This is circle with center: 1:1 and radius: 1
C.move(1,1)
print(C)                                        # This is circle with center: 2:2 and radius: 1
print(S)                                        # This is shape with center: 2:2
print("Circle area: " + str(C.area()))          # Circle area: 3.141592653589793
print("Circle length: " + str(C.length()))      # Circle length: 6.283185307179586