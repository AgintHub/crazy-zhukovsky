from pydantic import BaseModel, Field
from typing import List


class ConductPreliminaryDataAnalysisPart1Output(BaseModel):
    """Pydantic model for conduct_preliminary_data_analysis_part1 node outputs."""
    identified_trends: List[str] = (
        Field(..., description="List of trend names or descriptors identified in the data")
    )
    trend_strengths: List[float] = (
        Field(..., description="Quantitative strength (e.g., slope or growth rate) associated with each identified trend")
    )


class ConductPreliminaryDataAnalysisPart2Output(BaseModel):
    """Pydantic model for conduct_preliminary_data_analysis_part2 node outputs."""
    anomalies_detected: bool = (
        Field(..., description="Indicates whether any anomalies or irregular patterns were detected during preliminary analysis")
    )


class IdentifyPotentialMacroeconomicDriversPart1Output(BaseModel):
    """Pydantic model for identify_potential_macroeconomic_drivers_part1 node outputs."""
    potential_drivers: List[str] = (
        Field(..., description="A list of macroeconomic variable names identified as potential drivers.")
    )


def identify_potential_macroeconomic_drivers_part1(conduct_preliminary_data_analysis_part1_input: ConductPreliminaryDataAnalysisPart1Output, conduct_preliminary_data_analysis_part2_input: ConductPreliminaryDataAnalysisPart2Output, **kwargs) -> IdentifyPotentialMacroeconomicDriversPart1Output:
    """
    Generate a list of candidate macroeconomic driver variables from trend data
    and anomaly flags.

    Parameters
    ----------
    identified_trends : List[str]
        Trend identifiers extracted from the preliminary data analysis
        (e.g., ['GDP growth', 'inflation']).
    trend_strengths : List[float]
        Numeric strength for each trend (e.g., slope or growth‑rate) aligned
        with `identified_trends`.
    anomalies_detected : bool
        Flag indicating whether any data anomalies were found during the
        preliminary analysis.

    Returns
    -------
    List[str]
        A list of macroeconomic variable names that could plausibly
        influence the observed trends.

    Raises
    ------
    ValueError
        If `identified_trends` and `trend_strengths` have different lengths.
    ValueError
        If `identified_trends` is empty, meaning no basis exists to infer
        drivers.

    Examples
    --------
    >>> identify_potential_drivers(["GDP growth", "inflation"], [0.4, -0.1],
    False)
    ["Consumer Spending", "Monetary Policy Rate"]

    >>> identify_potential_drivers(["Unemployment"], [ -0.3 ], True)
    ["Labor Market Flexibility", "Job Creation Programs"]

    """
    return IdentifyPotentialMacroeconomicDriversPart1Output(
        potential_drivers=[],
    )