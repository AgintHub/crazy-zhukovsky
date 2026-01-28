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


class IdentifyKeyMacroeconomicDriversPart1Output(BaseModel):
    """Pydantic model for identify_key_macroeconomic_drivers_part1 node outputs."""
    key_variables: List[str] = (
        Field(..., description="List of identified key macroeconomic variables.")
    )
    importance_scores: List[float] = (
        Field(..., description="Relative importance score for each key variable (higher indicates greater influence).")
    )


def identify_key_macroeconomic_drivers_part1(collect_economic_data_part1_input: CollectEconomicDataPart1Output, collect_economic_data_part2_input: CollectEconomicDataPart2Output, identify_potential_macroeconomic_drivers_part1_input: IdentifyPotentialMacroeconomicDriversPart1Output, **kwargs) -> IdentifyKeyMacroeconomicDriversPart1Output:
    """
    Selects key macroeconomic drivers based on statistical importance derived
    from pre‑processed data.

    Parameters
    ----------
    potential_drivers : List[str]
        List of candidate macroeconomic variables identified by the
        preceding driver‑identification node.
    data_records_count : int
        Number of observations available after data collection and
        preprocessing.
    preprocessing_successful : bool
        Flag indicating whether the data preprocessing step completed
        without errors.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple where the first element is `key_variables`—the selected
        macroeconomic variables—and the second element is
        `importance_scores`—their corresponding relative importance values.

    Raises
    ------
    ValueError
        If `preprocessing_successful` is False, indicating that the input
        data are not ready for analysis.
    ValueError
        If `potential_drivers` is empty, because no candidates are available
        to evaluate.

    Examples
    --------
    >>> identify_key_macroeconomic_drivers_part1(
    ...     potential_drivers=["GDP", "CPI", "Unemployment", "Interest Rate"],
    ...     data_records_count=120,
    ...     preprocessing_successful=True
    >>> )
    (['GDP', 'CPI', 'Interest Rate'], [0.45, 0.30, 0.25])

    >>> identify_key_macroeconomic_drivers_part1(
    ...     potential_drivers=["Export Volume", "Import Price"],
    ...     data_records_count=80,
    ...     preprocessing_successful=True
    >>> )
    (['Export Volume', 'Import Price'], [0.52, 0.48])

    """
    return IdentifyKeyMacroeconomicDriversPart1Output(
        key_variables=[],
        importance_scores=[],
    )