from math import sqrt


class Cuboid:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (
            self.width * self.height +
            self.width * self.depth +
            self.height * self.depth
        )


class Pyramid:
    def __init__(self, base_width, base_depth, height):
        self.base_width = base_width
        self.base_depth = base_depth
        self.height = height

    def volume(self):
        return (
            1/3 * self.base_width * self.base_depth * self.height
        )

    def surface_area(self):
        slant_height = sqrt((self.base_width / 2) ** 2 + self.height ** 2)
        base_area = self.base_width * self.base_depth
        lateral_area = 2 * (
            self.base_width * slant_height + self.base_depth * slant_height
        )
        return base_area + lateral_area


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (
            4/3 * 3.14159 * self.radius ** 3
        )

    def surface_area(self):
        return 4 * 3.14159 * self.radius ** 2


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (
            3.14159 * self.radius ** 2 * self.height
        )

    def surface_area(self):
        return (
            2 * 3.14159 * self.radius * (self.radius + self.height)
        )


if __name__ == "__main__":
    cuboid = Cuboid(3, 4, 5)
    print("Cuboid volume:", cuboid.volume())
    print("Cuboid surface area:", cuboid.surface_area())

    pyramid = Pyramid(6, 8, 10)
    print("Pyramid volume:", pyramid.volume())
    print("Pyramid surface area:", pyramid.surface_area())

    sphere = Sphere(7)
    print("Sphere volume:", sphere.volume())
    print("Sphere surface area:", sphere.surface_area())

    cylinder = Cylinder(5, 12)
    print("Cylinder volume:", cylinder.volume())
    print("Cylinder surface area:", cylinder.surface_area())
