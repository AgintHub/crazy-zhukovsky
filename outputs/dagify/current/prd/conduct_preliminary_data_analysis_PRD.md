# conduct_preliminary_data_analysis PRD

## Description
This node performs an initial exploratory analysis of the macroeconomic time‑series data collected in previous steps. It computes simple trend estimates (e.g., linear regression slopes or growth rates), flags any statistically significant upward or downward movements, and checks for outliers or irregularities that may warrant further investigation. The output summarizes the detected trends, their quantitative strengths, and whether any anomalies were found.


## Conceptual Info

Conduct_preliminary_data_analysis extracts high‑level trend signals and anomaly flags from macroeconomic time‑series to inform subsequent model specification and driver selection.

## Docstring

### Summary
Performs a quick exploratory analysis of macroeconomic data to identify trends and detect anomalies.

### Parameters

- **data** (pandas.DataFrame): Multivariate time‑series of macroeconomic indicators with a DatetimeIndex. Columns correspond to metrics specified in the parent node 'define_macroeconomic_objectives'.
- **metrics** (List[str]): List of column names in `data` that represent the macroeconomic metrics to analyze.
- **window_size** (int): Size of the rolling window (in periods) used to compute local trend slopes. Default is 12 (months).

### Returns

Tuple[List[str], List[float], bool]: A tuple containing (identified_trends, trend_strengths, anomalies_detected). The list lengths are equal and correspond to the same order.

### Raises

- ValueError: Raised if `data` is empty or missing any of the specified `metrics`.
- TypeError: Raised if `data` is not a pandas DataFrame or if `metrics` is not a list of strings.

### Examples

```python
>>> import pandas as pd
>>> df = pd.DataFrame({
...     'date': pd.date_range('2020-01-01', periods=24, freq='M'),
...     'GDP_growth': [2.5, 2.7, 2.6, 2.8, 3.0, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 4.0, 4.1, 4.3, 4.5, 4.6, 4.7, 4.9, 5.0, 5.1, 5.3, 5.4, 5.6, 5.8]
>>> })
>>> df.set_index('date', inplace=True)
>>> trends, strengths, anomalies = conduct_preliminary_data_analysis(df, ['GDP_growth'])
>>> print(trends)
>>> print(strengths)
>>> print(anomalies)
['upward']
[0.045]
False
```

```python
>>> df['inflation'] = [2.1, 2.3, 2.2, 2.5, 2.7, 2.6, 2.8, 3.0, 3.1, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0, 4.1, 4.2, 4.3, 4.5, 4.6, 4.8, 5.0, 5.2, 5.4]
>>> trends, strengths, anomalies = conduct_preliminary_data_analysis(df, ['GDP_growth', 'inflation'], window_size=6)
>>> print(trends)
>>> print(strengths)
>>> print(anomalies)
['upward', 'upward']
[0.048, 0.054]
True
```
