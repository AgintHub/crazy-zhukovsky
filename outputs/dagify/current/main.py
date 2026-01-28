import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.apply_econometric_models import apply_econometric_models
from code.collect_economic_data import collect_economic_data
from code.conduct_preliminary_data_analysis import conduct_preliminary_data_analysis
from code.conduct_trend_analysis import conduct_trend_analysis
from code.define_macroeconomic_objectives import define_macroeconomic_objectives
from code.draw_implications_and_recommendations import draw_implications_and_recommendations
from code.evaluate_model_performance import evaluate_model_performance
from code.identify_key_macroeconomic_drivers import identify_key_macroeconomic_drivers
from code.identify_potential_macroeconomic_drivers import identify_potential_macroeconomic_drivers

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

apply_econometric_models_async = make_async(apply_econometric_models)
collect_economic_data_async = make_async(collect_economic_data)
conduct_preliminary_data_analysis_async = make_async(conduct_preliminary_data_analysis)
conduct_trend_analysis_async = make_async(conduct_trend_analysis)
define_macroeconomic_objectives_async = make_async(define_macroeconomic_objectives)
draw_implications_and_recommendations_async = make_async(draw_implications_and_recommendations)
evaluate_model_performance_async = make_async(evaluate_model_performance)
identify_key_macroeconomic_drivers_async = make_async(identify_key_macroeconomic_drivers)
identify_potential_macroeconomic_drivers_async = make_async(identify_potential_macroeconomic_drivers)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_macroeconomic_objectives
    async def run_define_macroeconomic_objectives():
        # Call the async version of define_macroeconomic_objectives with results from dependencies
        return await define_macroeconomic_objectives_async(user_input)

    # Run level 0 nodes in parallel
    results['define_macroeconomic_objectives'] = await run_define_macroeconomic_objectives()

    # Level 1: collect_economic_data, conduct_preliminary_data_analysis
    async def run_collect_economic_data():
        # Call the async version of collect_economic_data with results from dependencies
        return await collect_economic_data_async(results['define_macroeconomic_objectives'])

    async def run_conduct_preliminary_data_analysis():
        # Call the async version of conduct_preliminary_data_analysis with results from dependencies
        return await conduct_preliminary_data_analysis_async(results['define_macroeconomic_objectives'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_collect_economic_data(), run_conduct_preliminary_data_analysis())
    results['collect_economic_data'] = level_1_results[0]
    results['conduct_preliminary_data_analysis'] = level_1_results[1]

    # Level 2: conduct_trend_analysis, identify_potential_macroeconomic_drivers
    async def run_conduct_trend_analysis():
        # Call the async version of conduct_trend_analysis with results from dependencies
        return await conduct_trend_analysis_async(results['collect_economic_data'])

    async def run_identify_potential_macroeconomic_drivers():
        # Call the async version of identify_potential_macroeconomic_drivers with results from dependencies
        return await identify_potential_macroeconomic_drivers_async(results['conduct_preliminary_data_analysis'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_conduct_trend_analysis(), run_identify_potential_macroeconomic_drivers())
    results['conduct_trend_analysis'] = level_2_results[0]
    results['identify_potential_macroeconomic_drivers'] = level_2_results[1]

    # Level 3: identify_key_macroeconomic_drivers
    async def run_identify_key_macroeconomic_drivers():
        # Call the async version of identify_key_macroeconomic_drivers with results from dependencies
        return await identify_key_macroeconomic_drivers_async(results['collect_economic_data'], results['identify_potential_macroeconomic_drivers'])

    # Run level 3 nodes in parallel
    results['identify_key_macroeconomic_drivers'] = await run_identify_key_macroeconomic_drivers()

    # Level 4: apply_econometric_models
    async def run_apply_econometric_models():
        # Call the async version of apply_econometric_models with results from dependencies
        return await apply_econometric_models_async(results['conduct_trend_analysis'], results['identify_key_macroeconomic_drivers'], results['identify_potential_macroeconomic_drivers'])

    # Run level 4 nodes in parallel
    results['apply_econometric_models'] = await run_apply_econometric_models()

    # Level 5: evaluate_model_performance
    async def run_evaluate_model_performance():
        # Call the async version of evaluate_model_performance with results from dependencies
        return await evaluate_model_performance_async(results['apply_econometric_models'])

    # Run level 5 nodes in parallel
    results['evaluate_model_performance'] = await run_evaluate_model_performance()

    # Level 6: draw_implications_and_recommendations
    async def run_draw_implications_and_recommendations():
        # Call the async version of draw_implications_and_recommendations with results from dependencies
        return await draw_implications_and_recommendations_async(results['evaluate_model_performance'])

    # Run level 6 nodes in parallel
    results['draw_implications_and_recommendations'] = await run_draw_implications_and_recommendations()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
