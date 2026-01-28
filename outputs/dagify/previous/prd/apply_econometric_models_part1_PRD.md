# apply_econometric_models_part1 PRD

## Description
Implement econometric models (e.g., VAR, UCM) using significant drivers and trend inputs.


## Conceptual Info

This node fits an econometric forecasting model (such as VAR or UCM) to the macroeconomic time‑series trends and the set of statistically significant drivers identified earlier. The fitted model is then used to generate forward‑looking forecasts for the target macroeconomic performance metrics.

## Docstring

### Summary
Fit an econometric model to trend and driver data and produce forecasts.

### Parameters

- **trend_data** (dict): Dictionary containing outputs from the trend analysis nodes:
- "trend_directions": List[str] – direction of each detected trend.
- "seasonality_patterns": List[str] – seasonal pattern identifiers.
- "trend_magnitudes": List[float] – numeric magnitude (e.g., slope) of each trend.
- "is_significant_trend": List[bool] – significance flag for each trend.
- "key_patterns": List[str] – textual summary of the most important patterns.
- **driver_data** (dict): Dictionary containing outputs from the driver‑identification nodes:
- "key_variables": List[str] – selected macroeconomic drivers.
- "importance_scores": List[float] – relative importance of each driver.
- "relationship_strength": List[float] – strength of each driver’s relationship to the target.
- "relationship_direction": List[str] – "positive" or "negative" direction for each driver.
- **model_type** (str): Choice of econometric model to fit. Supported values: "VAR" (Vector Autoregression) or "UCM" (Unobserved Components Model).

### Returns

dict: Dictionary with keys:
- "model_name": str – the concrete model instantiated (e.g., "Vector Autoregression").
- "forecast_values": List[float] – forecasted values for the target metric over the specified horizon.
- "significant_drivers": List[str] – subset of driver_data["key_variables"] that were retained as statistically significant in the fitted model.

### Raises

- ValueError: If any required field in trend_data or driver_data is missing, empty, or has mismatched lengths.
- RuntimeError: If the chosen model fails to converge or encounters singular matrix issues during estimation.

### Examples

```python
>>> trend_data = {
...     "trend_directions": ["upward", "stable"],
...     "seasonality_patterns": ["quarterly"],
...     "trend_magnitudes": [0.02, 0.0],
...     "is_significant_trend": [True, False],
...     "key_patterns": ["Q1 growth"]
>>> }
>>> driver_data = {
...     "key_variables": ["interest_rate", "unemployment"],
...     "importance_scores": [0.8, 0.6],
...     "relationship_strength": [0.45, -0.30],
...     "relationship_direction": ["negative", "negative"]
>>> }
>>> result = apply_econometric_models(trend_data, driver_data, model_type="VAR")
>>> print(result)
{'model_name': 'Vector Autoregression', 'forecast_values': [2.5, 2.7, 2.9], 'significant_drivers': ['interest_rate']}
```
