import pytest
from pdfExtractor.FileNameManiputlation import FileNameManipulation 
from pdfExtractor.FileNameManipulationImp import FileNameManiputlationImp

class TestAlgorithmSelector:
    def test_bt(self):
        fileNameManipulation:FileNameManipulation = FileNameManiputlationImp()
        output = fileNameManipulation.extractBankName("02/09/2022 -BT - Etats financiers semestriels au 30/06/2022")
        assert output == 'BT' 
        
    def test_biat(self):
        fileNameManipulation:FileNameManipulation = FileNameManiputlationImp()
        output = fileNameManipulation.extractBankName("13/04/2023 -BIAT - Etats financiers annuels consolidés au 31/12/2022")
        assert output == 'BIAT' 

    if __name__ == '__main__':
        pytest.main()

