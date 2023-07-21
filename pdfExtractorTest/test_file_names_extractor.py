import pytest
from pdfExtractor.FileNamesExtractor import FileNamesExtractor
from pdfExtractor.FileNameManiputlation import FileNameManipulation
from pdfExtractor.FileNameManipulationImp import FileNameManiputlationImp

class TestFileNamesExtractor:
    def test_bt(self):
        fileNameManipulation:FileNameManipulation = FileNameManiputlationImp()
        fileNamesExtractor:FileNamesExtractor = FileNamesExtractor(fileNameManipulation)
        output = fileNamesExtractor.extractFileNames()
        print(output)
        assert output["BT"] == [' -BT - Etats financiers annuels individuels  au 31/12/2022 ', ' -BT - Etats financiers annuels individuels  au 31/12/2021 ', ' -BT - Etats financiers annuels individuels  au 31/12/2020 ']
        
    def test_atb(self):
        fileNamesManipulation:FileNameManipulation = FileNameManiputlationImp()
        fileNamesExtractor:FileNamesExtractor = FileNamesExtractor(fileNamesManipulation)
        output = fileNamesExtractor.extractFileNames()
        assert output["BIAT"] == [' -BIAT - Etats financiers annuels individuels  au 31/12/2022 ', ' -BIAT - Etats financiers annuels individuels  au 31/12/2021 ', ' -BIAT - Etats financiers annuels individuels  au 31/12/2020 ']

    if __name__ == '__main__':
        pytest.main()

