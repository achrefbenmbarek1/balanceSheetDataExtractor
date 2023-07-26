import pytest
from pdfExtractor.PatternSelector import PatternSelector 

class TestPatternSelector:
    def test_bt(self):
        patternSelector:PatternSelector = PatternSelector()
        output = patternSelector.selectPattern('BT')
        assert output == [ "PA3", "AC3", "PR1", "PR2", "PR3", "PR4", "CH1", "CH2", "PR7", "CH6", "CH7", "PR5", "PR6" ]

        
    def test_biat(self):
        patternSelector:PatternSelector = PatternSelector()
        output = patternSelector.selectPattern('BIAT')
        assert output == [ "III-3", "IV-3", "VII-1-1", "VII-1-2", "VII-1-3", "VII-1-4", "VII-2-1", "VII-2-2", "VII-3", "VII-4", "VII-5", "VII-6", "VII-7" ]

    if __name__ == '__main__':
        pytest.main()


