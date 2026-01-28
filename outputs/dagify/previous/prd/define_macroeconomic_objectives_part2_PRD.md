# define_macroeconomic_objectives_part2 PRD

## Description
Extract key performance metrics associated with the defined macroeconomic objectives.


## Conceptual Info

This node bridges high-level macroeconomic objectives with quantifiable indicators by identifying specific performance metrics that can be used to monitor and evaluate each objective. It ensures alignment between strategic goals and measurable data points, enabling downstream data collection and analysis.

## Docstring

### Summary
Extract key performance metrics corresponding to the defined macroeconomic objectives.

### Parameters

- **input_text** (str): Free-form textual description containing macroeconomic objectives from which performance metrics must be identified and extracted.

### Returns

List[str]: List of key performance metrics (e.g., GDP growth rate, CPI inflation rate) associated with the macroeconomic objectives mentioned in the input text.

### Raises

- ValueError: If the input_text is empty or contains only whitespace.
- TypeError: If the input_text is not of type string.

### Examples

```python
>>> extract_metrics('The government aims to boost GDP growth, control inflation, and reduce unemployment.')
['GDP growth rate', 'CPI inflation rate', 'unemployment rate']
```

```python
>>> extract_metrics('Maintain price stability and achieve full employment.')
['inflation rate', 'employment rate']
```
