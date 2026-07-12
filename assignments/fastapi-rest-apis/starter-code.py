"""Starter code for Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


# In-memory storage for tasks (for learning purposes).
tasks: list[Task] = []


@app.get("/")
def read_root() -> dict[str, str]:
    """TODO: Return a short welcome message as JSON."""
    return {"message": "Welcome to the Task API starter project"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """TODO: Return a simple API health status."""
    return {"status": "ok"}


@app.post("/tasks")
def create_task(task: Task) -> dict[str, object]:
    """TODO: Add input validation and duplicate-id checks if needed."""
    tasks.append(task)
    return {"message": "Task created", "task": task}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    """TODO: Return all tasks in memory."""
    return tasks


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task) -> dict[str, object]:
    """TODO: Replace the task with matching id or raise 404."""
    for index, existing_task in enumerate(tasks):
        if existing_task.id == task_id:
            tasks[index] = updated_task
            return {"message": "Task updated", "task": updated_task}

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    """TODO: Delete the task with matching id or raise 404."""
    for index, existing_task in enumerate(tasks):
        if existing_task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")
