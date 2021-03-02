class OP:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        s3 = OP(x,y)

        return  s3

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        s3 = OP(x,y)

        return  s3
    
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        s3 = OP(x,y)

        return  s3

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        s3 = OP(x,y)

        return  s3


    
