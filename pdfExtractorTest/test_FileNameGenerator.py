import pytest
from pdfExtractor.FileNameManipulationImp import FileNameManiputlationImp
from pdfExtractor.FileNameManiputlation import FileNameManipulation

class TestFileNameGenerator:
    def test_bt(self):
        fileNameManipulation:FileNameManipulation = FileNameManiputlationImp()
        output = fileNameManipulation.generateFileName("14/04/2023 -BT - Etats financiers annuels individuels au 31/12/2022")
        print(output)
        assert output == 'http://www.bvmt.com.tn/sites/default/files/societes/bt/etats-financiers/bt-etats-financiers-annuels-individuels-31-12-2022.pdf' 
        
    def test_biat(self):
        fileNameManipulation:FileNameManipulation = FileNameManiputlationImp()
        output = fileNameManipulation.generateFileName("13/04/2023 -BIAT - Etats financiers annuels individuels au 31/12/2022")
        assert output == 'http://www.bvmt.com.tn/sites/default/files/societes/biat/etats-financiers/biat-etats-financiers-annuels-individuels-31-12-2022.pdf' 

    if __name__ == '__main__':
        pytest.main()

