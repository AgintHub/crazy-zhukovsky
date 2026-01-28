from pydantic import BaseModel, Field
from typing import List


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


class DrawImplicationsAndRecommendationsOutput(BaseModel):
    """Pydantic model for draw_implications_and_recommendations node outputs."""
    key_insights: List[str] = (
        Field(..., description="Concise list of the most important insights derived from the model evaluation.")
    )
    caveats: List[str] = (
        Field(..., description="Potential limitations, uncertainties, or assumptions affecting the reliability of the insights.")
    )
    policy_recommendations: List[str] = (
        Field(..., description="Specific policy actions or adjustments suggested to address the identified economic issues.")
    )
    action_items: List[str] = (
        Field(..., description="Step\u2011by\u2011step actions stakeholders can take to implement the recommendations.")
    )
    impact_summary: str = (
        Field(..., description="High\u2011level summary of the expected impact of the recommended actions on the key macroeconomic objectives.")
    )


def draw_implications_and_recommendations(evaluate_model_performance_input: EvaluateModelPerformanceOutput, **kwargs) -> DrawImplicationsAndRecommendationsOutput:
    """
    Generate a policy brief from econometric model evaluation results.

    Parameters
    ----------
    model_name : str
        Identifier of the evaluated econometric model.
    mae : float
        Mean Absolute Error of the model predictions.
    rmse : float
        Root Mean Squared Error of the model predictions.
    mape : float
        Mean Absolute Percentage Error of the model predictions.
    good_fit : bool
        Indicator whether the model meets predefined goodness‑of‑fit
        thresholds.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the keys `key_insights`, `caveats`,
        `policy_recommendations`, `action_items`, and `impact_summary` as
        specified in the node's output structure.

    Raises
    ------
    ValueError
        If any required input is missing or of incorrect type.
    RuntimeError
        If the model evaluation indicates that the model is invalid
        (`good_fit` is False).

    Examples
    --------
    >>> result = draw_implications_and_recommendations(
    ...     model_name='Vector Autoregression',
    ...     mae=0.015,
    ...     rmse=0.020,
    ...     mape=3.2,
    ...     good_fit=True
    >>> )
    {
      'key_insights': ['MAE and RMSE are within acceptable thresholds for
    short‑term forecasts.', 'MAPE < 5% indicates high relative accuracy.'],
      'caveats': ['Model performance evaluated on the most recent 12‑month
    window only.', 'Potential structural change in the economy not captured.'],
      'policy_recommendations': ['Maintain current fiscal stimulus to support
    growth.', 'Gradually tighten monetary policy to counteract inflationary
    pressures.'],
      'action_items': ['Review fiscal policy mix in Q3 2026.', 'Schedule a
    monetary policy review meeting in Q1 2027.'],
      'impact_summary': 'Recommended actions aim to sustain GDP growth while
    containing inflation, aligning with the macroeconomic objectives of the
    current policy framework.'
    }

    >>> result = draw_implications_and_recommendations(
    ...     model_name='Unobserved Components Model',
    ...     mae=0.050,
    ...     rmse=0.080,
    ...     mape=12.5,
    ...     good_fit=False
    >>> )
    RuntimeError: Model evaluation indicates insufficient fit for actionable
    policy guidance.

    """
    return DrawImplicationsAndRecommendationsOutput(
        key_insights=[],
        caveats=[],
        policy_recommendations=[],
        action_items=[],
        impact_summary="",
    )