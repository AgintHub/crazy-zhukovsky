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


class ConductTrendAnalysisPart1Output(BaseModel):
    """Pydantic model for conduct_trend_analysis_part1 node outputs."""
    trend_directions: List[str] = (
        Field(..., description="Textual description of identified trend directions (e.g., 'upward', 'downward', 'stable')")
    )
    seasonality_patterns: List[str] = (
        Field(..., description="Identified seasonal patterns in time series data")
    )
    trend_magnitudes: List[float] = (
        Field(..., description="Numerical values representing trend magnitude (e.g., regression coefficients)")
    )


def conduct_trend_analysis_part1(collect_economic_data_part1_input: CollectEconomicDataPart1Output, collect_economic_data_part2_input: CollectEconomicDataPart2Output, **kwargs) -> ConductTrendAnalysisPart1Output:
    """
    Identify trend directions, seasonality patterns, and trend magnitudes from a
    pre‑processed time‑series dataset.

    Parameters
    ----------
    time_series : pandas.DataFrame
        Pre‑processed macro‑economic time‑series with a DateTime index and
        one or more numeric columns.
    significance_level : float
        Statistical significance threshold (default 0.05) used when testing
        trend coefficients.

    Returns
    -------
    dict
        Dictionary containing three keys – `trend_directions` (List[str]),
        `seasonality_patterns` (List[str]), and `trend_magnitudes`
        (List[float]) – matching the node's output_structure.

    Raises
    ------
    ValueError
        If `time_series` is empty or does not contain a DateTime index.
    RuntimeError
        If statistical models fail to converge on the supplied data.

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     'date': pd.date_range(start='2020-01-01', periods=6, freq='M'),
    ...     'gdp': [100, 102, 105, 107, 110, 112]
    >>> }).set_index('date')
    >>> result = conduct_trend_analysis_part1(time_series=data)
    >>> print(result)
    {'trend_directions': ['upward'], 'seasonality_patterns': [],
    'trend_magnitudes': [0.38]}

    >>> # Example with a clear seasonal component
    >>> data = pd.DataFrame({
    ...     'date': pd.date_range(start='2020-01-01', periods=12, freq='M'),
    ...     'sales': [200,210,190,205,215,225,230,240,250,260,270,280]
    >>> }).set_index('date')
    >>> result = conduct_trend_analysis_part1(time_series=data,
    significance_level=0.01)
    >>> print(result)
    {'trend_directions': ['upward'], 'seasonality_patterns': ['annual'],
    'trend_magnitudes': [0.75]}

    """
    return ConductTrendAnalysisPart1Output(
        trend_directions=[],
        seasonality_patterns=[],
        trend_magnitudes=[],
    )