from pydantic import BaseModel, Field
from typing import List


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


class IdentifyPotentialMacroeconomicDriversOutput(BaseModel):
    """Pydantic model for identify_potential_macroeconomic_drivers node outputs."""
    potential_drivers: List[str] = (
        Field(..., description="A list of macroeconomic variable names identified as potential drivers.")
    )


class IdentifyKeyMacroeconomicDriversOutput(BaseModel):
    """Pydantic model for identify_key_macroeconomic_drivers node outputs."""
    key_variables: List[str] = (
        Field(..., description="List of identified key macroeconomic variables.")
    )
    importance_scores: List[float] = (
        Field(..., description="Relative importance score for each key variable (higher indicates greater influence).")
    )
    relationship_strength: List[float] = (
        Field(..., description="Numeric strength of the relationship between each key variable and the target macroeconomic indicator.")
    )
    relationship_direction: List[str] = (
        Field(..., description="Direction of the relationship for each key variable (e.g., 'positive', 'negative').")
    )


def identify_key_macroeconomic_drivers(collect_economic_data_input: CollectEconomicDataOutput, identify_potential_macroeconomic_drivers_input: IdentifyPotentialMacroeconomicDriversOutput, **kwargs) -> IdentifyKeyMacroeconomicDriversOutput:
    """
    Identify key macroeconomic drivers and their relationships with the target
    indicator.

    Parameters
    ----------
    data : pd.DataFrame
        Preprocessed macroeconomic time‑series data obtained from
        collect_economic_data. Columns represent potential drivers and the
        target indicator.
    potential_drivers : List[str]
        List of variable names identified by
        identify_potential_macroeconomic_drivers.
    target_indicator : str
        Column name of the macroeconomic indicator to be forecasted (e.g.,
        'GDP_growth').

    Returns
    -------
    Dict[str, List[Union[str, float]]]
        Dictionary containing four lists: key_variables, importance_scores,
        relationship_strength, and relationship_direction.

    Raises
    ------
    ValueError
        Raised if target_indicator is not in data columns or
        potential_drivers is empty.
    RuntimeError
        Raised if correlation analysis fails due to insufficient data
        points.

    Examples
    --------
    >>> import pandas as pd
    >>> # Sample data frame
    >>> df = pd.DataFrame({
    ...     'GDP_growth': [2.5, 2.7, 3.0, 2.9, 3.2],
    ...     'Inflation': [1.2, 1.3, 1.1, 1.4, 1.2],
    ...     'Unemployment': [5.0, 4.8, 4.6, 4.7, 4.5],
    ...     'Interest_Rate': [0.5, 0.6, 0.4, 0.5, 0.5]
    >>> })
    >>> # Potential drivers identified earlier
    >>> potential = ['Inflation', 'Unemployment', 'Interest_Rate']
    >>> # Identify key drivers
    >>> result = identify_key_macroeconomic_drivers(df, potential, 'GDP_growth')
    >>> print(result['key_variables'])
    >>> print(result['importance_scores'])
    >>> print(result['relationship_strength'])
    >>> print(result['relationship_direction'])
    ['Unemployment', 'Inflation', 'Interest_Rate']
    [0.95, 0.78, 0.65]
    [0.92, 0.75, 0.60]
    ['negative', 'negative', 'positive']

    >>> # Handling error: target not in data
    >>> try:
    ...     identify_key_macroeconomic_drivers(df, potential, 'NonExistent')
    >>> except ValueError as e:
    ...     print(e)
    'target_indicator 'NonExistent' not found in data columns.'

    """
    return IdentifyKeyMacroeconomicDriversOutput(
        key_variables=[],
        importance_scores=[],
        relationship_strength=[],
        relationship_direction=[],
    )