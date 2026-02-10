# Virtual Column Generator

## Project Description

This project implements the `add_virtual_column()` function, which allows adding new columns to a DataFrame based on arithmetic rules. The function supports the following operations:
- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (*)

The function validates column names (letters and underscores only) and checks if the specified columns exist in the DataFrame.

## Requirements

- Python 3.7+
- pandas
- pytest (for running tests)

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

### From terminal (pytest)
```bash
pytest test_virtual_column.py -v
```

### Manual test execution
```bash
python test_virtual_column.py
```

### In Jupyter Notebook
```python
import pytest
pytest.main(['-v', 'test_virtual_column.py'])
```

## Usage

```python
import pandas as pd
from solution import add_virtual_column

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Add a new column as the sum of A and B
df = add_virtual_column(df, 'A + B', 'C')
print(df)
```

## File Structure

```
├── solution.py              # Main add_virtual_column() function
├── test_virtual_column.py   # Function tests
├── tests.ipynb              # Jupyter notebook with tests
├── requirements.txt         # Project dependencies
├── .gitignore              # Files ignored by git
└── README.md               # This file
```

## Validation

The function returns an empty DataFrame when:
- The new column name contains characters other than letters and underscores
- The column name in the rule contains characters other than letters and underscores
- A specified column does not exist in the DataFrame
- The rule contains an invalid operator
