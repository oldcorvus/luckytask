"""
This module defines the command to add a new task to the task repository.
The add_task function is used as a CLI command to create a new task with specified name, priority, and description.
"""

import click

from src.cli.context import ApplicationContext
from src.utils.emoji import TURTLE_EMOJI


@click.command()
@click.argument("name")
@click.argument("priority", type=int)
@click.argument("description")
def add_task(name: str, priority: int, description: str) -> None:
    """
    Add a new task to the task repository.

    Args:
        name (str): The name of the task.
        priority (int): The priority of the task.
        description (str): The description of the task.
    """
    context = ApplicationContext()
    task = context.task_service.add_task(name, priority, description)
    click.echo(f"{TURTLE_EMOJI} Task added: {task}")
