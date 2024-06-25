"""
task_service.py

This module defines the TaskService class for managing tasks.
"""

from typing import List, Optional

from src.entities.task import Task
from src.repositories.base_repository import TaskRepository


class TaskService:
    """
    TaskService provides an interface for managing tasks by interacting with a TaskRepository.

    Methods:
        add_task(name: str, priority: int, description: str) -> Task:
            Adds a new task to the repository.
        get_all_tasks() -> List[Task]:
            Retrieves all tasks from the repository.
        get_tasks_by_priority(priority: int) -> List[Task]:
            Retrieves tasks from the repository by priority.
        get_tasks_by_priority_range(min_priority: int, max_priority: int) -> List[Task]:
            Retrieves tasks from the repository within a priority range.
        delete_task(task_id: str) -> bool:
            Deletes a task from the repository.
        update_task(task_id: str, **kwargs) -> Optional[Task]:
            Updates a task in the repository.
    """

    def __init__(self, repository: TaskRepository):
        """
        Initialize the TaskService with a repository.

        Args:
            repository (TaskRepository): The repository to use for task management.

        """
        self.repository: TaskRepository = repository

    def add_task(self, name: str, priority: int, description: str) -> Task:
        """
        Adds a new task to the repository.

        Args:
            name (str): The name of the task.
            priority (int): The priority of the task.
            description (str): The description of the task.

        Returns:
            Task: The added Task object.

        """
        task: Task = Task(name=name, priority=priority, description=description)
        self.repository.add(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks from the repository.

        Returns:
            List[Task]: A list of all Task objects.

        """
        return self.repository.list()

    def get_tasks_by_priority(self, priority: int) -> List[Task]:
        """
        Retrieves tasks from the repository by priority.

        Args:
            priority (int): The priority value to filter tasks.

        Returns:
            List[Task]: A list of Task objects with the specified priority.

        """
        return self.repository.list_by_priority(priority, priority)

    def get_tasks_by_priority_range(
        self, min_priority: int, max_priority: int
    ) -> List[Task]:
        """
        Retrieves tasks from the repository within a priority range.

        Args:
            min_priority (int): The minimum priority value.
            max_priority (int): The maximum priority value.

        Returns:
            List[Task]: A list of Task objects within the specified priority range.

        """
        return self.repository.list_by_priority(min_priority, max_priority)

    def delete_task(self, task_id: str) -> bool:
        """
        Deletes a task from the repository.

        Args:
            task_id (str): The ID of the task to delete.

        Returns:
            bool: True if the task was successfully deleted, False otherwise.

        """
        return self.repository.delete(task_id)

    def update_task(self, task_id: str, **kwargs) -> Optional[Task]:
        """
        Updates a task in the repository.

        Args:
            task_id (str): The ID of the task to update.
            **kwargs: Keyword arguments representing fields to update in the task.

        Returns:
            Optional[Task]: The updated Task object if successful, None if the task was not found.

        """
        task: Optional[Task] = self.repository.get_by_id(task_id)
        if not task:
            return None

        updated_fields: dict = {
            key: value for key, value in kwargs.items() if value is not None
        }
        for key, value in updated_fields.items():
            setattr(task, key, value)

        return self.repository.update(task)
