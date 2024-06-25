"""
This module defines the command to delete a task by its ID from the task repository.
The delete_task function is used as a CLI command to remove a specified task from the repository.
"""

import click

from src.cli.context import ApplicationContext
from src.utils.emoji import TURTLE_EMOJI


@click.command()
@click.argument("task_id")
def delete_task(task_id: str) -> None:
    """
    Delete a task by ID from the task repository.

    Args:
        task_id (str): The ID of the task to delete.
    """
    context = ApplicationContext()
    result = context.task_service.delete_task(task_id)
    if result:
        click.echo(f"{TURTLE_EMOJI} Task {task_id} deleted.")
    else:
        click.echo(f"{TURTLE_EMOJI} Task {task_id} not found.")
