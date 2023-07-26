import pytest
from pdfExtractor.FileLinksExtractor import FileLinksExtractor
from pdfExtractor.FileLinksExtractorImp import FileLinksExtractorImp
from pdfExtractor.FileLinkManipulator import FileLinkManipulator
from pdfExtractor.FileLinkManipulatorImp import FileLinkManipulatorImp

class TestFileNamesExtractor:
    def test_bt(self):
        fileLinkManipulator:FileLinkManipulator = FileLinkManipulatorImp()
        fileLinksExtractor:FileLinksExtractor = FileLinksExtractorImp(fileLinkManipulator)
        output = fileLinksExtractor.extractFileLinks()
        print(output)
        assert output["BT"] == [' -BT - Etats financiers annuels individuels  au 31/12/2022', ' -BT - Etats financiers annuels individuels  au 31/12/2021', ' -BT - Etats financiers annuels individuels  au 31/12/2020']
        
    def test_atb(self):
        fileNameManipulation:FileLinkManipulator = FileLinkManipulatorImp()
        fileNamesExtractor:FileLinksExtractor = FileLinksExtractorImp(fileNameManipulation)
        output = fileNamesExtractor.extractFileLinks()
        assert output["BIAT"] == [' -BIAT - Etats financiers annuels individuels  au 31/12/2022', ' -BIAT - Etats financiers annuels individuels  au 31/12/2021', ' -BIAT - Etats financiers annuels individuels  au 31/12/2020']

    if __name__ == '__main__':
        pytest.main()

