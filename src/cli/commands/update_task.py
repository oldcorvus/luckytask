"""
This module defines the command to update a task by its ID in the task repository.
The update_task function is used as a CLI command to modify the details of a specified task.
"""

from typing import Optional

import click

from src.cli.context import ApplicationContext
from src.utils.emoji import TURTLE_EMOJI


@click.command()
@click.argument("task_id")
@click.option("--name", default=None, help="New name of the task.")
@click.option("--priority", default=None, type=int, help="New priority of the task.")
@click.option("--description", default=None, help="New description of the task.")
def update_task(
    task_id: str,
    name: Optional[str],
    priority: Optional[int],
    description: Optional[str],
) -> None:
    """
    Update a task by ID in the task repository.

    Args:
        task_id (str): The ID of the task to update.
        name (Optional[str]): The new name of the task.
        priority (Optional[int]): The new priority of the task.
        description (Optional[str]): The new description of the task.
    """
    context = ApplicationContext()
    task = context.task_service.update_task(
        task_id, name=name, priority=priority, description=description
    )
    if task:
        click.echo(f"{TURTLE_EMOJI} Task updated: {task}")
    else:
        click.echo(f"{TURTLE_EMOJI} Task {task_id} not found.")
