# evaluate_model_performance PRD

## Description
Assesses the accuracy and robustness of the econometric models produced by the apply_econometric_models node, providing key quantitative metrics and a quick fit indicator.


## Conceptual Info

The Evaluate Model Performance node takes the forecasts, significant drivers, and diagnostic flags produced by Apply Econometric Models and computes a concise set of error metrics and a binary goodness‑of‑fit flag. The metrics—Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE)—provide quantitative evidence of predictive accuracy, while the good_fit flag offers an immediate, policy‑ready indicator of model readiness for decision‐making.

## Docstring

### Summary
Compute MAE, RMSE, and MAPE for each econometric model and return a structured summary with a goodness‑of‑fit flag.

### Parameters

- **model_name** (str): The name of the econometric model (e.g., 'Vector Autoregression').
- **forecast_values** (list[float]): List of forecasted macroeconomic values produced by the model.
- **actual_values** (list[float]): Corresponding actual observed values against which forecasts are compared.
- **mae_threshold** (float): Optional MAE threshold below which the model is considered acceptable.
- **rmse_threshold** (float): Optional RMSE threshold below which the model is considered acceptable.
- **mape_threshold** (float): Optional MAPE threshold below which the model is considered acceptable.

### Returns

dict: Dictionary with keys 'model_name', 'mae', 'rmse', 'mape', and 'good_fit' matching the output structure.

### Raises

- ValueError: If forecast_values and actual_values have different lengths or are empty.

### Examples

```python
>>> result = evaluate_model_performance(
...     model_name='Vector Autoregression',
...     forecast_values=[102.5, 105.0, 107.3],
...     actual_values=[100.0, 106.0, 108.0],
...     mae_threshold=5.0,
...     rmse_threshold=4.0,
...     mape_threshold=2.0
>>> )
{'model_name': 'Vector Autoregression', 'mae': 3.8333333333333335, 'rmse': 3.7416573867739413, 'mape': 1.888888888888889, 'good_fit': True}
```

```python
>>> result = evaluate_model_performance(
...     model_name='Unobserved Components Model',
...     forecast_values=[90.0, 92.0, 95.0],
...     actual_values=[100.0, 95.0, 98.0],
...     mae_threshold=3.0,
...     rmse_threshold=3.0,
...     mape_threshold=4.0
>>> )
{'model_name': 'Unobserved Components Model', 'mae': 5.666666666666667, 'rmse': 6.082207795688476, 'mape': 6.666666666666667, 'good_fit': False}
```
