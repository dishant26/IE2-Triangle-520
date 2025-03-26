import unittest
from isTriangle import Triangle

class TestTriangleDecisionCoverage(unittest.TestCase):
    
    def test_negative_sides(self):
        # Test with negative side values (covers 'if a <= 0 or b <= 0 or c <= 0:' = TRUE)
        result1 = Triangle.classify(-1, 2, 3)
        self.assertEqual(result1, Triangle.Type.INVALID)
        result2 = Triangle.classify(1, -2, 3)
        self.assertEqual(result2, Triangle.Type.INVALID)
        result3 = Triangle.classify(1, 2, -3)
        self.assertEqual(result3, Triangle.Type.INVALID)

    def test_zero_sides(self):
        # Test with zero side values (also covers 'if a <= 0 or b <= 0 or c <= 0:' = TRUE)
        result1 = Triangle.classify(0, 2, 3)
        self.assertEqual(result1, Triangle.Type.INVALID)
        result2 = Triangle.classify(1, 0, 3)
        self.assertEqual(result2, Triangle.Type.INVALID)
        result3 = Triangle.classify(1, 2, 0)
        self.assertEqual(result3, Triangle.Type.INVALID)

    def test_valid_positive_sides(self):
        # Test with all positive sides (covers 'if a <= 0 or b <= 0 or c <= 0:' = FALSE)
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)
        
    def test_a_equals_b(self):
        # Test with a == b (covers 'if a == b:' = TRUE)
        result = Triangle.classify(5, 5, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_a_not_equals_b(self):
        # Test with a != b (covers 'if a == b:' = FALSE)
        result = Triangle.classify(5, 6, 7)
        self.assertEqual(result, Triangle.Type.SCALENE)
        
    def test_a_equals_c(self):
        # Test with a == c (covers 'if a == c:' = TRUE)
        result = Triangle.classify(5, 3, 5)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_a_not_equals_c(self):
        # Test with a != c (covers 'if a == c:' = FALSE)
        result = Triangle.classify(5, 6, 7)
        self.assertEqual(result, Triangle.Type.SCALENE)
        
    def test_b_equals_c(self):
        # Test with b == c (covers 'if b == c:' = TRUE)
        result = Triangle.classify(3, 5, 5)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_b_not_equals_c(self):
        # Test with b != c (covers 'if b == c:' = FALSE)
        result = Triangle.classify(5, 6, 7)
        self.assertEqual(result, Triangle.Type.SCALENE)
        
    def test_trian_equals_zero_valid(self):
        # Test with trian == 0 and valid triangle (covers 'if trian == 0:' = TRUE and inner triangle inequality = FALSE)
        result = Triangle.classify(5, 6, 7)
        self.assertEqual(result, Triangle.Type.SCALENE)
        
    def test_trian_equals_zero_invalid(self):
        # Test with trian == 0 and invalid triangle (covers 'if trian == 0:' = TRUE and inner triangle inequality = TRUE)
        result1 = Triangle.classify(1, 2, 3)  # a + b = c
        self.assertEqual(result1, Triangle.Type.INVALID)
        result2 = Triangle.classify(1, 3, 2)  # a + c = b
        self.assertEqual(result2, Triangle.Type.INVALID)
        result3 = Triangle.classify(3, 1, 2)  # b + c = a
        self.assertEqual(result3, Triangle.Type.INVALID)
        
    def test_trian_greater_than_three(self):
        # Test with trian > 3 (covers 'if trian > 3:' = TRUE)
        result = Triangle.classify(5, 5, 5)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)
        
    def test_trian_not_greater_than_three(self):
        # Test with trian <= 3 (covers 'if trian > 3:' = FALSE)
        result = Triangle.classify(5, 5, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_trian_equals_one(self):
        # Test with trian == 1 and valid triangle (covers 'if trian == 1 and a + b > c:' = TRUE)
        result = Triangle.classify(5, 5, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_trian_equals_two(self):
        # Test with trian == 2 and valid triangle (covers 'if trian == 2 and a + c > b:' = TRUE)
        result = Triangle.classify(5, 3, 5)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_trian_equals_three(self):
        # Test with trian == 3 and valid triangle (covers 'if trian == 3 and b + c > a:' = TRUE)
        result = Triangle.classify(3, 5, 5)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
    def test_trian_isoceles_invalid(self):
        # Testing edge cases for isosceles triangles that don't satisfy the triangle inequality
        # This will cover the FALSE branches of the remaining conditional statements
        # These are harder to construct but might be necessary for full branch coverage
        result1 = Triangle.classify(1, 1, 3)  # a == b, but a + b <= c
        self.assertEqual(result1, Triangle.Type.INVALID)
        result2 = Triangle.classify(3, 1, 1)  # b == c, but b + c <= a
        self.assertEqual(result2, Triangle.Type.INVALID)
        result3 = Triangle.classify(1, 3, 1)  # a == c, but a + c <= b
        self.assertEqual(result3, Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()