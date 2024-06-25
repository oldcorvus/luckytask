
# 🐢 LuckyTask

LuckyTask is a CLI tool to manage tasks with a Redis backend. It allows you to add, list, delete, update tasks, and configure Redis connection settings.

## Features

- Add a new task
- List all tasks
- Get tasks by specific priority
- Get tasks by priority range
- Delete a task by ID
- Update a task by ID
- Configure Redis connection settings

## Installation

You can install the package using Poetry:

```sh
poetry install
```

## Usage

After installing, you can use the `luckytask` command to manage your tasks.

### Add a Task

To add a new task:

```sh
luckytask add-task "Task 4" 8 "Sample description"
```
🐢 Task added: id='a4099d38-c92f-4d2c-9254-e3b6ba520726' name='Task 4' priority=8 description='Sample description' timestamp=1719274988.0359566


### List All Tasks

To list all tasks:

```sh
luckytask list-tasks
```
🐢 id='8e4d55a4-019a-4900-9099-458eca956d5a' name='Task 2' priority=1 description='Sample description' timestamp=1719275722.1838574

🐢 id='70688bb5-c8d9-4df7-bca9-99f1390e4d44' name='Task 3' priority=1 description='Sample description' timestamp=1719275727.4264348

🐢 id='b59ed13a-7660-441b-ace6-d5caa61bbb37' name='Task 1' priority=3 description='Sample description' timestamp=1719275714.860256

🐢 id='cc77f464-dcb5-4536-a2c9-6b10d85fbef5' name='Task 5' priority=5 description='Sample description' timestamp=1719275737.764184

🐢 id='776baa27-802d-4d66-af6c-57f08f3670da' name='Task 4' priority=8 description='Sample description' timestamp=1719275706.1597753

🐢 id='f3b7da5f-4d3b-4dc1-9f43-68b1aef7988b' name='Task 6' priority=10 description='Sample description' timestamp=1719275745.6112974

### Get Tasks by Specific Priority

To get tasks by specific priority:

```sh
luckytask get-by-priority 1
```
🐢 id='8e4d55a4-019a-4900-9099-458eca956d5a' name='Task 2' priority=1 description='Sample description' timestamp=1719275722.1838574

🐢 id='70688bb5-c8d9-4df7-bca9-99f1390e4d44' name='Task 3' priority=1 description='Sample description' timestamp=1719275727.4264348


### Get Tasks by Priority Range

To get tasks within a priority range:

```sh
luckytask get-by-priority-range 2 5
```
🐢 id='b59ed13a-7660-441b-ace6-d5caa61bbb37' name='Task 1' priority=3 description='Sample description' timestamp=1719275714.860256

🐢 id='cc77f464-dcb5-4536-a2c9-6b10d85fbef5' name='Task 5' priority=5 description='Sample description' timestamp=1719275737.764184

### Delete a Task

To delete a task by ID:

```sh
luckytask delete-task <task_id>
```
🐢 Task cc77f464-dcb5-4536-a2c9-6b10d85fbef5 deleted.

### Update a Task

To update a task by ID:

```sh
luckytask update-task b59ed13a-7660-441b-ace6-d5caa61bbb37 --name "Updated Task" --priority 3 --description "Updated description"
```
🐢 Task updated: id='b59ed13a-7660-441b-ace6-d5caa61bbb37' name='Updated Task' priority=3 description='Updated description' timestamp=1719275714.860256

### Configure Redis

To configure Redis connection settings:

```sh
luckytask config-redis --host 127.0.0.1 --port 6379 --db 1
```

## Using Docker

You can also run LuckyTask using Docker. Below are the steps to build and run the Docker container.

### Docker Image

1. **Build the Docker Image**
   Build the Docker Image

   ```sh
   docker build -t luckytask .
   ```

2. **Run the Docker Container**:

   ```sh
   docker run -it luckytask <command> <arguments>
   ```

   For example, to add a task:

   ```sh
   docker run -it luckytask add-task "Task 1" 5 "Sample description"
   ```

### Docker Compose

Alternatively, you can use Docker Compose.

1. **Build and Run the Container**:

   ```sh
   docker-compose up --build -d
   ```

2. **Run Commands Inside the Container**:

   ```sh
   docker-compose run luckytask luckytask <command> <arguments>
   ```

   For example, to list all tasks:

   ```sh
   docker-compose run luckytask luckytask list-tasks
   ```
   🐢 id='8e4d55a4-019a-4900-9099-458eca956d5a' name='Task 2' priority=1 description='Sample description' timestamp=1719275722.1838574

   🐢 id='70688bb5-c8d9-4df7-bca9-99f1390e4d44' name='Task 3' priority=1 description='Sample description' timestamp=1719275727.4264348

   🐢 id='b59ed13a-7660-441b-ace6-d5caa61bbb37' name='Updated Task' priority=3 description='Updated description' timestamp=1719275714.860256

   🐢 id='776baa27-802d-4d66-af6c-57f08f3670da' name='Task 4' priority=8 description='Sample description' timestamp=1719275706.1597753

   🐢 id='f3b7da5f-4d3b-4dc1-9f43-68b1aef7988b' name='Task 6' priority=10 description='Sample description' timestamp=1719275745.6112974

