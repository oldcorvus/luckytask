"""
This module serves as the main entry point for the Task Management CLI application.
It groups the various commands defined in the commands package and sets up the CLI interface using Click.
"""

import click

from src.cli.commands.add_task import add_task
from src.cli.commands.config_redis import config_redis
from src.cli.commands.delete_task import delete_task
from src.cli.commands.get_by_priority import get_by_priority
from src.cli.commands.get_by_priority_range import get_by_priority_range
from src.cli.commands.list_tasks import list_tasks
from src.cli.commands.update_task import update_task


@click.group()
def cli() -> None:
    """Task Management CLI."""
    pass


cli.add_command(add_task)
cli.add_command(list_tasks)
cli.add_command(get_by_priority)
cli.add_command(get_by_priority_range)
cli.add_command(delete_task)
cli.add_command(update_task)
cli.add_command(config_redis)

if __name__ == "__main__":
    cli()
