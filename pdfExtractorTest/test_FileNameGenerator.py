import pytest
from pdfExtractor.FileLinkManipulator import FileLinkManipulator
from pdfExtractor.FileLinkManipulatorImp import FileLinkManipulatorImp

class TestFileNameGenerator:
    def test_bt(self):
        fileNameManipulation:FileLinkManipulator = FileLinkManipulatorImp()
        output = fileNameManipulation.generateFileUrl("14/04/2023 -BT - Etats financiers annuels individuels au 31/12/2022")
        assert output == 'http://www.bvmt.com.tn/sites/default/files/societes/bt/etats-financiers/bt-etats-financiers-annuels-individuels-31-12-2022.pdf' 
        
    def test_biat(self):
        fileNameManipulation:FileLinkManipulator = FileLinkManipulatorImp()
        output = fileNameManipulation.generateFileUrl("13/04/2023 -BIAT - Etats financiers annuels individuels au 31/12/2022")
        assert output == 'http://www.bvmt.com.tn/sites/default/files/societes/biat/etats-financiers/biat-etats-financiers-annuels-individuels-31-12-2022.pdf' 

    if __name__ == '__main__':
        pytest.main()

