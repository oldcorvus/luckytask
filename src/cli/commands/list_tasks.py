"""
This module defines the command to list all tasks from the task repository.
The list_tasks function is used as a CLI command to display all tasks stored in the repository.
"""

import click

from src.cli.context import ApplicationContext
from src.utils.emoji import TURTLE_EMOJI


@click.command()
def list_tasks() -> None:
    """
    List all tasks from the task repository.
    """
    context = ApplicationContext()
    tasks = context.task_service.get_all_tasks()
    for task in tasks:
        click.echo(f"{TURTLE_EMOJI} {task}")
