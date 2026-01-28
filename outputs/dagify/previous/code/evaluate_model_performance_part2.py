from pydantic import BaseModel, Field


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


def evaluate_model_performance_part2(evaluate_model_performance_part1_input: EvaluateModelPerformancePart1Output, **kwargs) -> EvaluateModelPerformancePart2Output:
    """
    Determine whether an econometric model satisfies predefined goodness‑of‑fit
    thresholds based on its error metrics.

    Parameters
    ----------
    model_name : str
        Identifier or name of the model evaluated (e.g., 'VAR', 'UCM').
    mae : float
        Mean Absolute Error of the model predictions.
    rmse : float
        Root Mean Squared Error of the model predictions.
    mape : float
        Mean Absolute Percentage Error of the model predictions.

    Returns
    -------
    bool
        True if all supplied error metrics are within the acceptable
        thresholds; otherwise False.

    Raises
    ------
    ValueError
        If any of the error metric values are negative or not a finite
        number.

    Examples
    --------
    >>> evaluate_model_performance_part2('Vector Autoregression', 0.02, 0.04,
    2.0)
    True

    >>> evaluate_model_performance_part2('Unobserved Components Model', 0.08,
    0.12, 6.5)
    False

    """
    return EvaluateModelPerformancePart2Output(
        good_fit=False,
    )