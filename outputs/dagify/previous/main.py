import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.define_macroeconomic_objectives_part1 import define_macroeconomic_objectives_part1
from code.define_macroeconomic_objectives_part2 import define_macroeconomic_objectives_part2
from code.collect_economic_data_part1 import collect_economic_data_part1
from code.collect_economic_data_part2 import collect_economic_data_part2
from code.conduct_preliminary_data_analysis_part1 import conduct_preliminary_data_analysis_part1
from code.conduct_preliminary_data_analysis_part2 import conduct_preliminary_data_analysis_part2
from code.conduct_trend_analysis_part1 import conduct_trend_analysis_part1
from code.conduct_trend_analysis_part2 import conduct_trend_analysis_part2
from code.identify_potential_macroeconomic_drivers_part1 import identify_potential_macroeconomic_drivers_part1
from code.identify_key_macroeconomic_drivers_part1 import identify_key_macroeconomic_drivers_part1
from code.identify_key_macroeconomic_drivers_part2 import identify_key_macroeconomic_drivers_part2
from code.apply_econometric_models_part1 import apply_econometric_models_part1
from code.apply_econometric_models_part2 import apply_econometric_models_part2
from code.evaluate_model_performance_part1 import evaluate_model_performance_part1
from code.evaluate_model_performance_part2 import evaluate_model_performance_part2
from code.draw_implications_and_recommendations_part1 import draw_implications_and_recommendations_part1
from code.draw_implications_and_recommendations_part2 import draw_implications_and_recommendations_part2

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

define_macroeconomic_objectives_part1_async = make_async(define_macroeconomic_objectives_part1)
define_macroeconomic_objectives_part2_async = make_async(define_macroeconomic_objectives_part2)
collect_economic_data_part1_async = make_async(collect_economic_data_part1)
collect_economic_data_part2_async = make_async(collect_economic_data_part2)
conduct_preliminary_data_analysis_part1_async = make_async(conduct_preliminary_data_analysis_part1)
conduct_preliminary_data_analysis_part2_async = make_async(conduct_preliminary_data_analysis_part2)
conduct_trend_analysis_part1_async = make_async(conduct_trend_analysis_part1)
conduct_trend_analysis_part2_async = make_async(conduct_trend_analysis_part2)
identify_potential_macroeconomic_drivers_part1_async = make_async(identify_potential_macroeconomic_drivers_part1)
identify_key_macroeconomic_drivers_part1_async = make_async(identify_key_macroeconomic_drivers_part1)
identify_key_macroeconomic_drivers_part2_async = make_async(identify_key_macroeconomic_drivers_part2)
apply_econometric_models_part1_async = make_async(apply_econometric_models_part1)
apply_econometric_models_part2_async = make_async(apply_econometric_models_part2)
evaluate_model_performance_part1_async = make_async(evaluate_model_performance_part1)
evaluate_model_performance_part2_async = make_async(evaluate_model_performance_part2)
draw_implications_and_recommendations_part1_async = make_async(draw_implications_and_recommendations_part1)
draw_implications_and_recommendations_part2_async = make_async(draw_implications_and_recommendations_part2)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_macroeconomic_objectives_part2, define_macroeconomic_objectives_part1
    async def run_define_macroeconomic_objectives_part2():
        # Call the async version of define_macroeconomic_objectives_part2 with results from dependencies
        return await define_macroeconomic_objectives_part2_async(user_input)

    async def run_define_macroeconomic_objectives_part1():
        # Call the async version of define_macroeconomic_objectives_part1 with results from dependencies
        return await define_macroeconomic_objectives_part1_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_define_macroeconomic_objectives_part2(), run_define_macroeconomic_objectives_part1())
    results['define_macroeconomic_objectives_part2'] = level_0_results[0]
    results['define_macroeconomic_objectives_part1'] = level_0_results[1]

    # Level 1: collect_economic_data_part1, conduct_preliminary_data_analysis_part2, collect_economic_data_part2, conduct_preliminary_data_analysis_part1
    async def run_collect_economic_data_part1():
        # Call the async version of collect_economic_data_part1 with results from dependencies
        return await collect_economic_data_part1_async(results['define_macroeconomic_objectives_part1'], results['define_macroeconomic_objectives_part2'])

    async def run_conduct_preliminary_data_analysis_part2():
        # Call the async version of conduct_preliminary_data_analysis_part2 with results from dependencies
        return await conduct_preliminary_data_analysis_part2_async(results['define_macroeconomic_objectives_part1'], results['define_macroeconomic_objectives_part2'])

    async def run_collect_economic_data_part2():
        # Call the async version of collect_economic_data_part2 with results from dependencies
        return await collect_economic_data_part2_async(results['define_macroeconomic_objectives_part1'], results['define_macroeconomic_objectives_part2'])

    async def run_conduct_preliminary_data_analysis_part1():
        # Call the async version of conduct_preliminary_data_analysis_part1 with results from dependencies
        return await conduct_preliminary_data_analysis_part1_async(results['define_macroeconomic_objectives_part1'], results['define_macroeconomic_objectives_part2'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_collect_economic_data_part1(), run_conduct_preliminary_data_analysis_part2(), run_collect_economic_data_part2(), run_conduct_preliminary_data_analysis_part1())
    results['collect_economic_data_part1'] = level_1_results[0]
    results['conduct_preliminary_data_analysis_part2'] = level_1_results[1]
    results['collect_economic_data_part2'] = level_1_results[2]
    results['conduct_preliminary_data_analysis_part1'] = level_1_results[3]

    # Level 2: identify_potential_macroeconomic_drivers_part1, conduct_trend_analysis_part2, conduct_trend_analysis_part1
    async def run_identify_potential_macroeconomic_drivers_part1():
        # Call the async version of identify_potential_macroeconomic_drivers_part1 with results from dependencies
        return await identify_potential_macroeconomic_drivers_part1_async(results['conduct_preliminary_data_analysis_part1'], results['conduct_preliminary_data_analysis_part2'])

    async def run_conduct_trend_analysis_part2():
        # Call the async version of conduct_trend_analysis_part2 with results from dependencies
        return await conduct_trend_analysis_part2_async(results['collect_economic_data_part1'], results['collect_economic_data_part2'])

    async def run_conduct_trend_analysis_part1():
        # Call the async version of conduct_trend_analysis_part1 with results from dependencies
        return await conduct_trend_analysis_part1_async(results['collect_economic_data_part1'], results['collect_economic_data_part2'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_identify_potential_macroeconomic_drivers_part1(), run_conduct_trend_analysis_part2(), run_conduct_trend_analysis_part1())
    results['identify_potential_macroeconomic_drivers_part1'] = level_2_results[0]
    results['conduct_trend_analysis_part2'] = level_2_results[1]
    results['conduct_trend_analysis_part1'] = level_2_results[2]

    # Level 3: identify_key_macroeconomic_drivers_part2, identify_key_macroeconomic_drivers_part1
    async def run_identify_key_macroeconomic_drivers_part2():
        # Call the async version of identify_key_macroeconomic_drivers_part2 with results from dependencies
        return await identify_key_macroeconomic_drivers_part2_async(results['collect_economic_data_part1'], results['collect_economic_data_part2'], results['identify_potential_macroeconomic_drivers_part1'])

    async def run_identify_key_macroeconomic_drivers_part1():
        # Call the async version of identify_key_macroeconomic_drivers_part1 with results from dependencies
        return await identify_key_macroeconomic_drivers_part1_async(results['collect_economic_data_part1'], results['collect_economic_data_part2'], results['identify_potential_macroeconomic_drivers_part1'])

    # Run level 3 nodes in parallel
    level_3_results = await asyncio.gather(run_identify_key_macroeconomic_drivers_part2(), run_identify_key_macroeconomic_drivers_part1())
    results['identify_key_macroeconomic_drivers_part2'] = level_3_results[0]
    results['identify_key_macroeconomic_drivers_part1'] = level_3_results[1]

    # Level 4: apply_econometric_models_part1, apply_econometric_models_part2
    async def run_apply_econometric_models_part1():
        # Call the async version of apply_econometric_models_part1 with results from dependencies
        return await apply_econometric_models_part1_async(results['conduct_trend_analysis_part1'], results['conduct_trend_analysis_part2'], results['identify_key_macroeconomic_drivers_part1'], results['identify_key_macroeconomic_drivers_part2'])

    async def run_apply_econometric_models_part2():
        # Call the async version of apply_econometric_models_part2 with results from dependencies
        return await apply_econometric_models_part2_async(results['conduct_trend_analysis_part1'], results['conduct_trend_analysis_part2'], results['identify_key_macroeconomic_drivers_part1'], results['identify_key_macroeconomic_drivers_part2'])

    # Run level 4 nodes in parallel
    level_4_results = await asyncio.gather(run_apply_econometric_models_part1(), run_apply_econometric_models_part2())
    results['apply_econometric_models_part1'] = level_4_results[0]
    results['apply_econometric_models_part2'] = level_4_results[1]

    # Level 5: evaluate_model_performance_part1
    async def run_evaluate_model_performance_part1():
        # Call the async version of evaluate_model_performance_part1 with results from dependencies
        return await evaluate_model_performance_part1_async(results['apply_econometric_models_part1'], results['apply_econometric_models_part2'])

    # Run level 5 nodes in parallel
    results['evaluate_model_performance_part1'] = await run_evaluate_model_performance_part1()

    # Level 6: evaluate_model_performance_part2
    async def run_evaluate_model_performance_part2():
        # Call the async version of evaluate_model_performance_part2 with results from dependencies
        return await evaluate_model_performance_part2_async(results['evaluate_model_performance_part1'])

    # Run level 6 nodes in parallel
    results['evaluate_model_performance_part2'] = await run_evaluate_model_performance_part2()

    # Level 7: draw_implications_and_recommendations_part2, draw_implications_and_recommendations_part1
    async def run_draw_implications_and_recommendations_part2():
        # Call the async version of draw_implications_and_recommendations_part2 with results from dependencies
        return await draw_implications_and_recommendations_part2_async(results['evaluate_model_performance_part1'], results['evaluate_model_performance_part2'])

    async def run_draw_implications_and_recommendations_part1():
        # Call the async version of draw_implications_and_recommendations_part1 with results from dependencies
        return await draw_implications_and_recommendations_part1_async(results['evaluate_model_performance_part1'], results['evaluate_model_performance_part2'])

    # Run level 7 nodes in parallel
    level_7_results = await asyncio.gather(run_draw_implications_and_recommendations_part2(), run_draw_implications_and_recommendations_part1())
    results['draw_implications_and_recommendations_part2'] = level_7_results[0]
    results['draw_implications_and_recommendations_part1'] = level_7_results[1]

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
