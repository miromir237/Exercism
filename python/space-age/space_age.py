class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = 31557600
        self.mercury = 0.2408467
        self.venus = 0.61519726
        self.mars = 1.8808158
        self.jupiter = 11.862615
        self.saturn = 29.447498
        self.uranus = 84.016846
        self.neptune = 164.79132

    def on_earth(self):
        return round(self.seconds / self.earth, 2)

    def on_mercury(self):
        return round(self.seconds / (self.earth * self.mercury), 2)

    def on_venus(self):
        return round(self.seconds / (self.earth * self.venus), 2)

    def on_mars(self):
        return round(self.seconds / (self.earth * self.mars), 2)

    def on_jupiter(self):
        return round(self.seconds / (self.earth * self.jupiter), 2)

    def on_saturn(self):
        return round(self.seconds / (self.earth * self.saturn), 2)

    def on_uranus(self):
        return round(self.seconds / (self.earth * self.uranus), 2)
    
    def on_neptune(self):
        return round(self.seconds / (self.earth * self.neptune), 2)
