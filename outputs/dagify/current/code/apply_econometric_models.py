from pydantic import BaseModel, Field
from typing import List


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


class IdentifyKeyMacroeconomicDriversOutput(BaseModel):
    """Pydantic model for identify_key_macroeconomic_drivers node outputs."""
    key_variables: List[str] = (
        Field(..., description="List of identified key macroeconomic variables.")
    )
    importance_scores: List[float] = (
        Field(..., description="Relative importance score for each key variable (higher indicates greater influence).")
    )
    relationship_strength: List[float] = (
        Field(..., description="Numeric strength of the relationship between each key variable and the target macroeconomic indicator.")
    )
    relationship_direction: List[str] = (
        Field(..., description="Direction of the relationship for each key variable (e.g., 'positive', 'negative').")
    )


class IdentifyPotentialMacroeconomicDriversOutput(BaseModel):
    """Pydantic model for identify_potential_macroeconomic_drivers node outputs."""
    potential_drivers: List[str] = (
        Field(..., description="A list of macroeconomic variable names identified as potential drivers.")
    )


class ApplyEconometricModelsOutput(BaseModel):
    """Pydantic model for apply_econometric_models node outputs."""
    model_name: str = (
        Field(..., description="Name of the econometric model used (e.g., 'Vector Autoregression', 'Unobserved Components Model')")
    )
    forecast_values: List[float] = (
        Field(..., description="Numerical forecasts of macroeconomic performance metrics")
    )
    significant_drivers: List[str] = (
        Field(..., description="List of statistically significant macroeconomic drivers included in the model")
    )
    evaluation_metrics: List[float] = (
        Field(..., description="Quantitative metrics for model performance evaluation (e.g., MAE, RMSE, R-squared)")
    )
    is_model_valid: bool = (
        Field(..., description="Indicates whether the model passed diagnostic checks (e.g., multicollinearity tests)")
    )


def apply_econometric_models(conduct_trend_analysis_input: ConductTrendAnalysisOutput, identify_key_macroeconomic_drivers_input: IdentifyKeyMacroeconomicDriversOutput, identify_potential_macroeconomic_drivers_input: IdentifyPotentialMacroeconomicDriversOutput, **kwargs) -> ApplyEconometricModelsOutput:
    """
    Constructs and validates econometric models using statistically significant
    macroeconomic drivers, trend patterns, and potential drivers to produce
    macroeconomic forecasts.

    Parameters
    ----------
    trend_analysis : Dict[str, List]
        Results from conduct_trend_analysis including trend_directions,
        seasonality_patterns, and trend_magnitudes
    key_drivers : Dict[str, List]
        Significant drivers from identify_key_macroeconomic_drivers with
        importance_scores > 0.7
    potential_drivers : Dict[str, List[str]]
        Candidate variables from identify_potential_macroeconomic_drivers

    Returns
    -------
    Dict[str, Union[str, List, bool]]
        Structured dictionary containing model specification, forecasts,
        validation metrics, and diagnostic results.

    Raises
    ------
    ValueError
        If no significant drivers exist after multicollinearity checks
    RuntimeWarning
        When model convergence issues occur during optimization

    Examples
    --------
    >>> model = apply_econometric_models(
    ...     trend_analysis={
    ...         'trend_directions': ['upward'],
    ...         'trend_magnitudes': [0.05]
    ...     },
    ...     key_drivers={
    ...         'key_variables': ['GDP', 'CPI'],
    ...         'importance_scores': [0.85, 0.72]
    ...     },
    ...     potential_drivers={'potential_drivers': ['Interest Rate']}
    >>> )
    >>> model['model_name'], len(model['forecast_values'])
    ("'Vector Autoregression', 12)

    >>> try:
    ...     apply_econometric_models({
    ...         'trend_directions': ['stable'],
    ...         'trend_magnitudes': [0.0]
    ...     }, {
    ...         'key_variables': [],
    ...         'importance_scores': []
    ...     }, {
    ...         'potential_drivers': ['Unemployment']
    ...     })
    >>> except ValueError as e:
    ...     str(e)
    'No valid drivers available after filtering'

    """
    return ApplyEconometricModelsOutput(
        model_name="",
        forecast_values=[],
        significant_drivers=[],
        evaluation_metrics=[],
        is_model_valid=False,
    )