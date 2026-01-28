# apply_econometric_models_part2 PRD

## Description
Evaluate model validity and compute diagnostic metrics.


## Conceptual Info

This node validates the econometric model generated in part 1 by running a suite of diagnostic tests (multicollinearity, omitted‑variable bias, convergence) and by computing standard forecasting performance metrics. The results determine whether the model is statistically sound and ready for downstream evaluation and recommendation generation.

## Docstring

### Summary
Validate an econometric model and compute diagnostic performance metrics.

### Parameters

- **trend_directions** (List[str]): Directional trend labels (e.g., 'upward', 'downward') from conduct_trend_analysis_part1.
- **seasonality_patterns** (List[str]): Identified seasonal patterns from conduct_trend_analysis_part1.
- **trend_magnitudes** (List[float]): Numerical magnitudes of each trend (e.g., regression coefficients).
- **is_significant_trend** (List[bool]): Statistical significance flags for each trend from conduct_trend_analysis_part2.
- **key_variables** (List[str]): Key macroeconomic drivers identified in identify_key_macroeconomic_drivers_part1.
- **importance_scores** (List[float]): Relative importance scores for each key variable.
- **relationship_strength** (List[float]): Strength of the relationship between each key variable and the target indicator.
- **relationship_direction** (List[str]): Direction ('positive'/'negative') of each relationship.
- **model_name** (str): Identifier of the econometric model used (e.g., 'Vector Autoregression').
- **forecast_values** (List[float]): Forecasted macro‑economic values produced by the model.
- **significant_drivers** (List[str]): Drivers that passed statistical significance thresholds in part 1.

### Returns

dict: Dictionary containing 'evaluation_metrics' (list of floats) and 'is_model_valid' (bool).

### Raises

- ValueError: If required input lists are mismatched in length or missing.
- RuntimeError: If any diagnostic calculation fails (e.g., singular matrix during VIF computation).

### Examples

```python
>>> result = apply_econometric_models_part2(
...     trend_directions=['upward'],
...     seasonality_patterns=['annual'],
...     trend_magnitudes=[0.03],
...     is_significant_trend=[True],
...     key_variables=['inflation'],
...     importance_scores=[0.85],
...     relationship_strength=[0.78],
...     relationship_direction=['positive'],
...     model_name='Vector Autoregression',
...     forecast_values=[2.5, 2.7, 2.9],
...     significant_drivers=['inflation']
>>> )
{'evaluation_metrics': [0.12, 0.45, 0.92], 'is_model_valid': True}
```

```python
>>> apply_econometric_models_part2(
...     trend_directions=[],
...     seasonality_patterns=[],
...     trend_magnitudes=[],
...     is_significant_trend=[],
...     key_variables=[],
...     importance_scores=[],
...     relationship_strength=[],
...     relationship_direction=[],
...     model_name='VAR',
...     forecast_values=[],
...     significant_drivers=[]
>>> )
ValueError: Input lists cannot be empty.
```
