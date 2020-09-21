class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,p1:Point,p2:Point):
        self.p1=p1
        self.p2=p2
    def is_clockwise(self,p:Point):
         x1=self.p2.x - self.p1.x
         x2=p.x-self.p1.x
         y1=self.p2.y-self.p1.y
         y2=p.y-self.p1.y


         return x1*y2-x2*y1<0 #TODO 还是小于0来着？

class Triangle:
    def __init__(self,x:Point,y:Point,z:Point):
        self.x=x
        self.y=y
        self.z=z
    def is_point_in_me(self,p:Point):

        return Line(self.x,self.y).is_clockwise(p) and Line(self.y,self.z).is_clockwise(p) and Line(self.z,self.x).is_clockwise(p)


p1=Point(0,0)
p2=Point(0,100)
p3=Point(100,0)

p4=Point(200,2)

print(Triangle(p1,p2,p3).is_point_in_me(p4))