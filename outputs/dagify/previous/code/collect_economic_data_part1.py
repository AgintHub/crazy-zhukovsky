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


class CollectEconomicDataPart1Output(BaseModel):
    """Pydantic model for collect_economic_data_part1 node outputs."""
    data_source_names: List[str] = (
        Field(..., description="Names of data sources used (e.g., 'Bureau of Labor Statistics', 'World Bank').")
    )


def collect_economic_data_part1(define_macroeconomic_objectives_part1_input: DefineMacroeconomicObjectivesPart1Output, define_macroeconomic_objectives_part2_input: DefineMacroeconomicObjectivesPart2Output, **kwargs) -> CollectEconomicDataPart1Output:
    """
    Retrieve a list of reputable data source names that can provide the
    requested macroeconomic series.

    Parameters
    ----------
    objectives : List[str]
        Primary macroeconomic objectives extracted from the input
        description (e.g., ['GDP growth', 'inflation control']).
    metrics : List[str]
        Key performance metrics associated with each objective (e.g., ['GDP
        growth rate', 'CPI inflation rate']).

    Returns
    -------
    List[str]
        A list of data source names that are capable of supplying the
        required series (e.g., ['World Bank', 'Bureau of Labor
        Statistics']).

    Raises
    ------
    ValueError
        If either *objectives* or *metrics* is empty or not a list of
        strings.
    RuntimeError
        If no suitable data source can be identified for the supplied
        objectives/metrics.

    Examples
    --------
    >>> collect_economic_data(['GDP growth'], ['GDP growth rate'])
    ['World Bank', 'Bureau of Labor Statistics']

    >>> collect_economic_data(['Unemployment'], ['Unemployment rate'])
    ['International Labour Organization', 'U.S. Bureau of Labor Statistics']

    """
    return CollectEconomicDataPart1Output(
        data_source_names=[],
    )