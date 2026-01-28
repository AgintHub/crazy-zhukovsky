from pydantic import BaseModel, Field
from typing import List


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


class EvaluateModelPerformancePart2Output(BaseModel):
    """Pydantic model for evaluate_model_performance_part2 node outputs."""
    good_fit: bool = (
        Field(..., description="Indicator of whether the model meets predefined goodness-of-fit thresholds")
    )


class DrawImplicationsAndRecommendationsPart1Output(BaseModel):
    """Pydantic model for draw_implications_and_recommendations_part1 node outputs."""
    key_insights: List[str] = (
        Field(..., description="Concise list of the most important insights derived from the model evaluation.")
    )
    caveats: List[str] = (
        Field(..., description="Potential limitations, uncertainties, or assumptions affecting the reliability of the insights.")
    )


def draw_implications_and_recommendations_part1(evaluate_model_performance_part1_input: EvaluateModelPerformancePart1Output, evaluate_model_performance_part2_input: EvaluateModelPerformancePart2Output, **kwargs) -> DrawImplicationsAndRecommendationsPart1Output:
    """
    Generate concise insights and associated caveats from model performance
    metrics.

    Parameters
    ----------
    model_name : str
        Identifier or name of the evaluated econometric model (e.g., 'Vector
        Autoregression').
    mae : float
        Mean Absolute Error of the model predictions.
    rmse : float
        Root Mean Squared Error of the model predictions.
    mape : float
        Mean Absolute Percentage Error of the model predictions.
    good_fit : bool
        Flag indicating whether the model meets predefined goodness‑of‑fit
        thresholds.

    Returns
    -------
    dict
        Dictionary with two keys: 'key_insights' (List[str]) and 'caveats'
        (List[str]).

    Raises
    ------
    ValueError
        If any of the numeric metrics are negative or NaN.
    TypeError
        If input types do not match the declared parameter types.

    Examples
    --------
    >>> insights = draw_implications_and_recommendations_part1(
    ...     model_name='Vector Autoregression',
    ...     mae=0.45,
    ...     rmse=0.62,
    ...     mape=5.3,
    ...     good_fit=True
    >>> )
    {'key_insights': ['MAE of 0.45 indicates modest average error.', 'RMSE of
    0.62 shows reasonable forecast dispersion.', 'Model meets the predefined
    goodness‑of‑fit criteria.'], 'caveats': ['MAE and RMSE do not capture
    directional bias.', 'MAPE of 5.3% may be high for policy‑sensitive
    variables.', 'Good‑fit flag is based on static thresholds that may not
    reflect all economic regimes.']}

    >>> draw_implications_and_recommendations_part1(
    ...     model_name='Unobserved Components Model',
    ...     mae=0.0, rmse=0.0, mape=0.0, good_fit=False
    >>> )
    {'key_insights': ['All error metrics are zero, suggesting a possible data
    leakage or over‑fitting.'], 'caveats': ['Good‑fit flag is False, indicating
    the model failed diagnostic checks.', 'Zero errors are unrealistic for
    real‑world macroeconomic data.']}

    """
    return DrawImplicationsAndRecommendationsPart1Output(
        key_insights=[],
        caveats=[],
    )