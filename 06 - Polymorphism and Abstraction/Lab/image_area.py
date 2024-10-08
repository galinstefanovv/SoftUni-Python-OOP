class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    # self >= other
    def __gt__(self, other):
        return self.get_area() > other.get_area()

    # self < other
    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    # self <= other
    def __le__(self, other):
        return self.get_area() <= other.get_area()

    # self == other
    def __eq__(self, other):
        return self.get_area() == other.get_area()

    # self != other
    def __ne__(self, other):
        return self.get_area() != other.get_area()