# collect_economic_data_part1 PRD

## Description
Gather macroeconomic data from reliable sources based on defined objectives.


## Conceptual Info

This node selects and records the authoritative data providers that can supply the macro‑economic series required to measure the previously defined objectives and metrics.

## Docstring

### Summary
Retrieve a list of reputable data source names that can provide the requested macroeconomic series.

### Parameters

- **objectives** (List[str]): Primary macroeconomic objectives extracted from the input description (e.g., ['GDP growth', 'inflation control']).
- **metrics** (List[str]): Key performance metrics associated with each objective (e.g., ['GDP growth rate', 'CPI inflation rate']).

### Returns

List[str]: A list of data source names that are capable of supplying the required series (e.g., ['World Bank', 'Bureau of Labor Statistics']).

### Raises

- ValueError: If either *objectives* or *metrics* is empty or not a list of strings.
- RuntimeError: If no suitable data source can be identified for the supplied objectives/metrics.

### Examples

```python
>>> collect_economic_data(['GDP growth'], ['GDP growth rate'])
['World Bank', 'Bureau of Labor Statistics']
```

```python
>>> collect_economic_data(['Unemployment'], ['Unemployment rate'])
['International Labour Organization', 'U.S. Bureau of Labor Statistics']
```
