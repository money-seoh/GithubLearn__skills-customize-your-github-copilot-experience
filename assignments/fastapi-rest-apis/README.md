# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a basic REST API using the FastAPI framework. In this assignment, you will create endpoints, validate request data, and return JSON responses for a simple task manager service.

## 📝 Tasks

### 🛠️ Build Your First FastAPI App

#### Description
Set up a FastAPI application and implement foundational endpoints so you can run and test your API locally.

#### Requirements
Completed program should:

- Create a FastAPI app instance in starter-code.py.
- Add a GET endpoint at / that returns a welcome JSON message.
- Add a GET endpoint at /health that returns a status value such as {"status": "ok"}.
- Run successfully with Uvicorn and respond to requests in the browser or API docs.


### 🛠️ Implement Task CRUD Endpoints

#### Description
Extend the API into a small in-memory task manager where users can create, view, update, and delete tasks.

#### Requirements
Completed program should:

- Define a Task model with id, title, and completed fields.
- Add a POST endpoint at /tasks to create a task.
- Add a GET endpoint at /tasks to return all tasks.
- Add a PUT endpoint at /tasks/{task_id} to update an existing task.
- Add a DELETE endpoint at /tasks/{task_id} to remove a task.
- Return clear error responses when a task id is not found.
