# DevFlow

DevFlow is a web application for managing software development workflows.

The system allows users to manage tasks, workers, teams and task types.

## Features

* Create tasks
* Update tasks
* Delete tasks
* View task details
* Manage teams
* Manage workers
* Manage task types
* Django Admin Panel
* Bootstrap Interface

## Technologies

* Python 3
* Django
* SQLite
* Bootstrap 5
* HTML
* CSS

## Database Structure

### Team

Stores development teams.

### Worker

Stores workers and their positions.

### TaskType

Stores task categories.

### Task

Stores tasks, priorities, statuses and deadlines.

## Installation

```bash
git clone <repository-url>

cd dev-flow

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Screenshots

Add screenshots here.

## Author

Matheus Araujo Nascimento
