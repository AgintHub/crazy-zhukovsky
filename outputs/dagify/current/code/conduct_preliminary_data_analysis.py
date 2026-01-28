from pydantic import BaseModel, Field
from typing import List


class DefineMacroeconomicObjectivesOutput(BaseModel):
    """Pydantic model for define_macroeconomic_objectives node outputs."""
    objectives: List[str] = (
        Field(..., description="List of primary macroeconomic objectives (e.g., GDP growth, inflation control, employment level).")
    )
    metrics: List[str] = (
        Field(..., description="List of key performance metrics associated with each objective (e.g., GDP growth rate, CPI inflation rate, unemployment rate).")
    )


class ConductPreliminaryDataAnalysisOutput(BaseModel):
    """Pydantic model for conduct_preliminary_data_analysis node outputs."""
    identified_trends: List[str] = (
        Field(..., description="List of trend names or descriptors identified in the data")
    )
    trend_strengths: List[float] = (
        Field(..., description="Quantitative strength (e.g., slope or growth rate) associated with each identified trend")
    )
    anomalies_detected: bool = (
        Field(..., description="Indicates whether any anomalies or irregular patterns were detected during preliminary analysis")
    )


def conduct_preliminary_data_analysis(define_macroeconomic_objectives_input: DefineMacroeconomicObjectivesOutput, **kwargs) -> ConductPreliminaryDataAnalysisOutput:
    """
    Performs a quick exploratory analysis of macroeconomic data to identify
    trends and detect anomalies.

    Parameters
    ----------
    data : pandas.DataFrame
        Multivariate time‑series of macroeconomic indicators with a
        DatetimeIndex. Columns correspond to metrics specified in the parent
        node 'define_macroeconomic_objectives'.
    metrics : List[str]
        List of column names in `data` that represent the macroeconomic
        metrics to analyze.
    window_size : int
        Size of the rolling window (in periods) used to compute local trend
        slopes. Default is 12 (months).

    Returns
    -------
    Tuple[List[str], List[float], bool]
        A tuple containing (identified_trends, trend_strengths,
        anomalies_detected). The list lengths are equal and correspond to
        the same order.

    Raises
    ------
    ValueError
        Raised if `data` is empty or missing any of the specified `metrics`.
    TypeError
        Raised if `data` is not a pandas DataFrame or if `metrics` is not a
        list of strings.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'date': pd.date_range('2020-01-01', periods=24, freq='M'),
    ...     'GDP_growth': [2.5, 2.7, 2.6, 2.8, 3.0, 3.1, 3.3, 3.4, 3.5, 3.6,
    3.8, 4.0, 4.1, 4.3, 4.5, 4.6, 4.7, 4.9, 5.0, 5.1, 5.3, 5.4, 5.6, 5.8]
    >>> })
    >>> df.set_index('date', inplace=True)
    >>> trends, strengths, anomalies = conduct_preliminary_data_analysis(df,
    ['GDP_growth'])
    >>> print(trends)
    >>> print(strengths)
    >>> print(anomalies)
    ['upward']
    [0.045]
    False

    >>> df['inflation'] = [2.1, 2.3, 2.2, 2.5, 2.7, 2.6, 2.8, 3.0, 3.1, 3.2,
    3.4, 3.5, 3.6, 3.8, 4.0, 4.1, 4.2, 4.3, 4.5, 4.6, 4.8, 5.0, 5.2, 5.4]
    >>> trends, strengths, anomalies = conduct_preliminary_data_analysis(df,
    ['GDP_growth', 'inflation'], window_size=6)
    >>> print(trends)
    >>> print(strengths)
    >>> print(anomalies)
    ['upward', 'upward']
    [0.048, 0.054]
    True

    """
    return ConductPreliminaryDataAnalysisOutput(
        identified_trends=[],
        trend_strengths=[],
        anomalies_detected=False,
    )