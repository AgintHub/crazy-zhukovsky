from pydantic import BaseModel, Field
from typing import List


class CollectEconomicDataPart1Output(BaseModel):
    """Pydantic model for collect_economic_data_part1 node outputs."""
    data_source_names: List[str] = (
        Field(..., description="Names of data sources used (e.g., 'Bureau of Labor Statistics', 'World Bank').")
    )


class CollectEconomicDataPart2Output(BaseModel):
    """Pydantic model for collect_economic_data_part2 node outputs."""
    data_records_count: int = (
        Field(..., description="Total number of data records retrieved across all sources.")
    )
    preprocessing_successful: bool = (
        Field(..., description="Indicates whether preprocessing (adjustments, normalization) completed without errors.")
    )
    notes: str = (
        Field(..., description="Any additional remarks or issues encountered during data collection and preprocessing.")
    )


class ConductTrendAnalysisPart2Output(BaseModel):
    """Pydantic model for conduct_trend_analysis_part2 node outputs."""
    is_significant_trend: List[bool] = (
        Field(..., description="Indicator of whether trends are statistically significant")
    )
    key_patterns: List[str] = (
        Field(..., description="Summary of primary patterns identified in macroeconomic indicators")
    )


def conduct_trend_analysis_part2(collect_economic_data_part1_input: CollectEconomicDataPart1Output, collect_economic_data_part2_input: CollectEconomicDataPart2Output, **kwargs) -> ConductTrendAnalysisPart2Output:
    """
    Determine significance of identified trends and produce a high‑level pattern
    summary.

    Parameters
    ----------
    trend_directions : List[str]
        Directional descriptors for each trend (e.g., 'upward', 'downward',
        'stable').
    trend_magnitudes : List[float]
        Numeric magnitude of each trend (e.g., slope, growth rate).
    seasonality_patterns : List[str]
        Identified seasonal components for each series (e.g., 'quarterly',
        'annual').
    confidence_level : float
        Desired confidence level for significance testing (default 0.95).

    Returns
    -------
    dict
        Dictionary with keys 'is_significant_trend' (List[bool]) and
        'key_patterns' (List[str]) matching the node's output structure.

    Raises
    ------
    ValueError
        If the lengths of trend_directions, trend_magnitudes, and
        seasonality_patterns do not match.
    RuntimeError
        If statistical tests fail to converge or required libraries are
        unavailable.

    Examples
    --------
    >>> result = conduct_trend_analysis_part2(
    ...     trend_directions=['upward', 'downward'],
    ...     trend_magnitudes=[0.04, -0.02],
    ...     seasonality_patterns=['annual', 'quarterly'],
    ...     confidence_level=0.95
    >>> )
    {'is_significant_trend': [True, False], 'key_patterns': ['Sustained annual
    growth', 'Recent quarterly decline']}

    >>> conduct_trend_analysis_part2(
    ...     trend_directions=['stable'],
    ...     trend_magnitudes=[0.0],
    ...     seasonality_patterns=['none']
    >>> )
    {'is_significant_trend': [False], 'key_patterns': ['No significant trend
    detected']}

    """
    return ConductTrendAnalysisPart2Output(
        is_significant_trend=[],
        key_patterns=[],
    )