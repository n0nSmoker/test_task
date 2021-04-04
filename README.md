# FileMerger
Merges multiple files in one

**Contents**
- [Usage](#Usage)
- [Tests](#Tests)

## Usage
```bash
python src/run.py tests/data/bank1.csv tests/data/bank2.csv tests/data/bank3.csv
```
Also see `tests/test_csv_file_saver.py` for examples of usage


# Tests
To run tests and see tests coverage report just type the following command:(doker and doker-compose should be installed on you local machine)
```bash
make test
```
To run a particular test use
```bash
make test file=tests/some_file.py
make test file=tests/some_file.py::test_func
```
