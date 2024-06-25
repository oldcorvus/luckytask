"""
Unit tests for TaskService using a FakeTaskRepository.

Tests:
- test_add_task: Verifies adding a task to the service and repository.
- test_get_all_tasks: Verifies retrieving all tasks from the service.
- test_get_tasks_by_priority: Verifies retrieving tasks by priority from the service.
- test_get_tasks_by_priority_range: Verifies retrieving tasks within a priority range from the service.
- test_delete_task: Verifies deleting a task from the service and repository.
- test_update_task: Verifies updating a task in the service and repository.
"""

import unittest

from src.entities.task import Task
from src.repositories.fake_repository import FakeTaskRepository
from src.services.task_service import TaskService


class TestTaskServiceWithFakeRepository(unittest.TestCase):
    """
    TestTaskServiceWithFakeRepository contains unit tests for TaskService using a FakeTaskRepository.

    Methods:
        setUp() -> None:
            Sets up the test environment with a FakeTaskRepository and TaskService.
        test_add_task() -> None:
            Verifies adding a task to the service and repository.
        test_get_all_tasks() -> None:
            Verifies retrieving all tasks from the service.
        test_get_tasks_by_priority() -> None:
            Verifies retrieving tasks by priority from the service.
        test_get_tasks_by_priority_range() -> None:
            Verifies retrieving tasks within a priority range from the service.
        test_delete_task() -> None:
            Verifies deleting a task from the service and repository.
        test_update_task() -> None:
            Verifies updating a task in the service and repository.
    """

    def setUp(self) -> None:
        """
        Set up test environment with FakeTaskRepository and TaskService.
        """
        self.fake_repository: FakeTaskRepository = FakeTaskRepository()
        self.service: TaskService = TaskService(repository=self.fake_repository)

    def test_add_task(self) -> None:
        """
        Test case for adding a task to the service.
        """
        task: Task = self.service.add_task(
            name="Test Task", priority=5, description="This is a test task"
        )
        self.assertIn(task.id, self.fake_repository.tasks)
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.priority, 5)
        self.assertEqual(task.description, "This is a test task")

    def test_get_all_tasks(self) -> None:
        """
        Test case for retrieving all tasks from the service.
        """
        task1: Task = self.service.add_task(
            name="Task 1", priority=1, description="Description 1"
        )
        task2: Task = self.service.add_task(
            name="Task 2", priority=2, description="Description 2"
        )

        result: list[Task] = self.service.get_all_tasks()
        self.assertEqual(len(result), 2)
        self.assertIn(task1, result)
        self.assertIn(task2, result)

    def test_get_tasks_by_priority(self) -> None:
        """
        Test case for retrieving tasks by priority from the service.
        """
        task: Task = self.service.add_task(
            name="Task 1", priority=5, description="Description 1"
        )

        result: list[Task] = self.service.get_tasks_by_priority(5)
        self.assertEqual(result, [task])

    def test_get_tasks_by_priority_range(self) -> None:
        """
        Test case for retrieving tasks within a priority range from the service.
        """
        task1: Task = self.service.add_task(
            name="Task 1", priority=3, description="Description 1"
        )
        task2: Task = self.service.add_task(
            name="Task 2", priority=5, description="Description 2"
        )

        result: list[Task] = self.service.get_tasks_by_priority_range(3, 5)
        self.assertEqual(len(result), 2)
        self.assertIn(task1, result)
        self.assertIn(task2, result)

    def test_delete_task(self) -> None:
        """
        Test case for deleting a task from the service.
        """
        task: Task = self.service.add_task(
            name="Task 1", priority=3, description="Description 1"
        )

        result: bool = self.service.delete_task(task.id)
        self.assertTrue(result)
        self.assertNotIn(task.id, self.fake_repository.tasks)

    def test_update_task(self) -> None:
        """
        Test case for updating a task in the service.
        """
        task: Task = self.service.add_task(
            name="Task 1", priority=3, description="Description 1"
        )
        updated_task = self.service.update_task(
            task.id, name="Updated Task", priority=5, description="Updated Description"
        )
        if updated_task is None:
            self.fail("Task not found")

        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.name, "Updated Task")
        self.assertEqual(updated_task.priority, 5)
        self.assertEqual(updated_task.description, "Updated Description")
        self.assertEqual(self.fake_repository.tasks[task.id], updated_task)


if __name__ == "__main__":
    unittest.main()
