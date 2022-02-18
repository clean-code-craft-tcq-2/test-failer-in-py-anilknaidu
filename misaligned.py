
def print_color_map():
    textFilePrint = open("PrintedColorMapManual.txt",'w')
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    max_alignment_numbers = len(str(len(major_colors) * len(minor_colors))) + 1
    max_alignment_major_color = len(max(major_colors, key=len))+1
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            alignmentSpaces_numbers = " "*(max_alignment_numbers -len(str(i * 5 + j+1)))
            alignmentSpaces_majorColor = " "*(max_alignment_major_color -len(major))
            textToBePrinted = f'{i * 5 + j +1}'+alignmentSpaces_numbers + f'| {major}' + alignmentSpaces_majorColor + f'| {minor}'
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
        testPairNumber = 1
        for color_map_manual_index in range(len(self.ColorMapPrintedManualText)):
            self.assertEqual(int(self.ColorMapPrintedManualText[color_map_manual_index].split("|")[0].strip()),testPairNumber)
            testPairNumber +=1
    
    def test_color_map_manual_alignment(self):
        max_alignment_expected = len(str(self.result)) +1
        for color_map_manual_index in range(len(self.ColorMapPrintedManualText)):
            self.assertEqual(int(len(self.ColorMapPrintedManualText[color_map_manual_index].split("|")[0])),max_alignment_expected)
        
if __name__ == "__main__":
    unittest.main()
    colorMapManualTester.ColorMapPrintedManual.close()

print("All is well (maybe!)\n")