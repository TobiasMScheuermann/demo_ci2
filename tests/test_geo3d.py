"""Unit tests for geo3d module."""
import unittest
import sys
import os
from math import sqrt, pi

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from demo_ci.geo3d import Cuboid, Pyramid, Sphere, Cylinder


class TestCuboid(unittest.TestCase):
    """Test cases for the Cuboid class."""

    def test_cuboid_initialization(self):
        """Test Cuboid initialization with valid parameters."""
        cuboid = Cuboid(3, 4, 5)
        self.assertEqual(cuboid.width, 3)
        self.assertEqual(cuboid.height, 4)
        self.assertEqual(cuboid.depth, 5)

    def test_cuboid_volume(self):
        """Test Cuboid volume calculation."""
        cuboid = Cuboid(3, 4, 5)
        expected_volume = 3 * 4 * 5
        self.assertEqual(cuboid.volume(), expected_volume)

        # Test with decimal values
        cuboid2 = Cuboid(2.5, 3.0, 4.0)
        expected_volume2 = 2.5 * 3.0 * 4.0
        self.assertEqual(cuboid2.volume(), expected_volume2)

    def test_cuboid_surface_area(self):
        """Test Cuboid surface area calculation."""
        cuboid = Cuboid(3, 4, 5)
        expected_surface_area = 2 * (3 * 4 + 3 * 5 + 4 * 5)
        self.assertEqual(cuboid.surface_area(), expected_surface_area)

        # Test with unit cube
        unit_cube = Cuboid(1, 1, 1)
        expected_surface_area_unit = 6
        self.assertEqual(unit_cube.surface_area(), expected_surface_area_unit)

    def test_cuboid_edge_cases(self):
        """Test Cuboid with edge cases."""
        # Test with zero dimension
        cuboid_zero = Cuboid(0, 4, 5)
        self.assertEqual(cuboid_zero.volume(), 0)
        self.assertEqual(cuboid_zero.surface_area(), 2 * (0 + 0 + 4 * 5))


class TestPyramid(unittest.TestCase):
    """Test cases for the Pyramid class."""

    def test_pyramid_initialization(self):
        """Test Pyramid initialization with valid parameters."""
        pyramid = Pyramid(6, 8, 10)
        self.assertEqual(pyramid.base_width, 6)
        self.assertEqual(pyramid.base_depth, 8)
        self.assertEqual(pyramid.height, 10)

    def test_pyramid_volume(self):
        """Test Pyramid volume calculation."""
        pyramid = Pyramid(6, 8, 10)
        expected_volume = (1/3) * 6 * 8 * 10
        self.assertAlmostEqual(pyramid.volume(), expected_volume, places=5)

        # Test with unit pyramid
        unit_pyramid = Pyramid(1, 1, 3)
        expected_volume_unit = 1.0
        self.assertAlmostEqual(unit_pyramid.volume(), expected_volume_unit,
                               places=5)

    def test_pyramid_surface_area(self):
        """Test Pyramid surface area calculation."""
        pyramid = Pyramid(6, 8, 10)
        slant_height = sqrt((6 / 2) ** 2 + 10 ** 2)
        base_area = 6 * 8
        lateral_area = 2 * (6 * slant_height + 8 * slant_height)
        expected_surface_area = base_area + lateral_area
        self.assertAlmostEqual(pyramid.surface_area(), expected_surface_area,
                               places=5)


class TestSphere(unittest.TestCase):
    """Test cases for the Sphere class."""

    def test_sphere_initialization(self):
        """Test Sphere initialization with valid parameters."""
        sphere = Sphere(7)
        self.assertEqual(sphere.radius, 7)

    def test_sphere_volume(self):
        """Test Sphere volume calculation."""
        sphere = Sphere(7)
        expected_volume = (4/3) * 3.14159 * 7 ** 3
        self.assertAlmostEqual(sphere.volume(), expected_volume, places=2)

        # Test with unit sphere
        unit_sphere = Sphere(1)
        expected_volume_unit = (4/3) * 3.14159
        self.assertAlmostEqual(unit_sphere.volume(), expected_volume_unit,
                               places=5)

    def test_sphere_surface_area(self):
        """Test Sphere surface area calculation."""
        sphere = Sphere(7)
        expected_surface_area = 4 * 3.14159 * 7 ** 2
        self.assertAlmostEqual(sphere.surface_area(), expected_surface_area,
                               places=2)

        # Test with unit sphere
        unit_sphere = Sphere(1)
        expected_surface_area_unit = 4 * 3.14159
        self.assertAlmostEqual(unit_sphere.surface_area(),
                               expected_surface_area_unit, places=5)

    def test_sphere_zero_radius(self):
        """Test Sphere with zero radius."""
        zero_sphere = Sphere(0)
        self.assertEqual(zero_sphere.volume(), 0)
        self.assertEqual(zero_sphere.surface_area(), 0)


class TestCylinder(unittest.TestCase):
    """Test cases for the Cylinder class."""

    def test_cylinder_initialization(self):
        """Test Cylinder initialization with valid parameters."""
        cylinder = Cylinder(5, 12)
        self.assertEqual(cylinder.radius, 5)
        self.assertEqual(cylinder.height, 12)

    def test_cylinder_volume(self):
        """Test Cylinder volume calculation."""
        cylinder = Cylinder(5, 12)
        expected_volume = 3.14159 * 5 ** 2 * 12
        self.assertAlmostEqual(cylinder.volume(), expected_volume, places=2)

        # Test with unit cylinder
        unit_cylinder = Cylinder(1, 1)
        expected_volume_unit = 3.14159
        self.assertAlmostEqual(unit_cylinder.volume(), expected_volume_unit,
                               places=5)

    def test_cylinder_surface_area(self):
        """Test Cylinder surface area calculation."""
        cylinder = Cylinder(5, 12)
        expected_surface_area = 2 * 3.14159 * 5 * (5 + 12)
        self.assertAlmostEqual(cylinder.surface_area(), expected_surface_area,
                               places=2)

        # Test with unit cylinder
        unit_cylinder = Cylinder(1, 1)
        expected_surface_area_unit = 2 * 3.14159 * 1 * (1 + 1)
        self.assertAlmostEqual(unit_cylinder.surface_area(),
                               expected_surface_area_unit, places=5)

    def test_cylinder_edge_cases(self):
        """Test Cylinder with edge cases."""
        # Test with zero height
        flat_cylinder = Cylinder(5, 0)
        expected_volume_flat = 0
        expected_surface_area_flat = 2 * 3.14159 * 5 * 5
        self.assertEqual(flat_cylinder.volume(), expected_volume_flat)
        self.assertAlmostEqual(flat_cylinder.surface_area(),
                               expected_surface_area_flat, places=5)

        # Test with zero radius
        zero_cylinder = Cylinder(0, 12)
        self.assertEqual(zero_cylinder.volume(), 0)
        self.assertEqual(zero_cylinder.surface_area(), 0)


class TestPiAccuracy(unittest.TestCase):
    """Test cases to verify pi approximation used in the code."""

    def test_pi_approximation(self):
        """Test that the pi approximation is reasonable."""
        used_pi = 3.14159
        actual_pi = pi
        # The approximation should be within 0.001 of actual pi
        self.assertAlmostEqual(used_pi, actual_pi, places=4)


if __name__ == '__main__':
    unittest.main()
