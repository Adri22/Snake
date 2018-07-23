
class World:

    def __init__(self, size):
        self.size = size
        self.fields = [[None for x in range(self.size)] for y in range(self.size)]

# CLASS NOT IN USE