import pytest
from pdfExtractor.DefaultDataFormatter import DefaultDataFormatter
from pdfExtractor.DataFormatter import DataFormatter

class TestDefaultDataFormatter:
    def test_bt_millions(self):
        dataFormatter:DataFormatter = DefaultDataFormatter()
        output = dataFormatter.format("PA3 - Dépôts de la clientèle 3.3 5 305 679 4 634 053")
        assert output == 'PA3 - Dépôts de la clientèle 3.3,5 305 679,4 634 053' 
        
    def test_bt_thousands(self):
        dataFormatter:DataFormatter = DefaultDataFormatter()
        output = dataFormatter.format("CH7 - Charges générales d'exploitation 5.11 37 430 33 031")
        assert output == "CH7 - Charges générales d'exploitation 5.11,37 430,33 031" 
        

   
    if __name__ == '__main__':
        pytest.main()

