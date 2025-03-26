import unittest
from isTriangle import Triangle

class TestTriangleMutationAdequate(unittest.TestCase):
    
    # Enhanced test cases for operator boundary mutations
    def test_invalid_inputs(self):
        # Test all permutations of negative/zero inputs
        self.assertEqual(Triangle.classify(-1, 2, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, -1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 2, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 2, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 0, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 2, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0.0, 0.0, 0.0), Triangle.Type.INVALID)

    def test_equilateral_mutations(self):
        # Tests that would fail if equality checks are mutated
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(5.0, 5.0, 5.0), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(5, 5, 5.0000001), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(999, 999, 999), Triangle.Type.EQUILATERAL)

    def test_isosceles_mutations(self):
        # Tests for all isosceles permutations with edge cases
        self.assertEqual(Triangle.classify(5, 5, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 3, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 5, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 2, 3.9999999), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 2, 4.0000001), Triangle.Type.INVALID)
        
        # These test specific trian values and inequality checks
        self.assertEqual(Triangle.classify(10, 10, 1), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(10, 1, 10), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(1, 10, 10), Triangle.Type.ISOSCELES)

    def test_scalene_mutations(self):
        # Tests that would fail if inequality checks are mutated
        # These should be well within the triangle inequality theorem
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)  # Classic 3-4-5 triangle
        self.assertEqual(Triangle.classify(7, 9, 12), Triangle.Type.SCALENE)  # Larger values
        self.assertEqual(Triangle.classify(5, 12, 13), Triangle.Type.SCALENE)  # 5-12-13 triangle
        
        # Tests for triangle inequality violations
        self.assertEqual(Triangle.classify(1, 2, 4), Triangle.Type.INVALID)  # a + b <= c
        self.assertEqual(Triangle.classify(1, 3, 5), Triangle.Type.INVALID)  # a + b <= c
        self.assertEqual(Triangle.classify(1, 8, 3), Triangle.Type.INVALID)  # b > a + c
        self.assertEqual(Triangle.classify(8, 2, 3), Triangle.Type.INVALID)  # a > b + c
        self.assertEqual(Triangle.classify(2, 8, 3), Triangle.Type.INVALID)  # b > a + c
        self.assertEqual(Triangle.classify(8, 3, 2), Triangle.Type.INVALID)  # a > b + c

    def test_triangle_inequality_mutations(self):
        # Boundary cases for a + b <= c mutations
        self.assertEqual(Triangle.classify(1, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 1.9999999), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(1, 1, 2.0000001), Triangle.Type.INVALID)
        
        # Test exact boundaries for triangle inequality
        self.assertEqual(Triangle.classify(3, 4, 7), Triangle.Type.INVALID)  # a + b == c
        self.assertEqual(Triangle.classify(4, 3, 7), Triangle.Type.INVALID)  # a + b == c
        self.assertEqual(Triangle.classify(3, 7, 4), Triangle.Type.INVALID)  # b + c == a
        self.assertEqual(Triangle.classify(7, 3, 4), Triangle.Type.INVALID)  # a + c == b
        self.assertEqual(Triangle.classify(4, 7, 3), Triangle.Type.INVALID)  # b + c == a
        self.assertEqual(Triangle.classify(7, 4, 3), Triangle.Type.INVALID)  # a + c == b

    def test_trian_counter_mutations(self):
        # Tests for trian counter arithmetic mutations
        self.assertEqual(Triangle.classify(5, 5, 6), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 6, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(6, 5, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)
        
        # Test cases for arithmetic operator replacement in trian calculations
        self.assertEqual(Triangle.classify(5, 5, 7), Triangle.Type.ISOSCELES)  # trian = 1
        self.assertEqual(Triangle.classify(5, 7, 5), Triangle.Type.ISOSCELES)  # trian = 2
        self.assertEqual(Triangle.classify(7, 5, 5), Triangle.Type.ISOSCELES)  # trian = 3
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)  # trian = 6

    def test_operator_edge_cases(self):
        # Tests for operator mutations (>, <, ==, etc.)
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 3, 4), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(4, 5, 6), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)
        
        # Additional borderline cases
        self.assertEqual(Triangle.classify(4, 4, 7.999), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(4, 4, 8.001), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 3, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 3, 4.999), Triangle.Type.SCALENE)

    def test_trian_counter_logic(self):
        # Directly test trian counter arithmetic and comparison mutations
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)  # trian=1
        self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)  # trian=2
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)  # trian=3
        self.assertEqual(Triangle.classify(2, 2, 2), Triangle.Type.EQUILATERAL)  # trian=6
        
        # Test trian > 3 condition
        self.assertEqual(Triangle.classify(4, 4, 4), Triangle.Type.EQUILATERAL)  # trian > 3
        self.assertEqual(Triangle.classify(4, 4, 3), Triangle.Type.ISOSCELES)  # trian = 1

    def test_inequality_operator_mutations(self):
        # Target the a + b <= c checks specifically with precise values
        self.assertEqual(Triangle.classify(3, 3, 5.999), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 3, 6.001), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, 5, 8.999), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(4, 5, 9.001), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, 5, 9), Triangle.Type.INVALID)  # Exactly a + b = c
        
        # Test boundary of each inequality condition
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)  # a + b = c
        self.assertEqual(Triangle.classify(3, 1, 2), Triangle.Type.INVALID)  # a + c = b
        self.assertEqual(Triangle.classify(2, 3, 1), Triangle.Type.INVALID)  # b + c = a
        
        # Specific tests for close to the boundary values
        self.assertEqual(Triangle.classify(3, 4, 6.99), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(3, 6.99, 4), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(6.99, 3, 4), Triangle.Type.SCALENE)

if __name__ == '__main__':
    unittest.main()