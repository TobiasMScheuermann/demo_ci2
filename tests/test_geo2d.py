"""Unit tests for geo2d module."""
import unittest
import sys
import os
from math import sqrt

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from demo_ci.geo2d import Rectangle, Triangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_initialization(self):
        """Test Rectangle initialization with valid parameters."""
        rect = Rectangle(5, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)

    def test_rectangle_area(self):
        """Test Rectangle area calculation."""
        rect = Rectangle(5, 3)
        expected_area = 5 * 3  # Following the original implementation
        self.assertEqual(rect.area(), expected_area)

        # Test with different dimensions
        rect2 = Rectangle(10, 4)
        expected_area2 = 10 * 4
        self.assertEqual(rect2.area(), expected_area2)

        # Test with decimal values
        rect3 = Rectangle(2.5, 4.0)
        expected_area3 = 2.5 * 4.0
        self.assertEqual(rect3.area(), expected_area3)

    def test_rectangle_perimeter(self):
        """Test Rectangle perimeter calculation."""
        rect = Rectangle(5, 3)
        expected_perimeter = 2 * (5 + 3)
        self.assertEqual(rect.perimeter(), expected_perimeter)

        # Test with different dimensions
        rect2 = Rectangle(10, 4)
        expected_perimeter2 = 2 * (10 + 4)
        self.assertEqual(rect2.perimeter(), expected_perimeter2)

        # Test with decimal values
        rect3 = Rectangle(2.5, 4.0)
        expected_perimeter3 = 2 * (2.5 + 4.0)
        self.assertEqual(rect3.perimeter(), expected_perimeter3)

    def test_rectangle_edge_cases(self):
        """Test Rectangle with edge cases."""
        # Test with zero dimensions
        rect_zero = Rectangle(0, 5)
        self.assertEqual(rect_zero.area(), 0)
        self.assertEqual(rect_zero.perimeter(), 10)

        # Test with very small dimensions
        rect_small = Rectangle(0.01, 0.02)
        self.assertAlmostEqual(rect_small.area(), 0.01 * 0.02 * 2, places=5)
        expected_perimeter = 2 * (0.01 + 0.02)
        self.assertAlmostEqual(rect_small.perimeter(), expected_perimeter,
                               places=5)


class TestTriangle(unittest.TestCase):
    """Test cases for the Triangle class."""

    def test_triangle_initialization(self):
        """Test Triangle initialization with valid parameters."""
        tri = Triangle(3, 4, 5)
        self.assertEqual(tri.a, 3)
        self.assertEqual(tri.b, 4)
        self.assertEqual(tri.c, 5)

    def test_triangle_area_right_triangle(self):
        """Test Triangle area calculation for a right triangle (3-4-5)."""
        tri = Triangle(3, 4, 5)
        # For a 3-4-5 right triangle, area should be 6
        expected_area = 6.0
        self.assertAlmostEqual(tri.area(), expected_area, places=5)

    def test_triangle_area_equilateral(self):
        """Test Triangle area calculation for an equilateral triangle."""
        tri = Triangle(6, 6, 6)
        # For equilateral triangle with side 6: area = 9*sqrt(3)
        expected_area = 9 * sqrt(3)
        self.assertAlmostEqual(tri.area(), expected_area, places=5)

    def test_triangle_area_isosceles(self):
        """Test Triangle area calculation for an isosceles triangle."""
        tri = Triangle(5, 5, 8)
        # Using Heron's formula: s = 9, area = sqrt(9 * 4 * 4 * 1) = 12
        expected_area = 12.0
        self.assertAlmostEqual(tri.area(), expected_area, places=5)

    def test_triangle_perimeter(self):
        """Test Triangle perimeter calculation."""
        tri = Triangle(3, 4, 5)
        expected_perimeter = 3 + 4 + 5
        self.assertEqual(tri.perimeter(), expected_perimeter)

        # Test with different dimensions
        tri2 = Triangle(6, 8, 10)
        expected_perimeter2 = 6 + 8 + 10
        self.assertEqual(tri2.perimeter(), expected_perimeter2)

        # Test with decimal values
        tri3 = Triangle(2.5, 3.5, 4.0)
        expected_perimeter3 = 2.5 + 3.5 + 4.0
        self.assertEqual(tri3.perimeter(), expected_perimeter3)

    def test_triangle_area_small_values(self):
        """Test Triangle area calculation with small values."""
        tri = Triangle(0.3, 0.4, 0.5)
        # This is a scaled version of 3-4-5 triangle
        expected_area = 0.06  # (0.3 * 0.4) / 2
        self.assertAlmostEqual(tri.area(), expected_area, places=5)

    def test_triangle_invalid_triangle_degenerate(self):
        """Test Triangle with degenerate case (collinear points)."""
        # Triangle with sides 1, 2, 3 (degenerate case)
        tri = Triangle(1, 2, 3)
        # Area should be 0 for degenerate triangle
        self.assertAlmostEqual(tri.area(), 0.0, places=5)


if __name__ == '__main__':
    unittest.main()
