"""
This module implements a fake in-memory TaskRepository for testing purposes.

Classes:
    FakeTaskRepository: An in-memory implementation of the TaskRepository interface.

"""

from typing import List, Optional

from src.entities.task import Task
from src.repositories.base_repository import TaskRepository


class FakeTaskRepository(TaskRepository):
    """
    An in-memory implementation of the TaskRepository interface for testing.

    Methods:
        add(task: Task) -> None: Adds a new task to the in-memory store.
        get_by_id(task_id: str) -> Optional[Task]: Retrieves a task by its ID from the in-memory store.
        list() -> List[Task]: Retrieves all tasks from the in-memory store.
        list_by_priority(min_priority: int, max_priority: int) -> List[Task]: Retrieves tasks within a priority range from the in-memory store.
        delete(task_id: str) -> bool: Deletes a task by its ID from the in-memory store.
        update(task: Task) -> Optional[Task]: Updates a task in the in-memory store.
    """

    def __init__(self) -> None:
        """Initializes the in-memory task store."""
        self.tasks: dict[str, Task] = {}
        self.priority_index: list[tuple[int, str]] = []

    def add(self, task: Task) -> None:
        """
        Adds a new task to the in-memory store.

        Args:
            task (Task): The task to add.
        """
        self.tasks[task.id] = task
        self.priority_index.append((task.priority, task.id))
        self.priority_index.sort()

    def get_by_id(self, task_id: str) -> Optional[Task]:
        """
        Retrieves a task by its ID from the in-memory store.

        Args:
            task_id (str): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The retrieved task, or None if not found.
        """
        return self.tasks.get(task_id, None)

    def list(self) -> List[Task]:
        """
        Retrieves all tasks from the in-memory store.

        Returns:
            List[Task]: A list of all tasks.
        """
        return [self.tasks[task_id] for _, task_id in self.priority_index]

    def list_by_priority(self, min_priority: int, max_priority: int) -> List[Task]:
        """
        Retrieves tasks within a priority range from the in-memory store.

        Args:
            min_priority (int): The minimum priority.
            max_priority (int): The maximum priority.

        Returns:
            List[Task]: A list of tasks within the specified priority range.
        """
        return [
            self.tasks[task_id]
            for priority, task_id in self.priority_index
            if min_priority <= priority <= max_priority
        ]

    def delete(self, task_id: str) -> bool:
        """
        Deletes a task by its ID from the in-memory store.

        Args:
            task_id (str): The ID of the task to delete.

        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.priority_index = [
                (priority, id) for priority, id in self.priority_index if id != task_id
            ]
            return True
        return False

    def update(self, task: Task) -> Optional[Task]:
        """
        Updates a task in the in-memory store.

        Args:
            task (Task): The task to update.

        Returns:
            Optional[Task]: The updated task, or None if not found.
        """
        if task.id in self.tasks:
            self.tasks[task.id] = task
            self.priority_index = [
                (task.priority, task.id) if id == task.id else (priority, id)
                for priority, id in self.priority_index
            ]
            self.priority_index.sort()
            return task
        return None
