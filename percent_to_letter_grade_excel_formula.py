#!/usr/bin/env python3
import sys
import os

"""
Create an Excel formula for the following grading table:


| A+  |  A  |  A- |  B+ |  B  |  B- |  C+ |  C  |  C- |  D  |  F  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 97.0%- | 91.0- | 89.5- | 87.0- | 83.0- | 79.5- | 77.0- | 72.0- | 69.5- | 60.0- | Below |
| 100% | 96.9 | 90.9 | 89.4 |  86.9 | 82.9 |  79.4 | 76.9 | 71.9 | 69.4 | 59.9 |

Example:
```
$ ./percent_to_letter_grade_excel_formula.py AE2 | pbcopy
```

Output:
```
IF(AE2>=0.97, "A+",IF(AE2>=0.91, "A",IF(AE2>=0.895, "A-",IF(AE2>=0.87, "B+",IF(AE2>=0.83, "B",IF(AE2>=0.795, "B-",IF(AE2>=0.77, "C+",IF(AE2>=0.72, "C",IF(AE2>=0.695, "C-",IF(AE2>=0.6, "D", "F"))))))))))
```

"""

# Use lower limits of grading grading_table

grading_table = [
    ("A+", 0.97), ("A", 0.91),  ("A-", 0.895),
    ("B+", 0.87),  ("B", 0.83),  ("B-", 0.795),
    ("C+", 0.77),  ("C", 0.72),  ("C-", 0.695),
    ("D", 0.60),  ("F", 0.0),
]

def foo(gt, cell_label: str) -> str:
    """Recursive function to build nested IF expression

    Args:
        gt (Dict[Tuple[str, float]]): Grading Table
        cell_label (str): Cell label in Excel sheet that holds the percentage valaue, e.g. "AE2"

    Returns:
        str: Excel formula for one cell; paste into spreadsheet and fill the remaining rows

    """
    letter, mini = gt[0]
    if letter == 'D':
        return f'IF({cell_label}>={mini}, "{letter}", "F")'
    else:
        car = gt[1:]
        return f'IF({cell_label}>={mini}, "{letter}",' + foo(car, cell_label) + ')'
    

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("Usage: `{} CELL_LABEL`".format(os.path.basename(__file__)))
    else:
        cell_label = sys.argv[1]
        print(foo(grading_table, cell_label))

