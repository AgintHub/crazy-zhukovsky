# collect_economic_data PRD

## Description
Gather and preprocess macroeconomic data from reliable sources.


## Conceptual Info

This node collects macroeconomic data sources specified by user-defined objectives and converts heterogeneous datasets into standardized formats. It automates unit conversion, temporal alignment, and data validation to prepare inputs for trend analysis and econometric modeling.

## Docstring

### Summary
Collects macroeconomic data from specified sources, performs normalization, and returns structured output for downstream analysis.

### Parameters

- **objectives** (List[str]): List of macroeconomic objectives (e.g., GDP growth, inflation control) guiding data collection priorities.
- **metrics** (List[str]): Key performance metrics (e.g., GDP growth rate, CPI inflation) to extract and normalize.

### Returns

Dict[str, Union[List[str], int, bool, str]]: Dictionary containing formatted data sources, record counts, preprocessing status, and operational notes.

### Raises

- ConnectionError: If unable to access a required data source API or database.
- ValueError: If preprocessing steps fail due to incompatible data formats or missing required fields.

### Examples

```python
>>> collect_economic_data(['GDP growth', 'Inflation control'], ['GDP growth rate', 'CPI inflation rate'])
{'data_source_names': ['Bureau of Labor Statistics', 'World Bank'], 'data_records_count': 240, 'preprocessing_successful': True, 'notes': ''}
```

```python
>>> collect_economic_data(['Employment level'], ['Unemployment rate'], source_overrides=['Eurostat'])
{'data_source_names': ['Eurostat'], 'data_records_count': 120, 'preprocessing_successful': False, 'notes': 'Eurostat data contained inconsistent temporal resolution, imputation used'}
```
