# evaluate_model_performance_part2 PRD

## Description
Determine if the model meets goodness-of-fit thresholds based on evaluation metrics.


## Conceptual Info

This node evaluates the error metrics (MAE, RMSE, MAPE) produced by the previous performance‑evaluation node and decides whether the econometric model satisfies the predefined goodness‑of‑fit criteria. The result drives downstream recommendation and implication nodes.

## Docstring

### Summary
Determine whether an econometric model satisfies predefined goodness‑of‑fit thresholds based on its error metrics.

### Parameters

- **model_name** (str): Identifier or name of the model evaluated (e.g., 'VAR', 'UCM').
- **mae** (float): Mean Absolute Error of the model predictions.
- **rmse** (float): Root Mean Squared Error of the model predictions.
- **mape** (float): Mean Absolute Percentage Error of the model predictions.

### Returns

bool: True if all supplied error metrics are within the acceptable thresholds; otherwise False.

### Raises

- ValueError: If any of the error metric values are negative or not a finite number.

### Examples

```python
>>> evaluate_model_performance_part2('Vector Autoregression', 0.02, 0.04, 2.0)
True
```

```python
>>> evaluate_model_performance_part2('Unobserved Components Model', 0.08, 0.12, 6.5)
False
```
