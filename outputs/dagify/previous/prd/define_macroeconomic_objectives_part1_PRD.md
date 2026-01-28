# define_macroeconomic_objectives_part1 PRD

## Description
Extract primary macroeconomic objectives from the input description.


## Conceptual Info

This node serves as the foundational step in defining the scope of macroeconomic analysis by extracting high-level policy goals from an unstructured textual description. The identified objectives guide all subsequent data collection, analysis, and modeling decisions in the pipeline.

## Docstring

### Summary
Extracts primary macroeconomic objectives from an input text description, returning a list of standardized objective labels.

### Parameters

- **input_description** (str): Unstructured textual description containing information about economic policy goals, challenges, or priorities. Must be non-empty.

### Returns

List[str]: List of primary macroeconomic objectives (e.g., 'GDP growth', 'inflation control', 'employment level') identified from the input. The output is normalized to lowercase with consistent phrasing. Returns empty list if no objectives are found.

### Raises

- TypeError: If input_description is not of type str.
- ValueError: If input_description is empty or contains only whitespace.

### Examples

```python
>>> define_objectives('The government aims to boost GDP growth and maintain inflation below 3%.')
...   # Extracts core macroeconomic goals from policy statement
['gdp growth', 'inflation control']
```

```python
>>> define_objectives('Central bank priorities include employment, price stability, and sustainable development.')
['employment level', 'inflation control', 'sustainable economic growth']
```
