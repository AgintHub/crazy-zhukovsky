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


class ApplyEconometricModelsPart1Output(BaseModel):
    """Pydantic model for apply_econometric_models_part1 node outputs."""
    model_name: str = (
        Field(..., description="Name of the econometric model used (e.g., 'Vector Autoregression', 'Unobserved Components Model')")
    )
    forecast_values: List[float] = (
        Field(..., description="Numerical forecasts of macroeconomic performance metrics")
    )
    significant_drivers: List[str] = (
        Field(..., description="List of statistically significant macroeconomic drivers included in the model")
    )


def apply_econometric_models_part1(conduct_trend_analysis_part1_input: ConductTrendAnalysisPart1Output, conduct_trend_analysis_part2_input: ConductTrendAnalysisPart2Output, identify_key_macroeconomic_drivers_part1_input: IdentifyKeyMacroeconomicDriversPart1Output, identify_key_macroeconomic_drivers_part2_input: IdentifyKeyMacroeconomicDriversPart2Output, **kwargs) -> ApplyEconometricModelsPart1Output:
    """
    Fit an econometric model to trend and driver data and produce forecasts.

    Parameters
    ----------
    trend_data : dict
        Dictionary containing outputs from the trend analysis nodes: -
        "trend_directions": List[str] – direction of each detected trend. -
        "seasonality_patterns": List[str] – seasonal pattern identifiers. -
        "trend_magnitudes": List[float] – numeric magnitude (e.g., slope) of
        each trend. - "is_significant_trend": List[bool] – significance flag
        for each trend. - "key_patterns": List[str] – textual summary of the
        most important patterns.
    driver_data : dict
        Dictionary containing outputs from the driver‑identification nodes:
        - "key_variables": List[str] – selected macroeconomic drivers. -
        "importance_scores": List[float] – relative importance of each
        driver. - "relationship_strength": List[float] – strength of each
        driver’s relationship to the target. - "relationship_direction":
        List[str] – "positive" or "negative" direction for each driver.
    model_type : str
        Choice of econometric model to fit. Supported values: "VAR" (Vector
        Autoregression) or "UCM" (Unobserved Components Model).

    Returns
    -------
    dict
        Dictionary with keys: - "model_name": str – the concrete model
        instantiated (e.g., "Vector Autoregression"). - "forecast_values":
        List[float] – forecasted values for the target metric over the
        specified horizon. - "significant_drivers": List[str] – subset of
        driver_data["key_variables"] that were retained as statistically
        significant in the fitted model.

    Raises
    ------
    ValueError
        If any required field in trend_data or driver_data is missing,
        empty, or has mismatched lengths.
    RuntimeError
        If the chosen model fails to converge or encounters singular matrix
        issues during estimation.

    Examples
    --------
    >>> trend_data = {
    ...     "trend_directions": ["upward", "stable"],
    ...     "seasonality_patterns": ["quarterly"],
    ...     "trend_magnitudes": [0.02, 0.0],
    ...     "is_significant_trend": [True, False],
    ...     "key_patterns": ["Q1 growth"]
    >>> }
    >>> driver_data = {
    ...     "key_variables": ["interest_rate", "unemployment"],
    ...     "importance_scores": [0.8, 0.6],
    ...     "relationship_strength": [0.45, -0.30],
    ...     "relationship_direction": ["negative", "negative"]
    >>> }
    >>> result = apply_econometric_models(trend_data, driver_data,
    model_type="VAR")
    >>> print(result)
    {'model_name': 'Vector Autoregression', 'forecast_values': [2.5, 2.7, 2.9],
    'significant_drivers': ['interest_rate']}

    """
    return ApplyEconometricModelsPart1Output(
        model_name="",
        forecast_values=[],
        significant_drivers=[],
    )