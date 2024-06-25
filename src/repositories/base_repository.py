"""
This module defines the TaskRepository interface.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.entities.task import Task


class TaskRepository(ABC):
    """
    TaskRepository is an abstract base class that defines the interface for a task repository.

    Methods:
        add(task: Task) -> None:
            Adds a new task to the repository.
        get_by_id(task_id: str) -> Optional[Task]:
            Retrieves a task by its ID from the repository.
        list() -> List[Task]:
            Retrieves all tasks from the repository.
        list_by_priority(min_priority: int, max_priority: int) -> List[Task]:
            Retrieves tasks within a priority range from the repository.
        delete(task_id: str) -> bool:
            Deletes a task by its ID from the repository.
        update(task: Task) -> Optional[Task]:
            Updates a task in the repository.
    """

    @abstractmethod
    def add(self, task: Task) -> None:
        """
        Adds a new task to the repository.

        Args:
            task (Task): The task object to add.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("Method 'add' must be implemented.")

    @abstractmethod
    def get_by_id(self, task_id: str) -> Optional[Task]:
        """
        Retrieves a task by its ID from the repository.

        Args:
            task_id (str): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The retrieved task, or None if not found.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("Method 'get_by_id' must be implemented.")

    @abstractmethod
    def list(self) -> List[Task]:
        """
        Retrieves all tasks from the repository.

        Returns:
            List[Task]: A list of all tasks.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("Method 'list' must be implemented.")

    @abstractmethod
    def list_by_priority(self, min_priority: int, max_priority: int) -> List[Task]:
        """
        Retrieves tasks within a priority range from the repository.

        Args:
            min_priority (int): The minimum priority.
            max_priority (int): The maximum priority.

        Returns:
            List[Task]: A list of tasks within the specified priority range.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("Method 'list_by_priority' must be implemented.")

    @abstractmethod
    def delete(self, task_id: str) -> bool:
        """
        Deletes a task by its ID from the repository.

        Args:
            task_id (str): The ID of the task to delete.

        Returns:
            bool: True if the task was deleted, False otherwise.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("Method 'delete' must be implemented.")

    @abstractmethod
    def update(self, task: Task) -> Optional[Task]:
        """
        Updates a task in the repository.

        Args:
            task (Task): The task to update.

        Returns:
            Optional[Task]: The updated task, or None if not found.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("Method 'update' must be implemented.")
