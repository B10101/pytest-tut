class Shapes:

    def area():
        pass

    def perimeter():
        pass



class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    


    def area(self):
        return self.height * self.width
        
    
    def perimeter(self):
        return 2 * self.height + 2* self.width
    


