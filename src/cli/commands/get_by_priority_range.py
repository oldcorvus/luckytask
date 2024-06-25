"""
This module defines the command to retrieve tasks by a range of priorities from the task repository.
The get_by_priority_range function is used as a CLI command to display tasks within the specified priority range.
"""

import click

from src.cli.context import ApplicationContext
from src.utils.emoji import TURTLE_EMOJI


@click.command()
@click.argument("min_priority", type=int)
@click.argument("max_priority", type=int)
def get_by_priority_range(min_priority: int, max_priority: int) -> None:
    """
    Get tasks by priority range from the task repository.

    Args:
        min_priority (int): The minimum priority of the tasks to retrieve.
        max_priority (int): The maximum priority of the tasks to retrieve.
    """
    context = ApplicationContext()
    tasks = context.task_service.get_tasks_by_priority_range(min_priority, max_priority)
    if tasks:
        for task in tasks:
            click.echo(f"{TURTLE_EMOJI} {task}")
    else:
        click.echo(
            f"{TURTLE_EMOJI} No tasks found within the specified priority range."
        )
