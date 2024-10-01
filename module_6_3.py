class Horse:
    s1 = ""

    def __init__(self, x_distance1=0, y_distance1=0, sound1='Frrr'):
        self.x_distance = x_distance1
        self.sound = sound1
        Horse.s1 = sound1
        super().__init__(y_distance1)

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    s2 = ""

    def __init__(self, y_distance1=0, sound2='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance1
        self.sound = sound2
        Eagle.s2 = sound2

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    # s3=Horse.s1+Eagle.s2
    def __init__(self, x_distance1=0, y_distance1=0):
        super().__init__(x_distance1, y_distance1)
        self.sound = Horse.s1 + ", " + Eagle.s2

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()