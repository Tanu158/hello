class point(): #declaring the class
    def __init__(self,x,y):
        print(x,y)
        self.x = x
        self.y=y

    

obj = point(2, 3)
print(obj.x)
print(obj.y)


class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passanger =[]

    def add_passenger(self, name):
        if  not self.open_seats():
            return False
        self.passanger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passanger)


    

flight =flight(3)
people =['mona',"shona","tanu" ,"mona"]
for i in people:
   
    if flight.add_passenger(i):
        print(f"added{i} to flight")
    else:
        print("no seats avalible ")