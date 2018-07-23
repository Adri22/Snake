
class ObjectHandler:
    objects = []

    def __init__(self, canvas):
        self.canvas = canvas

    def add(self, o):
        self.objects.append(o)

    def remove(self, o):
        self.canvas.delete(o.shape)
        self.objects.remove(o)

    def joinList(self, l):
        self.objects += list(set(l) - set(self.objects))
        
    def update(self):
        for object in self.objects:
            object.update()

    def render(self):
        #self.canvas.delete("all")
        for object in self.objects:
            self.canvas.coords(object.shape, 
                object.position[0] * object.size,
                object.position[1] * object.size,
                object.position[0] * object.size + object.size,
                object.position[1] * object.size + object.size)