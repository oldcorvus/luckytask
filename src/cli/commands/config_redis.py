"""
This module defines the command to configure Redis connection settings.
The config_redis function is used as a CLI command to set the host, port, and database for Redis connection.
"""

import click

from src.utils.config_handler import save_config
from src.utils.emoji import TURTLE_EMOJI


@click.command()
@click.option("--host", default="localhost", help="Redis server host.")
@click.option("--port", default=6379, type=int, help="Redis server port.")
@click.option("--db", default=0, type=int, help="Redis database number.")
def config_redis(host: str, port: int, db: int) -> None:
    """
    Configure Redis connection settings.

    Args:
        host (str): Redis server host.
        port (int): Redis server port.
        db (int): Redis database number.
    """
    config = {"host": host, "port": port, "db": db}
    save_config(config)
    click.echo(
        f"{TURTLE_EMOJI} Redis configured with host={host}, port={port}, db={db}"
    )
