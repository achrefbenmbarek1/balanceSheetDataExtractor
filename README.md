# BalanceSheetDataExtractor


## Getting Started

To use this code, follow the steps below to set up the environment:

### Prerequisites

- Python 3.x

### Clone the Repository

```bash
git https://github.com/achrefbenmbarek1/balanceSheetDataExtractor.git
cd pdfExtractor 
```
### Install the virtual environment

```bash
python3 -m pip install virtualenv
```
### Create a virtual environment

Create a new virtual environment named .venv/pdfScrapping

```bash
python3 -m venv .venv/pdfScrapping
```

### Activate the virtual environment
On macOS and Linux:

```bash
source .venv/pdfScrapping/bin/activate
```
On Windows:
.venv/pdfScrapping\Scripts\activate

### Install dependencies
Once the virtual environment is activated, use the following command to install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

### Running the project
Now that everything is set up, from the root of the project go to the pdfExtractor directory you can run the project using the python3 command:

```bash
cd pdfExtractor
python3 main.py
```
### Running tests
from the root of the project go to pdfExtractorTest directory and run pytest as shown:

```bash
cd pdfExtractorTest
pytest -vv
```
