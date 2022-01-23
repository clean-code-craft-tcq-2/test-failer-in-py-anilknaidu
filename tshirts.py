def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

smallShirtSizeList =range(34,38)
mediumShirtSizeList =range(38,42)
largeShirtSizeList =range(42,46)
shirtSizeTestRange = range(30,50)
#Test Code below
import unittest
class ShirtSizeTester(unittest.TestCase):
    def test_ShirtSize(self):
        print("Executing Shirt Size tests")
        for shirtSize in shirtSizeTestRange:
            if(shirtSize in smallShirtSizeList):
                self.assertEqual(size(shirtSize),'S')
            elif(shirtSize in mediumShirtSizeList):
                self.assertEqual(size(shirtSize),'M')
            elif(shirtSize in largeShirtSizeList):
                self.assertEqual(size(shirtSize),'L')
            else:
                self.assertEqual(size(shirtSize),'InvalidShirtSize')

if __name__ == "__main__":
    unittest.main()
print("All is well (maybe!)\n")
