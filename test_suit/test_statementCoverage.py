import unittest
from isTriangle import Triangle

class TestTriangleStatementCoverage(unittest.TestCase):
    
    def test_negative_sides(self):
        # Test negative sides - should return INVALID
        result1 = Triangle.classify(-1, 2, 3)
        self.assertEqual(result1, Triangle.Type.INVALID)
        result2 = Triangle.classify(1, -2, 3)
        self.assertEqual(result2, Triangle.Type.INVALID)
        result3 = Triangle.classify(1, 2, -3)
        self.assertEqual(result3, Triangle.Type.INVALID)
        
    def test_zero_sides(self):
        # Test zero sides - should return INVALID
        result1 = Triangle.classify(0, 2, 3)
        self.assertEqual(result1, Triangle.Type.INVALID)
        result2 = Triangle.classify(1, 0, 3)
        self.assertEqual(result2, Triangle.Type.INVALID)
        result3 = Triangle.classify(1, 2, 0)
        self.assertEqual(result3, Triangle.Type.INVALID)
    
    def test_equilateral(self):
        # Test equilateral triangle - all sides equal
        result = Triangle.classify(5, 5, 5)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)
        
    def test_isosceles(self):
        # Test isosceles triangle - two sides equal
        # Case where a == b
        result1 = Triangle.classify(5, 5, 3)
        self.assertEqual(result1, Triangle.Type.ISOSCELES)
        # Case where a == c
        result2 = Triangle.classify(5, 3, 5)
        self.assertEqual(result2, Triangle.Type.ISOSCELES)
        # Case where b == c
        result3 = Triangle.classify(3, 5, 5)
        self.assertEqual(result3, Triangle.Type.ISOSCELES)
        
    def test_scalene(self):
        # Test scalene triangle - all sides different
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)
        
    def test_invalid_triangles(self):
        # Test invalid triangles - sides violate triangle inequality
        # a + b <= c
        result1 = Triangle.classify(1, 2, 3)
        self.assertEqual(result1, Triangle.Type.INVALID)
        # a + c <= b
        result2 = Triangle.classify(1, 3, 2)
        self.assertEqual(result2, Triangle.Type.INVALID)
        # b + c <= a
        result3 = Triangle.classify(3, 1, 2)
        self.assertEqual(result3, Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()
