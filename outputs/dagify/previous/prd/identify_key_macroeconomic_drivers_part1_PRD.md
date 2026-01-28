# identify_key_macroeconomic_drivers_part1 PRD

## Description
Select the most influential macroeconomic variables from the potential drivers.


## Conceptual Info

This node refines the broader set of potential macroeconomic drivers into a concise list of key variables that exhibit the strongest statistical relationship with the target economic indicator. It leverages correlation coefficients or model‑based feature importance scores computed from the pre‑processed dataset to rank and select the most impactful drivers.

## Docstring

### Summary
Selects key macroeconomic drivers based on statistical importance derived from pre‑processed data.

### Parameters

- **potential_drivers** (List[str]): List of candidate macroeconomic variables identified by the preceding driver‑identification node.
- **data_records_count** (int): Number of observations available after data collection and preprocessing.
- **preprocessing_successful** (bool): Flag indicating whether the data preprocessing step completed without errors.

### Returns

Tuple[List[str], List[float]]: A tuple where the first element is `key_variables`—the selected macroeconomic variables—and the second element is `importance_scores`—their corresponding relative importance values.

### Raises

- ValueError: If `preprocessing_successful` is False, indicating that the input data are not ready for analysis.
- ValueError: If `potential_drivers` is empty, because no candidates are available to evaluate.

### Examples

```python
>>> identify_key_macroeconomic_drivers_part1(
...     potential_drivers=["GDP", "CPI", "Unemployment", "Interest Rate"],
...     data_records_count=120,
...     preprocessing_successful=True
>>> )
(['GDP', 'CPI', 'Interest Rate'], [0.45, 0.30, 0.25])
```

```python
>>> identify_key_macroeconomic_drivers_part1(
...     potential_drivers=["Export Volume", "Import Price"],
...     data_records_count=80,
...     preprocessing_successful=True
>>> )
(['Export Volume', 'Import Price'], [0.52, 0.48])
```
