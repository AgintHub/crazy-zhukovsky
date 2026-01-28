from pydantic import BaseModel, Field
from typing import List


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


class ConductTrendAnalysisPart2Output(BaseModel):
    """Pydantic model for conduct_trend_analysis_part2 node outputs."""
    is_significant_trend: List[bool] = (
        Field(..., description="Indicator of whether trends are statistically significant")
    )
    key_patterns: List[str] = (
        Field(..., description="Summary of primary patterns identified in macroeconomic indicators")
    )


class IdentifyKeyMacroeconomicDriversPart1Output(BaseModel):
    """Pydantic model for identify_key_macroeconomic_drivers_part1 node outputs."""
    key_variables: List[str] = (
        Field(..., description="List of identified key macroeconomic variables.")
    )
    importance_scores: List[float] = (
        Field(..., description="Relative importance score for each key variable (higher indicates greater influence).")
    )


class IdentifyKeyMacroeconomicDriversPart2Output(BaseModel):
    """Pydantic model for identify_key_macroeconomic_drivers_part2 node outputs."""
    relationship_strength: List[float] = (
        Field(..., description="Numeric strength of the relationship between each key variable and the target macroeconomic indicator.")
    )
    relationship_direction: List[str] = (
        Field(..., description="Direction of the relationship for each key variable (e.g., 'positive', 'negative').")
    )


class ApplyEconometricModelsPart2Output(BaseModel):
    """Pydantic model for apply_econometric_models_part2 node outputs."""
    evaluation_metrics: List[float] = (
        Field(..., description="Quantitative metrics for model performance evaluation (e.g., MAE, RMSE, R-squared)")
    )
    is_model_valid: bool = (
        Field(..., description="Indicates whether the model passed diagnostic checks (e.g., multicollinearity tests)")
    )


def apply_econometric_models_part2(conduct_trend_analysis_part1_input: ConductTrendAnalysisPart1Output, conduct_trend_analysis_part2_input: ConductTrendAnalysisPart2Output, identify_key_macroeconomic_drivers_part1_input: IdentifyKeyMacroeconomicDriversPart1Output, identify_key_macroeconomic_drivers_part2_input: IdentifyKeyMacroeconomicDriversPart2Output, **kwargs) -> ApplyEconometricModelsPart2Output:
    """
    Validate an econometric model and compute diagnostic performance metrics.

    Parameters
    ----------
    trend_directions : List[str]
        Directional trend labels (e.g., 'upward', 'downward') from
        conduct_trend_analysis_part1.
    seasonality_patterns : List[str]
        Identified seasonal patterns from conduct_trend_analysis_part1.
    trend_magnitudes : List[float]
        Numerical magnitudes of each trend (e.g., regression coefficients).
    is_significant_trend : List[bool]
        Statistical significance flags for each trend from
        conduct_trend_analysis_part2.
    key_variables : List[str]
        Key macroeconomic drivers identified in
        identify_key_macroeconomic_drivers_part1.
    importance_scores : List[float]
        Relative importance scores for each key variable.
    relationship_strength : List[float]
        Strength of the relationship between each key variable and the
        target indicator.
    relationship_direction : List[str]
        Direction ('positive'/'negative') of each relationship.
    model_name : str
        Identifier of the econometric model used (e.g., 'Vector
        Autoregression').
    forecast_values : List[float]
        Forecasted macro‑economic values produced by the model.
    significant_drivers : List[str]
        Drivers that passed statistical significance thresholds in part 1.

    Returns
    -------
    dict
        Dictionary containing 'evaluation_metrics' (list of floats) and
        'is_model_valid' (bool).

    Raises
    ------
    ValueError
        If required input lists are mismatched in length or missing.
    RuntimeError
        If any diagnostic calculation fails (e.g., singular matrix during
        VIF computation).

    Examples
    --------
    >>> result = apply_econometric_models_part2(
    ...     trend_directions=['upward'],
    ...     seasonality_patterns=['annual'],
    ...     trend_magnitudes=[0.03],
    ...     is_significant_trend=[True],
    ...     key_variables=['inflation'],
    ...     importance_scores=[0.85],
    ...     relationship_strength=[0.78],
    ...     relationship_direction=['positive'],
    ...     model_name='Vector Autoregression',
    ...     forecast_values=[2.5, 2.7, 2.9],
    ...     significant_drivers=['inflation']
    >>> )
    {'evaluation_metrics': [0.12, 0.45, 0.92], 'is_model_valid': True}

    >>> apply_econometric_models_part2(
    ...     trend_directions=[],
    ...     seasonality_patterns=[],
    ...     trend_magnitudes=[],
    ...     is_significant_trend=[],
    ...     key_variables=[],
    ...     importance_scores=[],
    ...     relationship_strength=[],
    ...     relationship_direction=[],
    ...     model_name='VAR',
    ...     forecast_values=[],
    ...     significant_drivers=[]
    >>> )
    ValueError: Input lists cannot be empty.

    """
    return ApplyEconometricModelsPart2Output(
        evaluation_metrics=[],
        is_model_valid=False,
    )