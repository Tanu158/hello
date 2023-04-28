class point(): #declaring the class
    def __init__(self,x,y):
        print(x,y)
        self.x = x
        self.y=y

    

obj = point(2, 3)
print(obj.x)
print(obj.y)

