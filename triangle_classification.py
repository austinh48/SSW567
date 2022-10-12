import unittest

def classify_triangle(a,b,c):
    classification = ''
    #classify as equilateral, isosceles or scalene
    if a == b and b == c:
        classification = 'equilateral'
    elif a == b or b == c or a == c:
        classification = 'isosceles'
    else:
        classification = 'scalene'
    #check if the triangle is valid
    if a + b < c or a + c < b or b + c < a:
        classification = 'not'
    #check if the triangle is a right triangle
    if a**2 + b**2 == c**2:
        classification = 'right'
    if b**2 + c**2 == a**2:
        classification = 'right'
    if a**2 + c**2 == b**2:
        classification = 'right'
    return classification
def run_classify_triangle(a,b,c):
    #commas in ',a, ',', b, ',', c, ' are the same thing as doing ' + a + ',' + b + ',' + c'
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")
class TestTriangles(unittest.TestCase):
    def test_set_1(self):
        self.assertEqual(classify_triangle(3,4,5), 'right', '3,4,5 should be right')
        self.assertEqual(classify_triangle(4,3,5), 'right', '4,3,5 should be right')
        self.assertEqual(classify_triangle(5,4,3), 'right', '5,4,3 should be right')
        self.assertEqual(classify_triangle(3,3,3), 'equilateral', '3,3,3 should be equilateral')
        self.assertEqual(classify_triangle(2,4,6), 'scalene', '2,4,6 should be scalene')
    def test_set_2(self):
        self.assertEqual(classify_triangle(1,1,1),'equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'isoceles','Should be Equilateral')
        self.assertEqual(classify_triangle(10,15,30),'not','Should be Isoceles')
if __name__ == '__main__':
    run_classify_triangle(1,2,3)
    run_classify_triangle(1,1,1)
    unittest.main(exit=True)