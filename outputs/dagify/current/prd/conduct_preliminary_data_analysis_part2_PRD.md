# conduct_preliminary_data_analysis_part2 PRD

## Description
Detect anomalies or irregularities in the preliminary data analysis.


## Conceptual Info

This node evaluates the results of the preliminary exploratory analysis to determine whether any data points, trends, or metric relationships exhibit anomalous behavior (e.g., outliers, sudden spikes, or inconsistent patterns) that could jeopardize downstream econometric modeling.

## Docstring

### Summary
Detects anomalies in macroeconomic preliminary analysis based on defined objectives and associated metrics.

### Parameters

- **objectives** (List[str]): List of primary macroeconomic objectives extracted from the input description (e.g., ['GDP growth', 'inflation control']).
- **metrics** (List[str]): List of key performance metrics linked to each objective (e.g., ['GDP growth rate', 'CPI inflation rate']).

### Returns

bool: True if any anomaly or irregular pattern is detected; otherwise False.

### Raises

- ValueError: Raised when either `objectives` or `metrics` is empty, indicating insufficient input for anomaly detection.
- RuntimeError: Raised if the internal statistical routine fails (e.g., due to malformed data).

### Examples

```python
>>> detect_anomalies(["GDP growth
>>> \"inflation control\"
False
```

```python
>>> detect_anomalies(["employment level"], ["unemployment rate"] )
True
```
