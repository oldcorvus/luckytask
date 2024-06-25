"""
This module handles reading and writing configuration settings to a JSON file.
"""

import json
import os

CONFIG_FILE = "config.json"


def save_config(config: dict) -> None:
    """
    Save configuration settings to a JSON file.

    Args:
        config (dict): The configuration settings to save.
    """
    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file)


def load_config() -> dict:
    """
    Load configuration settings from a JSON file.

    Returns:
        dict: The configuration settings.
    """
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as config_file:
                return json.load(config_file)
        return {}

    except Exception:
        return {}
