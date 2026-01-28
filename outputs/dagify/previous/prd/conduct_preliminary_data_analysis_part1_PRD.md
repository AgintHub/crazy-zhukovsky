# conduct_preliminary_data_analysis_part1 PRD

## Description
Perform initial exploratory analysis to identify upward or downward trends in macroeconomic data using linear regression or growth‑rate calculations.


## Conceptual Info

This node conducts a quick exploratory statistical scan of the macro‑economic time‑series associated with the defined objectives and metrics. It fits simple linear models (or computes period‑to‑period growth rates) for each metric to surface the direction (upward/downward) and magnitude of observable trends, producing a concise list of trend descriptors and their numerical strengths for downstream driver identification.

## Docstring

### Summary
Identify primary upward or downward trends in macroeconomic metrics based on linear regression or growth‑rate calculations.

### Parameters

- **objectives** (List[str]): Primary macroeconomic objectives extracted from the input description (e.g., ['GDP growth', 'inflation control']).
- **metrics** (List[str]): Key performance metrics linked to the objectives (e.g., ['GDP growth rate', 'CPI inflation']).
- **data_frame** (pandas.DataFrame): Time‑series dataframe where each column corresponds to a metric name and rows represent chronological observations.

### Returns

dict: Dictionary with two keys: 'identified_trends' (List[str]) and 'trend_strengths' (List[float]), aligned by index.

### Raises

- ValueError: If either *objectives* or *metrics* is empty, or if required metric columns are missing from *data_frame*.
- RuntimeError: If linear regression fails to converge for a metric.

### Examples

```python
>>> import pandas as pd
>>> df = pd.DataFrame({
...     'GDP growth rate': [2.1, 2.3, 2.5, 2.8, 3.0],
...     'CPI inflation': [1.8, 1.9, 2.0, 2.2, 2.4]
>>> }, index=pd.date_range('2020', periods=5, freq='Y'))
>>> result = conduct_preliminary_data_analysis_part1(
...     objectives=['GDP growth', 'inflation control'],
...     metrics=['GDP growth rate', 'CPI inflation'],
...     data_frame=df
>>> )
>>> print(result)
{'identified_trends': ['upward', 'upward'], 'trend_strengths': [0.225, 0.15]}
```
