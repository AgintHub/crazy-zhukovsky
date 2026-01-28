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


class DrawImplicationsAndRecommendationsPart2Output(BaseModel):
    """Pydantic model for draw_implications_and_recommendations_part2 node outputs."""
    policy_recommendations: List[str] = (
        Field(..., description="Specific policy actions or adjustments suggested to address the identified economic issues.")
    )
    action_items: List[str] = (
        Field(..., description="Step-by-step actions stakeholders can take to implement the recommendations.")
    )
    impact_summary: str = (
        Field(..., description="High-level summary of the expected impact of the recommended actions on the key macroeconomic objectives.")
    )


def draw_implications_and_recommendations_part2(evaluate_model_performance_part1_input: EvaluateModelPerformancePart1Output, evaluate_model_performance_part2_input: EvaluateModelPerformancePart2Output, **kwargs) -> DrawImplicationsAndRecommendationsPart2Output:
    """
    Derive policy recommendations, actionable steps, and an impact summary from
    econometric model performance metrics.

    Parameters
    ----------
    model_name : str
        Identifier of the econometric model whose performance is being
        interpreted (e.g., 'VAR', 'UCM').
    mae : float
        Mean Absolute Error of the model forecasts.
    rmse : float
        Root Mean Squared Error of the model forecasts.
    mape : float
        Mean Absolute Percentage Error of the model forecasts.
    good_fit : bool
        Flag indicating whether the model meets predefined goodness‑of‑fit
        thresholds.

    Returns
    -------
    dict
        Dictionary containing three keys: 'policy_recommendations' (list of
        str), 'action_items' (list of str), and 'impact_summary' (str).

    Raises
    ------
    ValueError
        If any numeric error metric (mae, rmse, mape) is negative.
    TypeError
        If input types do not match the declared signatures.
    RuntimeError
        If good_fit is False, indicating that the model is unreliable for
        policy derivation.

    Examples
    --------
    >>> generate_recommendations(
    ...     model_name='Vector Autoregression',
    ...     mae=0.42,
    ...     rmse=0.58,
    ...     mape=4.7,
    ...     good_fit=True
    >>> )
    {
      'policy_recommendations': [
        "Increase counter‑cyclical fiscal spending during downturns",
        "Adjust interest rate corridor to stabilize inflation"
      ],
      'action_items': [
        "Legislate temporary tax credits for low‑income households",
        "Coordinate with central bank to set policy rate target",
        "Monitor inflation indicators monthly and adjust policy accordingly"
      ],
      'impact_summary': "If implemented, the recommended fiscal and monetary
    measures are expected to improve GDP growth by ~1.2% and keep inflation
    within the 2‑3% target range over the next two years."
    }

    """
    return DrawImplicationsAndRecommendationsPart2Output(
        policy_recommendations=[],
        action_items=[],
        impact_summary="",
    )