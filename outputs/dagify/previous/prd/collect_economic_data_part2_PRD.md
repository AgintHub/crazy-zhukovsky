# collect_economic_data_part2 PRD

## Description
Perform preprocessing on the collected macroeconomic data, including normalization, unit consistency checks, and missing data imputation.


## Conceptual Info

This node takes the macroeconomic objectives and their associated performance metrics defined upstream, retrieves the raw data records aligned with those specifications, and prepares the dataset for downstream econometric analysis by applying normalization, ensuring unit consistency, and imputing missing values.

## Docstring

### Summary
Preprocess raw macroeconomic data: normalize values, check unit consistency, and impute missing entries.

### Parameters

- **objectives** (List[str]): Primary macroeconomic objectives extracted from the input description (e.g., ['GDP growth', 'inflation control']).
- **metrics** (List[str]): Key performance metrics linked to each objective (e.g., ['GDP growth rate', 'CPI inflation rate']).
- **raw_records** (list[dict]): A list of raw data records fetched from the sources; each record is a dictionary mapping metric names to raw values and units.

### Returns

dict: Dictionary containing `data_records_count` (int), `preprocessing_successful` (bool), and `notes` (str) as defined in the node's output structure.

### Raises

- ValueError: If `objectives` or `metrics` are empty, or if `raw_records` is not a non‑empty list.
- RuntimeError: If normalization or imputation fails due to incompatible units or irrecoverable missing data.

### Examples

```python
>>> objectives = ['GDP growth', 'inflation control']
>>> metrics = ['GDP growth rate', 'CPI inflation rate']
>>> raw_records = [
...     {'GDP growth rate': 3.2, 'unit': '%', 'CPI inflation rate': None, 'unit': '%'},
...     {'GDP growth rate': 2.9, 'unit': '%', 'CPI inflation rate': 2.1, 'unit': '%'}
>>> ]
>>> result = preprocess_data(objectives, metrics, raw_records)
{'data_records_count': 2, 'preprocessing_successful': True, 'notes': 'Missing CPI value imputed using linear interpolation.'}
```

```python
>>> preprocess_data([], [], [])
ValueError: objectives and metrics must be non‑empty.
```
