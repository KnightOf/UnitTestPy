from types import ClassMethodDescriptorType
import unittest
import numpy as np
import cv2

class Functions():
    def Add(a , b ):
        return a+b
    def Sub(a , b ):
        return a-b
    def isPointInCircleRange(Point , Center , Radius):
        return (Center[0]-Point[0])*(Center[0]-Point[0]) + (Center[1]-Point[1])*(Center[1]-Point[1]) <= Radius*Radius

class TestBoolMethods(unittest.TestCase):
    def test_isPointInCircleRange_returnTrue(self):
        return self.assertTrue(Functions.isPointInCircleRange((3,3),(2,2),2))

class TestStringMethods(unittest.TestCase):

    def test_UpperCase(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isUpperCase(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestIntegerMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Functions.Add(3,5),8)
    def test_sub(self):
        self.assertEqual(Functions.Sub(3,5),-2)


if __name__ == '__main__':
    unittest.main()
