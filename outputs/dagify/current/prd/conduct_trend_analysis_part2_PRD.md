# conduct_trend_analysis_part2 PRD

## Description
Assess statistical significance of identified trends and summarize key patterns.


## Conceptual Info

This node evaluates the statistical significance of each detected macro‑economic trend (e.g., using t‑tests or confidence intervals) and synthesizes a concise textual summary of the most salient macro‑economic patterns such as growth, recession, or seasonal cycles. The results feed downstream econometric modelling and recommendation generation.

## Docstring

### Summary
Determine significance of identified trends and produce a high‑level pattern summary.

### Parameters

- **trend_directions** (List[str]): Directional descriptors for each trend (e.g., 'upward', 'downward', 'stable').
- **trend_magnitudes** (List[float]): Numeric magnitude of each trend (e.g., slope, growth rate).
- **seasonality_patterns** (List[str]): Identified seasonal components for each series (e.g., 'quarterly', 'annual').
- **confidence_level** (float): Desired confidence level for significance testing (default 0.95).

### Returns

dict: Dictionary with keys 'is_significant_trend' (List[bool]) and 'key_patterns' (List[str]) matching the node's output structure.

### Raises

- ValueError: If the lengths of trend_directions, trend_magnitudes, and seasonality_patterns do not match.
- RuntimeError: If statistical tests fail to converge or required libraries are unavailable.

### Examples

```python
>>> result = conduct_trend_analysis_part2(
...     trend_directions=['upward', 'downward'],
...     trend_magnitudes=[0.04, -0.02],
...     seasonality_patterns=['annual', 'quarterly'],
...     confidence_level=0.95
>>> )
{'is_significant_trend': [True, False], 'key_patterns': ['Sustained annual growth', 'Recent quarterly decline']}
```

```python
>>> conduct_trend_analysis_part2(
...     trend_directions=['stable'],
...     trend_magnitudes=[0.0],
...     seasonality_patterns=['none']
>>> )
{'is_significant_trend': [False], 'key_patterns': ['No significant trend detected']}
```
