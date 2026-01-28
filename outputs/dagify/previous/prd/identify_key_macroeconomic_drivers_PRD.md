# identify_key_macroeconomic_drivers PRD

## Description
Determine the most influential macroeconomic variables and the nature of their relationships with a target macroeconomic indicator.


## Conceptual Info

This node identifies the most critical macroeconomic drivers by analyzing processed data and visual relationships, producing a ranked list of variables with quantified importance and directional associations for downstream econometric modeling.

## Docstring

### Summary
Identify key macroeconomic drivers and their relationships with the target indicator.

### Parameters

- **data** (pd.DataFrame): Preprocessed macroeconomic time‑series data obtained from collect_economic_data. Columns represent potential drivers and the target indicator.
- **potential_drivers** (List[str]): List of variable names identified by identify_potential_macroeconomic_drivers.
- **target_indicator** (str): Column name of the macroeconomic indicator to be forecasted (e.g., 'GDP_growth').

### Returns

Dict[str, List[Union[str, float]]]: Dictionary containing four lists: key_variables, importance_scores, relationship_strength, and relationship_direction.

### Raises

- ValueError: Raised if target_indicator is not in data columns or potential_drivers is empty.
- RuntimeError: Raised if correlation analysis fails due to insufficient data points.

### Examples

```python
>>> import pandas as pd
>>> # Sample data frame
>>> df = pd.DataFrame({
...     'GDP_growth': [2.5, 2.7, 3.0, 2.9, 3.2],
...     'Inflation': [1.2, 1.3, 1.1, 1.4, 1.2],
...     'Unemployment': [5.0, 4.8, 4.6, 4.7, 4.5],
...     'Interest_Rate': [0.5, 0.6, 0.4, 0.5, 0.5]
>>> })
>>> # Potential drivers identified earlier
>>> potential = ['Inflation', 'Unemployment', 'Interest_Rate']
>>> # Identify key drivers
>>> result = identify_key_macroeconomic_drivers(df, potential, 'GDP_growth')
>>> print(result['key_variables'])
>>> print(result['importance_scores'])
>>> print(result['relationship_strength'])
>>> print(result['relationship_direction'])
['Unemployment', 'Inflation', 'Interest_Rate']
[0.95, 0.78, 0.65]
[0.92, 0.75, 0.60]
['negative', 'negative', 'positive']
```

```python
>>> # Handling error: target not in data
>>> try:
...     identify_key_macroeconomic_drivers(df, potential, 'NonExistent')
>>> except ValueError as e:
...     print(e)
'target_indicator 'NonExistent' not found in data columns.'
```
