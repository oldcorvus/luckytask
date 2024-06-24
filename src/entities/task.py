"""
This module defines the Task class using Pydantic for data validation and automatic timestamp setting.

Classes:
    Task: A Pydantic model representing a task with validation for priority and name fields.
"""

import time
from uuid import uuid4

from pydantic import BaseModel, Field, field_validator


class Task(BaseModel):
    """
    A class used to represent a Task.

    Attributes:
        id (str): The unique identifier for the task, generated automatically.
        name (str): The name of the task.
        priority (int): The priority of the task, must be between 1 and 10.
        description (str): A description of the task.
        timestamp (float): The creation timestamp of the task, set automatically.

    Methods:
        validate_priority(value): Validates that the priority is between 1 and 10.
        validate_name(value): Validates that the name is not empty.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    priority: int
    description: str
    timestamp: float = Field(default_factory=time.time)

    @field_validator("priority")
    def validate_priority(cls, value: int) -> int:
        """Validates that the priority is between 1 and 10."""
        if not 1 <= value <= 10:
            raise ValueError("Priority must be between 1 and 10")
        return value

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        """Validates that the name is not empty."""
        if not value:
            raise ValueError("Name cannot be empty")
        return value
