# encoding:utf-8
import unittest
from transform import willingnessCalculation,capacityCalculation,FiftyPercent,willingnessFinalCRP,gap,ContradictionFlag,displayColor

class transformTestCase(unittest.TestCase):
    """Test for 'transform.py'"""
    def test_willingnessCalculation(self):
        #Step 1: Test answer str 'Q2=a，Q3=b,Q8=c' for function willingnessCalculation
        self.assertTrue(willingnessCalculation('d','b','c'))
    def test_capacityCalculation(self):
        #Step 2: Test answer str 'Q2=b，Q3=b,Q8=e' for function capacityCalculation
        self.assertTrue(capacityCalculation('b','b','e'))
    def test_FifryPercent(self):
        #Step 3: Test input str '3,3,6' for function FiftyPercent
        self.assertTrue(FiftyPercent('3','3','6'))
    def test_willingnessFinalCRP(self):
        #Step 4: Test input str '3,1' for function willingnessFinalCRP
        self.assertTrue(willingnessFinalCRP('3','1'))
    def test_gap(self):
        #Step 5: Test input int 5,6,6 for function gap
        self.assertTrue(gap(5,6,6))
    def test_ContradictionFlag(self):
        #Step 6: Test input str '1,1,0' for function ContradictionFlag
        self.assertTrue(ContradictionFlag('1','1','0'))
    def test_displayColor(self):
        #Step 7: Test input int 0,0,0 for function displayColor
        self.assertTrue(displayColor(0,0,0))



if __name__ == '__main__':
    unittest.main()
