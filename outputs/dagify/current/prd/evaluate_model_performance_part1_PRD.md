# evaluate_model_performance_part1 PRD

## Description
Compute error metrics (MAE, RMSE, MAPE) for the applied econometric model.


## Conceptual Info

This node evaluates the predictive accuracy of an econometric model by comparing its forecasted values against observed ground‑truth data and returning standard error metrics (MAE, RMSE, MAPE).

## Docstring

### Summary
Calculate MAE, RMSE, and MAPE for a given econometric model's forecasts.

### Parameters

- **model_name** (str): Name or identifier of the econometric model whose forecasts are being evaluated.
- **forecast_values** (List[float]): The time‑ordered list of values produced by the model.
- **actual_values** (List[float]): The corresponding observed values against which forecasts are compared.

### Returns

dict: Dictionary containing the model name and three error metrics: mae, rmse, and mape.

### Raises

- ValueError: If the lengths of forecast_values and actual_values differ or if either list is empty.
- ZeroDivisionError: If any actual value is zero when computing MAPE, leading to division by zero.

### Examples

```python
>>> result = evaluate_model_performance_part1(
...     model_name='Vector Autoregression',
...     forecast_values=[101.5, 102.0, 103.2],
...     actual_values=[100.0, 102.5, 103.0]
>>> )
>>> print(result)
{'model_name': 'Vector Autoregression', 'mae': 0.5666666666666667, 'rmse': 0.816496580927726, 'mape': 0.5870588235294118}
```

```python
>>> evaluate_model_performance_part1(
...     model_name='Unobserved Components Model',
...     forecast_values=[200, 210, 220],
...     actual_values=[195, 215, 225]
>>> )
{'model_name': 'Unobserved Components Model', 'mae': 5.0, 'rmse': 5.0, 'mape': 2.380952380952381}
```
