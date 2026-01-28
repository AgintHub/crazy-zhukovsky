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


class CollectEconomicDataOutput(BaseModel):
    """Pydantic model for collect_economic_data node outputs."""
    data_source_names: List[str] = (
        Field(..., description="Names of data sources used (e.g., 'Bureau of Labor Statistics', 'World Bank').")
    )
    data_records_count: int = (
        Field(..., description="Total number of data records retrieved across all sources.")
    )
    preprocessing_successful: bool = (
        Field(..., description="Indicates whether preprocessing (adjustments, normalization) completed without errors.")
    )
    notes: str = (
        Field(..., description="Any additional remarks or issues encountered during data collection and preprocessing.")
    )


def collect_economic_data(define_macroeconomic_objectives_input: DefineMacroeconomicObjectivesOutput, **kwargs) -> CollectEconomicDataOutput:
    """
    Collects macroeconomic data from specified sources, performs normalization,
    and returns structured output for downstream analysis.

    Parameters
    ----------
    objectives : List[str]
        List of macroeconomic objectives (e.g., GDP growth, inflation
        control) guiding data collection priorities.
    metrics : List[str]
        Key performance metrics (e.g., GDP growth rate, CPI inflation) to
        extract and normalize.

    Returns
    -------
    Dict[str, Union[List[str], int, bool, str]]
        Dictionary containing formatted data sources, record counts,
        preprocessing status, and operational notes.

    Raises
    ------
    ConnectionError
        If unable to access a required data source API or database.
    ValueError
        If preprocessing steps fail due to incompatible data formats or
        missing required fields.

    Examples
    --------
    >>> collect_economic_data(['GDP growth', 'Inflation control'], ['GDP growth
    rate', 'CPI inflation rate'])
    {'data_source_names': ['Bureau of Labor Statistics', 'World Bank'],
    'data_records_count': 240, 'preprocessing_successful': True, 'notes': ''}

    >>> collect_economic_data(['Employment level'], ['Unemployment rate'],
    source_overrides=['Eurostat'])
    {'data_source_names': ['Eurostat'], 'data_records_count': 120,
    'preprocessing_successful': False, 'notes': 'Eurostat data contained
    inconsistent temporal resolution, imputation used'}

    """
    return CollectEconomicDataOutput(
        data_source_names=[],
        data_records_count=0,
        preprocessing_successful=False,
        notes="",
    )