class Rectange:
    length=10
    breadth=5

    def __init__(self,l,b):
        self.length=int(l)
        self.breadth=int(b)

    def Area(self):
        area=self.length*self.breadth
        return print("Area of length {} and breadth {} Rectangle is : {} ".format(self.length,self.breadth,area))
    
    def Perimeter(self):
        perimeter=(2*(int(self.length)+int(self.breadth)))
        return print("Perimenter of length {} and breadth {} of Rectangle : {} ".format(self.length,self.breadth,perimeter))
    

r1=Rectange(10,3)
r1.Area()
r1.Perimeter()


r2=Rectange(7,3)
r2.Area()
r2.Perimeter()
