"""
This module defines the command to retrieve tasks by a specific priority from the task repository.
The get_by_priority function is used as a CLI command to display tasks with the specified priority.
"""

import click

from src.cli.context import ApplicationContext
from src.utils.emoji import TURTLE_EMOJI


@click.command()
@click.argument("priority", type=int)
def get_by_priority(priority: int) -> None:
    """
    Get tasks by specific priority from the task repository.

    Args:
        priority (int): The priority of the tasks to retrieve.
    """
    context = ApplicationContext()
    tasks = context.task_service.get_tasks_by_priority(priority)
    if tasks:
        for task in tasks:
            click.echo(f"{TURTLE_EMOJI} {task}")
    else:
        click.echo(f"{TURTLE_EMOJI} No tasks found with the specified priority.")
