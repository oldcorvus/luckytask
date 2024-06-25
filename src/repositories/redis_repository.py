"""
This module implements the TaskRepository interface using Redis for storage.
"""

from typing import List, Optional

from src.adapters.redis_client import RedisClient
from src.entities.task import Task
from src.repositories.base_repository import TaskRepository
from src.utils.exceptions import RedisOperationError


class RedisTaskRepository(TaskRepository):
    """
    RedisTaskRepository is a concrete implementation of the TaskRepository interface,
    using Redis as the storage backend for tasks.

    Methods:
        add(task: Task) -> None:
            Adds a task to the Redis database.
        get_by_id(task_id: str) -> Optional[Task]:
            Retrieves a task from the Redis database by its ID.
        list() -> List[Task]:
            Retrieves all tasks from the Redis database.
        list_by_priority(min_priority: int, max_priority: int) -> List[Task]:
            Retrieves tasks within a specified priority range from the Redis database.
        delete(task_id: str) -> bool:
            Deletes a task from the Redis database by its ID.
        update(task: Task) -> Optional[Task]:
            Updates a task in the Redis database.
    """

    def __init__(self, redis_client: RedisClient):
        """
        Initialize the RedisTaskRepository with a RedisClient.

        Args:
            redis_client (RedisClient): The Redis client instance for database operations.
        """
        self.redis_client: RedisClient = redis_client

    def add(self, task: Task) -> None:
        """
        Add a task to Redis.

        Args:
            task (Task): The task object to add.

        Raises:
            RedisOperationError: If there is an error adding the task to Redis.
        """
        try:
            client = self.redis_client.get_client()
            task_key = f"task:{task.id}"
            score = task.priority + task.timestamp / 1e10
            client.hset(
                task_key,
                mapping={
                    "id": task.id,
                    "name": task.name,
                    "priority": task.priority,
                    "description": task.description,
                    "timestamp": task.timestamp,
                },
            )
            client.zadd("tasks", {task_key: score})
        except Exception as e:
            raise RedisOperationError(f"Failed to add task to Redis: {e}")

    def get_by_id(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a task from Redis by task ID.

        Args:
            task_id (str): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The Task object if found, None otherwise.

        Raises:
            RedisOperationError: If there is an error retrieving the task from Redis.
        """
        try:
            client = self.redis_client.get_client()
            task_key = f"task:{task_id}"
            task_data = client.hgetall(task_key)
            if task_data:
                return Task.model_validate(
                    {k.decode("utf-8"): v.decode("utf-8") for k, v in task_data.items()}
                )
            return None
        except Exception as e:
            raise RedisOperationError(f"Failed to retrieve task from Redis: {e}")

    def list(self) -> List[Task]:
        """
        Retrieve all tasks from Redis.

        Returns:
            List[Task]: A list of Task objects stored in Redis.

        Raises:
            RedisOperationError: If there is an error listing tasks from Redis.
        """
        try:
            client = self.redis_client.get_client()
            task_keys = client.zrange("tasks", 0, -1)
            return [
                task
                for task in (
                    self.get_by_id(task_key.decode("utf-8").split(":")[1])
                    for task_key in task_keys
                )
                if task is not None
            ]
        except Exception as e:
            raise RedisOperationError(f"Failed to list tasks from Redis: {e}")

    def list_by_priority(self, min_priority: int, max_priority: int) -> List[Task]:
        """
        Retrieve tasks from Redis within a priority range.

        Args:
            min_priority (int): The minimum priority value.
            max_priority (int): The maximum priority value.

        Returns:
            List[Task]: A list of Task objects within the specified priority range.

        Raises:
            RedisOperationError: If there is an error listing tasks by priority from Redis.
        """
        try:
            client = self.redis_client.get_client()
            min_score = min_priority
            max_score = max_priority + 1 - 1e-10
            task_keys = client.zrangebyscore("tasks", min_score, max_score)
            return [
                task
                for task in (
                    self.get_by_id(task_key.decode("utf-8").split(":")[1])
                    for task_key in task_keys
                )
                if task is not None
            ]
        except Exception as e:
            raise RedisOperationError(
                f"Failed to list tasks by priority from Redis: {e}"
            )

    def delete(self, task_id: str) -> bool:
        """
        Delete a task from Redis by task ID.

        Args:
            task_id (str): The ID of the task to delete.

        Returns:
            bool: True if the task was successfully deleted, False otherwise.

        Raises:
            RedisOperationError: If there is an error deleting the task from Redis.
        """
        try:
            client = self.redis_client.get_client()
            task_key = f"task:{task_id}"
            client.delete(task_key)
            client.zrem("tasks", task_key)
            return True
        except Exception as e:
            raise RedisOperationError(f"Failed to delete task from Redis: {e}")

    def update(self, task: Task) -> Optional[Task]:
        """
        Update a task in Redis.

        Args:
            task (Task): The updated task object.

        Returns:
            Optional[Task]: The updated Task object if successful, None if the task was not found.
        """
        self.add(task)  # Re-add the task to update in Redis
        return task
