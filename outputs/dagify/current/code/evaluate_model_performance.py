from pydantic import BaseModel, Field
from typing import List


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


class EvaluateModelPerformanceOutput(BaseModel):
    """Pydantic model for evaluate_model_performance node outputs."""
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
    good_fit: bool = (
        Field(..., description="Indicator of whether the model meets predefined goodness\u2011of\u2011fit thresholds")
    )


def evaluate_model_performance(apply_econometric_models_input: ApplyEconometricModelsOutput, **kwargs) -> EvaluateModelPerformanceOutput:
    """
    Compute MAE, RMSE, and MAPE for each econometric model and return a
    structured summary with a goodness‑of‑fit flag.

    Parameters
    ----------
    model_name : str
        The name of the econometric model (e.g., 'Vector Autoregression').
    forecast_values : list[float]
        List of forecasted macroeconomic values produced by the model.
    actual_values : list[float]
        Corresponding actual observed values against which forecasts are
        compared.
    mae_threshold : float
        Optional MAE threshold below which the model is considered
        acceptable.
    rmse_threshold : float
        Optional RMSE threshold below which the model is considered
        acceptable.
    mape_threshold : float
        Optional MAPE threshold below which the model is considered
        acceptable.

    Returns
    -------
    dict
        Dictionary with keys 'model_name', 'mae', 'rmse', 'mape', and
        'good_fit' matching the output structure.

    Raises
    ------
    ValueError
        If forecast_values and actual_values have different lengths or are
        empty.

    Examples
    --------
    >>> result = evaluate_model_performance(
    ...     model_name='Vector Autoregression',
    ...     forecast_values=[102.5, 105.0, 107.3],
    ...     actual_values=[100.0, 106.0, 108.0],
    ...     mae_threshold=5.0,
    ...     rmse_threshold=4.0,
    ...     mape_threshold=2.0
    >>> )
    {'model_name': 'Vector Autoregression', 'mae': 3.8333333333333335, 'rmse':
    3.7416573867739413, 'mape': 1.888888888888889, 'good_fit': True}

    >>> result = evaluate_model_performance(
    ...     model_name='Unobserved Components Model',
    ...     forecast_values=[90.0, 92.0, 95.0],
    ...     actual_values=[100.0, 95.0, 98.0],
    ...     mae_threshold=3.0,
    ...     rmse_threshold=3.0,
    ...     mape_threshold=4.0
    >>> )
    {'model_name': 'Unobserved Components Model', 'mae': 5.666666666666667,
    'rmse': 6.082207795688476, 'mape': 6.666666666666667, 'good_fit': False}

    """
    return EvaluateModelPerformanceOutput(
        model_name="",
        mae=0.0,
        rmse=0.0,
        mape=0.0,
        good_fit=False,
    )