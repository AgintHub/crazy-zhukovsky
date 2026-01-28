from pydantic import BaseModel, Field
from typing import List


class DefineMacroeconomicObjectivesPart2Output(BaseModel):
    """Pydantic model for define_macroeconomic_objectives_part2 node outputs."""
    metrics: List[str] = (
        Field(..., description="List of key performance metrics associated with each objective (e.g., GDP growth rate, CPI inflation rate, unemployment rate).")
    )


def define_macroeconomic_objectives_part2(general_input: str, **kwargs) -> DefineMacroeconomicObjectivesPart2Output:
    """
    Extract key performance metrics corresponding to the defined macroeconomic
    objectives.

    Parameters
    ----------
    input_text : str
        Free-form textual description containing macroeconomic objectives
        from which performance metrics must be identified and extracted.

    Returns
    -------
    List[str]
        List of key performance metrics (e.g., GDP growth rate, CPI
        inflation rate) associated with the macroeconomic objectives
        mentioned in the input text.

    Raises
    ------
    ValueError
        If the input_text is empty or contains only whitespace.
    TypeError
        If the input_text is not of type string.

    Examples
    --------
    >>> extract_metrics('The government aims to boost GDP growth, control
    inflation, and reduce unemployment.')
    ['GDP growth rate', 'CPI inflation rate', 'unemployment rate']

    >>> extract_metrics('Maintain price stability and achieve full employment.')
    ['inflation rate', 'employment rate']

    """
    return DefineMacroeconomicObjectivesPart2Output(
        metrics=[],
    )