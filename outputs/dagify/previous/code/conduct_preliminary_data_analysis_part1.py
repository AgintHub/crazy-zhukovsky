from pydantic import BaseModel, Field
from typing import List


class DefineMacroeconomicObjectivesPart1Output(BaseModel):
    """Pydantic model for define_macroeconomic_objectives_part1 node outputs."""
    objectives: List[str] = (
        Field(..., description="List of primary macroeconomic objectives (e.g., GDP growth, inflation control, employment level).")
    )


class DefineMacroeconomicObjectivesPart2Output(BaseModel):
    """Pydantic model for define_macroeconomic_objectives_part2 node outputs."""
    metrics: List[str] = (
        Field(..., description="List of key performance metrics associated with each objective (e.g., GDP growth rate, CPI inflation rate, unemployment rate).")
    )


class ConductPreliminaryDataAnalysisPart1Output(BaseModel):
    """Pydantic model for conduct_preliminary_data_analysis_part1 node outputs."""
    identified_trends: List[str] = (
        Field(..., description="List of trend names or descriptors identified in the data")
    )
    trend_strengths: List[float] = (
        Field(..., description="Quantitative strength (e.g., slope or growth rate) associated with each identified trend")
    )


def conduct_preliminary_data_analysis_part1(define_macroeconomic_objectives_part1_input: DefineMacroeconomicObjectivesPart1Output, define_macroeconomic_objectives_part2_input: DefineMacroeconomicObjectivesPart2Output, **kwargs) -> ConductPreliminaryDataAnalysisPart1Output:
    """
    Identify primary upward or downward trends in macroeconomic metrics based on
    linear regression or growth‑rate calculations.

    Parameters
    ----------
    objectives : List[str]
        Primary macroeconomic objectives extracted from the input
        description (e.g., ['GDP growth', 'inflation control']).
    metrics : List[str]
        Key performance metrics linked to the objectives (e.g., ['GDP growth
        rate', 'CPI inflation']).
    data_frame : pandas.DataFrame
        Time‑series dataframe where each column corresponds to a metric name
        and rows represent chronological observations.

    Returns
    -------
    dict
        Dictionary with two keys: 'identified_trends' (List[str]) and
        'trend_strengths' (List[float]), aligned by index.

    Raises
    ------
    ValueError
        If either *objectives* or *metrics* is empty, or if required metric
        columns are missing from *data_frame*.
    RuntimeError
        If linear regression fails to converge for a metric.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'GDP growth rate': [2.1, 2.3, 2.5, 2.8, 3.0],
    ...     'CPI inflation': [1.8, 1.9, 2.0, 2.2, 2.4]
    >>> }, index=pd.date_range('2020', periods=5, freq='Y'))
    >>> result = conduct_preliminary_data_analysis_part1(
    ...     objectives=['GDP growth', 'inflation control'],
    ...     metrics=['GDP growth rate', 'CPI inflation'],
    ...     data_frame=df
    >>> )
    >>> print(result)
    {'identified_trends': ['upward', 'upward'], 'trend_strengths': [0.225,
    0.15]}

    """
    return ConductPreliminaryDataAnalysisPart1Output(
        identified_trends=[],
        trend_strengths=[],
    )