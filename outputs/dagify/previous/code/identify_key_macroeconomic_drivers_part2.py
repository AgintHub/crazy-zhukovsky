from pydantic import BaseModel, Field
from typing import List


class CollectEconomicDataPart1Output(BaseModel):
    """Pydantic model for collect_economic_data_part1 node outputs."""
    data_source_names: List[str] = (
        Field(..., description="Names of data sources used (e.g., 'Bureau of Labor Statistics', 'World Bank').")
    )


class CollectEconomicDataPart2Output(BaseModel):
    """Pydantic model for collect_economic_data_part2 node outputs."""
    data_records_count: int = (
        Field(..., description="Total number of data records retrieved across all sources.")
    )
    preprocessing_successful: bool = (
        Field(..., description="Indicates whether preprocessing (adjustments, normalization) completed without errors.")
    )
    notes: str = (
        Field(..., description="Any additional remarks or issues encountered during data collection and preprocessing.")
    )


class IdentifyPotentialMacroeconomicDriversPart1Output(BaseModel):
    """Pydantic model for identify_potential_macroeconomic_drivers_part1 node outputs."""
    potential_drivers: List[str] = (
        Field(..., description="A list of macroeconomic variable names identified as potential drivers.")
    )


class IdentifyKeyMacroeconomicDriversPart2Output(BaseModel):
    """Pydantic model for identify_key_macroeconomic_drivers_part2 node outputs."""
    relationship_strength: List[float] = (
        Field(..., description="Numeric strength of the relationship between each key variable and the target macroeconomic indicator.")
    )
    relationship_direction: List[str] = (
        Field(..., description="Direction of the relationship for each key variable (e.g., 'positive', 'negative').")
    )


def identify_key_macroeconomic_drivers_part2(collect_economic_data_part1_input: CollectEconomicDataPart1Output, collect_economic_data_part2_input: CollectEconomicDataPart2Output, identify_potential_macroeconomic_drivers_part1_input: IdentifyPotentialMacroeconomicDriversPart1Output, **kwargs) -> IdentifyKeyMacroeconomicDriversPart2Output:
    """
    Compute relationship strength and direction between selected macro variables
    and a target macroeconomic indicator.

    Parameters
    ----------
    data : pandas.DataFrame
        Pre‑processed economic dataset where each column is a macroeconomic
        variable and rows correspond to time periods.
    key_variables : List[str]
        List of macroeconomic variable names whose relationship to the
        target indicator should be evaluated.
    target_indicator : str
        Name of the macroeconomic indicator that serves as the dependent
        variable (e.g., 'Inflation').

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple where the first element is a list of numeric relationship
        strengths (absolute correlation or standardized coefficient) and the
        second element is a list of strings ('positive' or 'negative')
        indicating the direction for each key variable, preserving the order
        of `key_variables`.

    Raises
    ------
    KeyError
        If any of the `key_variables` or `target_indicator` are not present
        in `data` columns.
    ValueError
        If `key_variables` is empty or contains duplicates.

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     "GDP_growth": [2.5, 3.0, 2.8, 3.2],
    ...     "Unemployment": [5.0, 4.8, 5.1, 4.9],
    ...     "Inflation": [1.8, 2.0, 1.9, 2.1]
    >>> })
    >>> key_vars = ["GDP_growth", "Unemployment"]
    >>> target = "Inflation"
    >>> strength, direction = determine_relationships(data, key_vars, target)
    >>> print(strength)
    >>> print(direction)
    [0.97, -0.85]\n['positive', 'negative']

    """
    return IdentifyKeyMacroeconomicDriversPart2Output(
        relationship_strength=[],
        relationship_direction=[],
    )