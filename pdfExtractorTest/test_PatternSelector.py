import pytest
from pdfExtractor.PatternSelector import PatternSelector 

class TestAlgorithmSelector:
    def test_bt(self):
        patternSelector:PatternSelector = PatternSelector()
        output = patternSelector.selectPattern('BT')
        assert output == [ "Total PA3", "Total AC3", "Total PR1", "Total PR2", "Total PR3", "Total PR4", "Total CH 1", "Total CH2", "Total PR7", "Total CH6", "Total CH7", "Total PR5", "Total PR6" ]

        
    def test_biat(self):
        patternSelector:PatternSelector = PatternSelector()
        output = patternSelector.selectPattern('BIAT')
        assert output == [ "PA3", "AC3", "PR1", "PR2", "PR3", "PR4", "CH 1", "CH2", "PR7", "CH6", "CH7", "PR5", "PR6" ]

    if __name__ == '__main__':
        pytest.main()


