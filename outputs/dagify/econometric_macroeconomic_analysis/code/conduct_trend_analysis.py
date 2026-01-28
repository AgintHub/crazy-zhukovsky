from pydantic import BaseModel, Field
from typing import List


class CollectEconomicDataOutput(BaseModel):
    """Pydantic model for collect_economic_data node outputs."""
    data_source_names: List[str] = (
        Field(..., description="Names of data sources used (e.g., 'Bureau of Labor Statistics', 'World Bank').")
    )
    data_records_count: int = (
        Field(..., description="Total number of data records retrieved across all sources.")
    )
    preprocessing_successful: bool = (
        Field(..., description="Indicates whether preprocessing (adjustments, normalization) completed without errors.")
    )
    notes: str = (
        Field(..., description="Any additional remarks or issues encountered during data collection and preprocessing.")
    )


class ConductTrendAnalysisOutput(BaseModel):
    """Pydantic model for conduct_trend_analysis node outputs."""
    trend_directions: List[str] = (
        Field(..., description="Textual description of identified trend directions (e.g., 'upward', 'downward', 'stable')")
    )
    seasonality_patterns: List[str] = (
        Field(..., description="Identified seasonal patterns in time series data")
    )
    trend_magnitudes: List[float] = (
        Field(..., description="Numerical values representing trend magnitude (e.g., regression coefficients)")
    )
    is_significant_trend: List[bool] = (
        Field(..., description="Indicator of whether trends are statistically significant")
    )
    key_patterns: List[str] = (
        Field(..., description="Summary of primary patterns identified in macroeconomic indicators")
    )


def conduct_trend_analysis(collect_economic_data_input: CollectEconomicDataOutput, **kwargs) -> ConductTrendAnalysisOutput:
    """
    Applies statistical analysis to identify directional trends, seasonality,
    and magnitude of change in macroeconomic time series data.

    Parameters
    ----------
    economic_data : pd.DataFrame
        Preprocessed macroeconomic time series data with datetime-indexed
        observations
    significance_level : float
        Threshold for determining statistical significance (p-value cutoff),
        default 0.05

    Returns
    -------
    Dict[str, Any]
        Dict containing five parallel arrays (trend_directions,
        seasonality_patterns, trend_magnitudes, is_significant_trend,
        key_patterns) indexed by economic indicator

    Raises
    ------
    ValueError
        If economic_data contains missing values or failed preprocessing
    TypeError
        If economic_data is not a properly formatted DataFrame

    Examples
    --------
    >>> economic_data = pd.DataFrame({'GDP': [2.1, 2.3, 2.5], 'CPI': [1.8, 1.9,
    2.1]})
    >>> analyze_trends(economic_data, significance_level=0.05)
    {'trend_directions': ['upward', 'upward'], 'seasonality_patterns': ['none',
    'none'], 'trend_magnitudes': [0.2, 0.15], 'is_significant_trend': [True,
    True], 'key_patterns': ['GDP growth trend', 'Moderate inflation rise']}

    >>> economic_data = pd.DataFrame({'Unemployment': [5.2, 5.1, 5.0]})
    >>> analyze_trends(economic_data)
    {'trend_directions': ['downward'], 'seasonality_patterns': ['none'],
    'trend_magnitudes': [-0.1], 'is_significant_trend': [False], 'key_patterns':
    ['Stable unemployment decline']}

    """
    return ConductTrendAnalysisOutput(
        trend_directions=[],
        seasonality_patterns=[],
        trend_magnitudes=[],
        is_significant_trend=[],
        key_patterns=[],
    )