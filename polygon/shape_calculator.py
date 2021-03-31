class Rectangle:

    def __init__(self, wd, ht):
        self.width = int(wd)
        self.height = int(ht)
    
    def set_width(self, wd):
        self.width = int(wd)

    def set_height(self, ht):
        self.height = int(ht)

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = ( self.width ** 2 + self.height ** 2 ) ** 0.5 
        return diagonal
    
    def get_picture(self):
        ht = self.height
        wd = self.width
        AST = '*'
        picture = ''
        errmsg = 'Too big for picture'

        if wd > 50 or ht > 50: return errmsg

        for _ in range(ht):
            for char in range(wd):
                picture += AST
            picture += '\n'
        return picture

    def __str__(self):
        width = self.width
        height = self.height
        inststr = "Rectangle(width={}, height={})".format(width, height)
        return inststr


class Square(Rectangle):
    
    def __init__(self, sd):
        sd = int(sd)
        self.width = sd
        self.height = sd
        self.side = sd

    def set_side(self, sd):
        sd = int(sd)
        self.width = sd
        self.height = sd
        self.side = sd

    def __str__(self):
        side = self.side
        inststr = "Square(side={})".format(side)

    def set_width(self, sd):
        sd = int(sd)
        self.width = sd
        self.height = sd
        self.side = sd

    def set_height(self, sd):
        sd = int(sd)
        self.width = sd
        self.height = sd
        self.side = sd
