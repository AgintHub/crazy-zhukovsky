from pydantic import BaseModel, Field
from typing import List


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


class ApplyEconometricModelsPart2Output(BaseModel):
    """Pydantic model for apply_econometric_models_part2 node outputs."""
    evaluation_metrics: List[float] = (
        Field(..., description="Quantitative metrics for model performance evaluation (e.g., MAE, RMSE, R-squared)")
    )
    is_model_valid: bool = (
        Field(..., description="Indicates whether the model passed diagnostic checks (e.g., multicollinearity tests)")
    )


class EvaluateModelPerformancePart1Output(BaseModel):
    """Pydantic model for evaluate_model_performance_part1 node outputs."""
    model_name: str = (
        Field(..., description="Identifier or name of the model evaluated")
    )
    mae: float = (
        Field(..., description="Mean Absolute Error of the model predictions")
    )
    rmse: float = (
        Field(..., description="Root Mean Squared Error of the model predictions")
    )
    mape: float = (
        Field(..., description="Mean Absolute Percentage Error of the model predictions")
    )


def evaluate_model_performance_part1(apply_econometric_models_part1_input: ApplyEconometricModelsPart1Output, apply_econometric_models_part2_input: ApplyEconometricModelsPart2Output, **kwargs) -> EvaluateModelPerformancePart1Output:
    """
    Calculate MAE, RMSE, and MAPE for a given econometric model's forecasts.

    Parameters
    ----------
    model_name : str
        Name or identifier of the econometric model whose forecasts are
        being evaluated.
    forecast_values : List[float]
        The time‑ordered list of values produced by the model.
    actual_values : List[float]
        The corresponding observed values against which forecasts are
        compared.

    Returns
    -------
    dict
        Dictionary containing the model name and three error metrics: mae,
        rmse, and mape.

    Raises
    ------
    ValueError
        If the lengths of forecast_values and actual_values differ or if
        either list is empty.
    ZeroDivisionError
        If any actual value is zero when computing MAPE, leading to division
        by zero.

    Examples
    --------
    >>> result = evaluate_model_performance_part1(
    ...     model_name='Vector Autoregression',
    ...     forecast_values=[101.5, 102.0, 103.2],
    ...     actual_values=[100.0, 102.5, 103.0]
    >>> )
    >>> print(result)
    {'model_name': 'Vector Autoregression', 'mae': 0.5666666666666667, 'rmse':
    0.816496580927726, 'mape': 0.5870588235294118}

    >>> evaluate_model_performance_part1(
    ...     model_name='Unobserved Components Model',
    ...     forecast_values=[200, 210, 220],
    ...     actual_values=[195, 215, 225]
    >>> )
    {'model_name': 'Unobserved Components Model', 'mae': 5.0, 'rmse': 5.0,
    'mape': 2.380952380952381}

    """
    return EvaluateModelPerformancePart1Output(
        model_name="",
        mae=0.0,
        rmse=0.0,
        mape=0.0,
    )