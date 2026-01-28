# identify_key_macroeconomic_drivers_part2 PRD

## Description
Determine the direction and strength of relationships between key variables and the target macroeconomic indicator.


## Conceptual Info

This node quantifies how each candidate macroeconomic driver relates to a chosen target indicator by computing statistical correlation (or regression coefficient) and assigning a sign indicating whether the relationship is positive or negative. The results feed downstream econometric models that require both magnitude and direction of drivers.

## Docstring

### Summary
Compute relationship strength and direction between selected macro variables and a target macroeconomic indicator.

### Parameters

- **data** (pandas.DataFrame): Pre‑processed economic dataset where each column is a macroeconomic variable and rows correspond to time periods.
- **key_variables** (List[str]): List of macroeconomic variable names whose relationship to the target indicator should be evaluated.
- **target_indicator** (str): Name of the macroeconomic indicator that serves as the dependent variable (e.g., 'Inflation').

### Returns

Tuple[List[float], List[str]]: A tuple where the first element is a list of numeric relationship strengths (absolute correlation or standardized coefficient) and the second element is a list of strings ('positive' or 'negative') indicating the direction for each key variable, preserving the order of `key_variables`.

### Raises

- KeyError: If any of the `key_variables` or `target_indicator` are not present in `data` columns.
- ValueError: If `key_variables` is empty or contains duplicates.

### Examples

```python
>>> import pandas as pd
>>> data = pd.DataFrame({
...     "GDP_growth": [2.5, 3.0, 2.8, 3.2],
...     "Unemployment": [5.0, 4.8, 5.1, 4.9],
...     "Inflation": [1.8, 2.0, 1.9, 2.1]
>>> })
>>> key_vars = ["GDP_growth", "Unemployment"]
>>> target = "Inflation"
>>> strength, direction = determine_relationships(data, key_vars, target)
>>> print(strength)
>>> print(direction)
[0.97, -0.85]\n['positive', 'negative']
```
