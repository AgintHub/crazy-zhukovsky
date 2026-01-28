# conduct_trend_analysis_part1 PRD

## Description
Apply statistical methods to determine directional trends and seasonality in time series data.


## Conceptual Info

This node consumes pre‑processed macroeconomic time‑series data and applies statistical techniques such as linear regression and ARIMA modeling to extract the direction of underlying trends, any recurring seasonal patterns, and quantitative measures of trend strength. The results feed downstream econometric models.

## Docstring

### Summary
Identify trend directions, seasonality patterns, and trend magnitudes from a pre‑processed time‑series dataset.

### Parameters

- **time_series** (pandas.DataFrame): Pre‑processed macro‑economic time‑series with a DateTime index and one or more numeric columns.
- **significance_level** (float): Statistical significance threshold (default 0.05) used when testing trend coefficients.

### Returns

dict: Dictionary containing three keys – `trend_directions` (List[str]), `seasonality_patterns` (List[str]), and `trend_magnitudes` (List[float]) – matching the node's output_structure.

### Raises

- ValueError: If `time_series` is empty or does not contain a DateTime index.
- RuntimeError: If statistical models fail to converge on the supplied data.

### Examples

```python
>>> import pandas as pd
>>> data = pd.DataFrame({
...     'date': pd.date_range(start='2020-01-01', periods=6, freq='M'),
...     'gdp': [100, 102, 105, 107, 110, 112]
>>> }).set_index('date')
>>> result = conduct_trend_analysis_part1(time_series=data)
>>> print(result)
{'trend_directions': ['upward'], 'seasonality_patterns': [], 'trend_magnitudes': [0.38]}
```

```python
>>> # Example with a clear seasonal component
>>> data = pd.DataFrame({
...     'date': pd.date_range(start='2020-01-01', periods=12, freq='M'),
...     'sales': [200,210,190,205,215,225,230,240,250,260,270,280]
>>> }).set_index('date')
>>> result = conduct_trend_analysis_part1(time_series=data, significance_level=0.01)
>>> print(result)
{'trend_directions': ['upward'], 'seasonality_patterns': ['annual'], 'trend_magnitudes': [0.75]}
```
