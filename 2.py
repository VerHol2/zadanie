class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '[{}, {}, {}]'.format(self.x, self.y, self.z)

    def __add__(self, v2):
        return Vector3d(self.x + v2.x, self.y + v2.y, self.z + v2.z)

v1 = Vector3d(-2, 9, 12)
v2 = Vector3d(-5, 5, 10)
v3 = v1 + v2
print(v3)