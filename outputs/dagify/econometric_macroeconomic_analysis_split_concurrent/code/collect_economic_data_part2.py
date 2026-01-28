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


def collect_economic_data_part2(define_macroeconomic_objectives_part1_input: DefineMacroeconomicObjectivesPart1Output, define_macroeconomic_objectives_part2_input: DefineMacroeconomicObjectivesPart2Output, **kwargs) -> CollectEconomicDataPart2Output:
    """
    Preprocess raw macroeconomic data: normalize values, check unit consistency,
    and impute missing entries.

    Parameters
    ----------
    objectives : List[str]
        Primary macroeconomic objectives extracted from the input
        description (e.g., ['GDP growth', 'inflation control']).
    metrics : List[str]
        Key performance metrics linked to each objective (e.g., ['GDP growth
        rate', 'CPI inflation rate']).
    raw_records : list[dict]
        A list of raw data records fetched from the sources; each record is
        a dictionary mapping metric names to raw values and units.

    Returns
    -------
    dict
        Dictionary containing `data_records_count` (int),
        `preprocessing_successful` (bool), and `notes` (str) as defined in
        the node's output structure.

    Raises
    ------
    ValueError
        If `objectives` or `metrics` are empty, or if `raw_records` is not a
        non‑empty list.
    RuntimeError
        If normalization or imputation fails due to incompatible units or
        irrecoverable missing data.

    Examples
    --------
    >>> objectives = ['GDP growth', 'inflation control']
    >>> metrics = ['GDP growth rate', 'CPI inflation rate']
    >>> raw_records = [
    ...     {'GDP growth rate': 3.2, 'unit': '%', 'CPI inflation rate': None,
    'unit': '%'},
    ...     {'GDP growth rate': 2.9, 'unit': '%', 'CPI inflation rate': 2.1,
    'unit': '%'}
    >>> ]
    >>> result = preprocess_data(objectives, metrics, raw_records)
    {'data_records_count': 2, 'preprocessing_successful': True, 'notes':
    'Missing CPI value imputed using linear interpolation.'}

    >>> preprocess_data([], [], [])
    ValueError: objectives and metrics must be non‑empty.

    """
    return CollectEconomicDataPart2Output(
        data_records_count=0,
        preprocessing_successful=False,
        notes="",
    )