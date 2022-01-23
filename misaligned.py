
def print_color_map():
    textFilePrint = open("PrintedColorMapManual.txt",'w')
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            textToBePrinted = f'{i * 5 + j} | {major} | {minor}'
            print(textToBePrinted)
            textFilePrint.write(textToBePrinted + '\n')
    textFilePrint.close()
    return len(major_colors) * len(minor_colors)


import unittest
class colorMapManualTester(unittest.TestCase):
    ColorMapPrintedManual = open("PrintedColorMapManual.txt",'r')
    ColorMapPrintedManualText = ColorMapPrintedManual.readlines()
    result = print_color_map()
    def test_color_map_manual_length(self):
        self.assertEqual(self.result,len(self.ColorMapPrintedManualText))

    def test_color_map_manual_index(self):
        testIndex = 0
        for color_map_manual_index in range(len(self.ColorMapPrintedManualText)):
            self.assertEqual(int(self.ColorMapPrintedManualText[color_map_manual_index].split("|")[0].strip()),testIndex)
            testIndex +=1
    
    def test_color_map_manual_alignment(self):
        max_alignmnet_expected = len(str(self.result)) +1
        for color_map_manual_index in range(len(self.ColorMapPrintedManualText)):
            self.assertEqual(int(len(self.ColorMapPrintedManualText[color_map_manual_index].split("|")[0])),max_alignmnet_expected)
        
if __name__ == "__main__":
    unittest.main()
    colorMapManualTester.ColorMapPrintedManual.close()

print("All is well (maybe!)\n")