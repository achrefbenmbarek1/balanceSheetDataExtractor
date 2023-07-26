import pytest
from pdfExtractor.FileLinkManipulator import FileLinkManipulator 
from pdfExtractor.FileLinkManipulatorImp import FileLinkManipulatorImp

class testalgorithmselector:
    def test_bt(self):
        fileLinkManipulator:FileLinkManipulator = FileLinkManipulatorImp()
        output = fileLinkManipulator.extractBankName("02/09/2022 -bt - etats financiers semestriels au 30/06/2022")
        assert output == 'bt' 
        
    def test_biat(self):
        fileLinkManipulator:FileLinkManipulator = FileLinkManipulatorImp()
        output = fileLinkManipulator.extractBankName("13/04/2023 -biat - etats financiers annuels consolidés au 31/12/2022")
        assert output == 'biat' 

    if __name__ == '__main__':
        pytest.main()


