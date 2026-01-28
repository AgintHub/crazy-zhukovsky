# define_macroeconomic_objectives PRD

## Description
Specifies the key macroeconomic objectives and performance metrics for analysis.


## Conceptual Info

This node defines the strategic economic goals and the quantitative indicators that will guide the subsequent data collection, analysis, and modeling phases of the macroeconomic workflow.

## Docstring

### Summary
Define macroeconomic objectives and associated performance metrics for analysis.

### Parameters

- **input_text** (str): A natural‑language description of the desired macroeconomic focus, typically provided by the user or higher‑level workflow. It may contain examples of objectives or metrics.

### Returns

Dict[str, List[str]]: A dictionary with two keys: 'objectives' and 'metrics', each mapping to a list of strings that enumerate the primary macroeconomic objectives and their associated performance metrics.

### Raises

- ValueError: If the input_text is empty or does not contain any recognizable objective/metric keywords.
- RuntimeError: If the underlying language model fails to generate a coherent list of objectives or metrics.

### Examples

```python
>>> result = define_macroeconomic_objectives("We aim to improve GDP growth, control inflation, and reduce unemployment.")
>>> print(result['objectives'])
>>> print(result['metrics'])
["GDP growth", "inflation control", "employment level"]
["GDP growth rate", "CPI inflation rate", "unemployment rate"]
```

```python
>>> result = define_macroeconomic_objectives("Focus on monetary policy effectiveness and fiscal stimulus.")
>>> print(result)
{"objectives": ["monetary policy effectiveness", "fiscal stimulus"], "metrics": ["interest rate", "government spending growth"]}
```
